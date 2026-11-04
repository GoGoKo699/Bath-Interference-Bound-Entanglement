#!/usr/bin/env python3
"""Reproduce independent checks of the exact Davies-channel results.

Run from the repository root:
    python verification/run_all.py

No network access, optimization solver, symbolic-algebra package, or plotting
library is needed. A failure raises an exception and exits nonzero.
"""

from __future__ import annotations

import csv
import importlib.metadata
import json
import math
from pathlib import Path
import platform

import numpy as np
from scipy.linalg import expm

import exact_formulas as exact
import lindblad_model as model


OUTPUT_DIRECTORY = Path(__file__).resolve().parent / "results"
TOLERANCE = 5e-11
ETA_GRID = (0.0, 0.001, 0.01, 0.1, 0.25, 0.5, 0.75, 0.99, 1.0)
TEMPERATURE_GRID = (0.0, 1e-4, 0.1)
POPULATION_INDICES = (0, 5, 10, 15)


class Checks:
    def __init__(self) -> None:
        self.results: dict[str, dict[str, float | int | bool]] = {}

    def small(self, name: str, error: float, tolerance: float = TOLERANCE) -> None:
        error = float(error)
        if not math.isfinite(error) or error > tolerance:
            raise AssertionError(f"{name}: error {error:.17g} exceeds {tolerance:.17g}")
        entry = self.results.setdefault(name, {"max_error": 0.0, "tolerance": tolerance,
                                               "evaluations": 0, "passed": True})
        entry["max_error"] = max(float(entry["max_error"]), error)
        entry["evaluations"] = int(entry["evaluations"]) + 1

    def equal(self, name: str, left: np.ndarray | float,
              right: np.ndarray | float, tolerance: float = TOLERANCE) -> None:
        self.small(name, float(np.max(np.abs(np.asarray(left) - np.asarray(right)))), tolerance)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def minimum_eigenvalue(matrix: np.ndarray) -> float:
    return float(np.linalg.eigvalsh((matrix + matrix.conj().T) / 2.0)[0])


def binary_entropy(value: float) -> float:
    if value <= 0.0 or value >= 1.0:
        return 0.0
    return -value * math.log2(value) - (1.0 - value) * math.log2(1.0 - value)


def recurrence_rate(fidelity: float, projection_probability: float) -> dict[str, float | int]:
    """A nonoptimized lower bound with isotropic retwirling after every round."""
    require(fidelity > 0.5, "The distillation check requires F > 1/2.")
    fidelity = min(1.0, fidelity)
    yield_factor = projection_probability
    rounds = 0
    initial_fidelity = fidelity
    while fidelity < 0.9:
        other = (1.0 - fidelity) / 3.0
        success = fidelity**2 + 2.0 * fidelity * other + 5.0 * other**2
        next_fidelity = (fidelity**2 + other**2) / success
        require(next_fidelity > fidelity, "Recurrence did not increase F.")
        yield_factor *= success / 2.0
        fidelity = next_fidelity
        rounds += 1
        require(rounds < 1000, "Unexpected failure of recurrence convergence.")
    hashing_yield = 1.0 - binary_entropy(fidelity) - (1.0 - fidelity) * math.log2(3.0)
    rate = yield_factor * hashing_yield
    require(rate > 0.0, "Expected a strictly positive illustrative rate.")
    return {
        "initial_fidelity": initial_fidelity,
        "projection_probability": projection_probability,
        "recurrence_rounds": rounds,
        "final_fidelity": fidelity,
        "hashing_yield": hashing_yield,
        "positive_rate_lower_bound": rate,
    }


def eb_components() -> list[tuple[str, tuple[str, ...], np.ndarray]]:
    result = [("singleton", (name,), model.singleton_channel(name)) for name in exact.GAMMAS]
    result += [("triple", names, model.triple_channel(names)) for names in model.commuting_triples()]
    return result


def component_weight(kind: str, names: tuple[str, ...], q: dict[str, float]) -> float:
    if kind == "singleton":
        return q["r"] - 3.0 * q["b"] + 2.0 * q["v"] if names[0] == "IZ" else q["u"] - q["v"]
    return q["b"] - 2.0 * q["v"] / 3.0 if "IZ" in names else q["v"] / 3.0


def main() -> None:
    checks = Checks()
    populations = np.ix_(POPULATION_INDICES, POPULATION_INDICES)
    trace_functional = model.IDENTITY.reshape(-1)
    hamiltonian_part = model.superoperator(
        lambda operator: -1j * (model.HAMILTONIAN @ operator - operator @ model.HAMILTONIAN))
    gamma_set = set(exact.GAMMAS)
    triples = model.commuting_triples()
    require(len(triples) == 15, "Expected fifteen maximal commuting Pauli triples.")
    require(all(len(gamma_set.intersection(triple)) == 1 for triple in triples),
            "Each triple must contain exactly one gamma.")
    require(sum("IZ" in triple for triple in triples) == 3,
            "Exactly three triples must contain Gamma_0.")
    for name in model.PAULIS:
        if name != "II":
            require(sum(name in triple for triple in triples) == 3,
                    f"Incorrect incidence count for {name}.")

    components = eb_components()
    require(len(components) == 20, "Expected twenty EB component channels.")
    for kind, names, channel in components:
        checks.small("component_trace_preservation", model.trace_preservation_error(channel))
        state = model.choi(channel)
        checks.small("component_choi_positivity", max(0.0, -minimum_eigenvalue(state)))
        retained = set(names) | {"II"}
        for name, pauli in model.PAULIS.items():
            target = pauli if name in retained else np.zeros((4, 4), dtype=complex)
            checks.equal("component_retained_coefficients", model.apply(channel, pauli), target)

    coherent_parts = model.bohr_components()
    require(len(coherent_parts) == 26, "The perturbation proof uses twenty-six Bohr components.")
    require(max(abs(frequency) for frequency, _ in coherent_parts) == 8.0,
            "The maximum absolute Bohr frequency must be eight.")
    for _, jump in coherent_parts:
        require(np.linalg.norm(jump, ord=2) <= 1.0 + TOLERANCE,
                "The perturbation proof requires jump norm at most one.")

    cached_generators = {}
    thermal_rows = []
    for beta in TEMPERATURE_GRID:
        reference = model.generator_from_pauli_couplings(0.0, beta)
        rho = model.gibbs_state(beta)
        metric = np.diag(np.tile(np.diag(rho), 4))
        for eta in ETA_GRID:
            generator = model.generator_from_pauli_couplings(eta, beta)
            direct_blocks = model.generator_from_frequency_blocks(eta, beta)
            checks.equal("two_generator_representations", generator, direct_blocks)
            checks.equal("generator_trace_preservation", trace_functional @ generator, 0.0)
            checks.equal("specified_hamiltonian_covariance", generator @ hamiltonian_part,
                         hamiltonian_part @ generator)
            checks.equal("gibbs_stationarity", generator @ rho.reshape(-1), 0.0)
            heisenberg_generator = generator.conj().T
            checks.equal("gns_detailed_balance", metric @ heisenberg_generator,
                         heisenberg_generator.conj().T @ metric)
            checks.equal("matched_population_generator", generator[populations], reference[populations])
            checks.equal("matched_matrix_unit_self_damping", np.diag(generator), np.diag(reference))
            if beta == 0.0:
                cached_generators[eta] = generator
                nonzero_rates = [-eigenvalue.real for eigenvalue in np.linalg.eigvals(generator)
                                 if abs(eigenvalue) > 1e-9]
                checks.equal("infinite_temperature_gap", min(nonzero_rates), 8.0)

        time = exact.finite_beta_certificate()["time"]
        state = model.choi(expm(time * model.generator_from_pauli_couplings(1.0, beta)))
        thermal_rows.append({
            "beta": beta,
            "eta": 1.0,
            "time": time,
            "ppt_minimum_eigenvalue": minimum_eigenvalue(model.partial_transpose(state)),
            "breuer_hall_minimum_eigenvalue": minimum_eigenvalue(model.breuer_hall_output(state)),
            "status": "analytically_certified_below" if beta in (0.0, 1e-4) else "numerical_observation_only",
        })

    expected_population_generator = np.asarray(
        [[-8, 2, 4, 2], [2, -8, 2, 4], [4, 2, -8, 2], [2, 4, 2, -8]], dtype=float)
    checks.equal("explicit_population_matrix", cached_generators[0.0][populations],
                 expected_population_generator)

    psi = np.zeros(16, dtype=complex)
    psi[1], psi[4] = 1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0)
    omega = np.zeros(16, dtype=complex)
    omega[[0, 5, 10, 15]] = 0.5
    local_indices = (0, 1, 4, 5)
    local_block = np.ix_(local_indices, local_indices)
    phi_plus = np.asarray([1.0, 0.0, 0.0, 1.0]) / math.sqrt(2.0)
    threshold_rows = []
    capacity_rows = []
    for eta in ETA_GRID:
        generator = cached_generators[eta]
        time_ppt, time_eb = exact.thresholds(eta)
        require(time_eb >= time_ppt - TOLERANCE, "Threshold ordering failed.")
        if eta > 0.0:
            require(time_eb > time_ppt, "Every positive sampled eta must give a strict interval.")
        times = (0.0, 0.05, 0.13, 0.9 * time_ppt, time_ppt,
                 (time_ppt + time_eb) / 2.0, time_eb, 0.4)
        for time in times:
            channel = expm(time * generator)
            state = model.choi(channel)
            partial = model.partial_transpose(state)
            witness_output = model.breuer_hall_output(state)
            q = exact.parameters(eta, time)
            eigenvalues = exact.multipliers(eta, time)
            for name, pauli in model.PAULIS.items():
                checks.equal("physical_channel_pauli_multipliers", model.apply(channel, pauli),
                             eigenvalues[name] * pauli)
            expected_choi = sum(eigenvalues[name] * np.kron(pauli.T, pauli)
                                for name, pauli in model.PAULIS.items()) / 16.0
            checks.equal("physical_channel_choi_expansion", state, expected_choi)
            checks.small("channel_trace_preservation", model.trace_preservation_error(channel))
            checks.equal("choi_normalization", np.trace(state), 1.0)
            checks.equal("choi_hermiticity", state, state.conj().T)
            checks.small("channel_complete_positivity", max(0.0, -minimum_eigenvalue(state)))
            checks.equal("partial_transpose_complete_spectrum", np.linalg.eigvalsh(partial),
                         exact.ppt_spectrum(eta, time))
            minimum = (1.0 - q["r"] - 2.0 * q["u"] - 2.0 * q["v"]) / 16.0
            checks.equal("rank_two_partial_transpose_eigenvector", partial @ psi, minimum * psi)
            witness_value = (1.0 - q["r"] - 4.0 * q["u"]) / 8.0
            checks.equal("breuer_hall_eigenvector", witness_output @ omega, witness_value * omega)
            checks.equal("breuer_hall_minimum", minimum_eigenvalue(witness_output), witness_value)

            projected = state[local_block]
            probability = float(np.trace(projected).real)
            expected_probability, expected_conditional = exact.projected_state(eta, time)
            checks.equal("projection_success_probability", probability, expected_probability)
            checks.equal("normalized_projected_state", projected / probability, expected_conditional)
            checks.equal("projected_state_trace", np.trace(projected / probability), 1.0)
            projected_minimum = minimum_eigenvalue(model.partial_transpose(projected / probability, 2))
            checks.equal("projected_partial_transpose_minimum", projected_minimum,
                         minimum / probability)

        q = exact.parameters(eta, time_eb)
        weights = [component_weight(kind, names, q) for kind, names, _ in components]
        require(min(weights) >= -TOLERANCE, "An EB mixture weight is negative.")
        checks.equal("eb_weight_normalization", sum(weights), 1.0)
        reconstructed = sum(weight * component[2] for weight, component in zip(weights, components))
        expected_channel = expm(time_eb * generator)
        reconstruction_error = float(np.max(np.abs(reconstructed - expected_channel)))
        checks.small("actual_measure_prepare_reconstruction", reconstruction_error)
        checks.small("reconstructed_channel_trace_preservation", model.trace_preservation_error(reconstructed))
        threshold_rows.append({
            "eta": eta,
            "t_ppt": time_ppt,
            "t_eb": time_eb,
            "binding_interval_width": time_eb - time_ppt,
            "minimum_mixture_weight": min(weights),
            "mixture_weight_sum": sum(weights),
            "actual_channel_reconstruction_error": reconstruction_error,
        })
        for fraction in (0.0, 0.5, 0.9):
            time = fraction * time_ppt
            state = model.choi(expm(time * generator))
            projected = state[local_block]
            probability = float(np.trace(projected).real)
            fidelity = float(np.vdot(phi_plus, (projected / probability) @ phi_plus).real)
            row = {"eta": eta, "time": time, "fraction_of_t_ppt": fraction}
            row.update(recurrence_rate(fidelity, probability))
            capacity_rows.append(row)

    checks.equal("eta_zero_equal_thresholds", exact.thresholds(0.0)[0], exact.thresholds(0.0)[1])
    checks.equal("eta_one_ppt_closed_form", exact.thresholds(1.0)[0], math.log(2.0) / 4.0)
    checks.equal("eta_one_eb_closed_form", exact.thresholds(1.0)[1], math.log(5.0) / 8.0)
    require(all(a["t_ppt"] < b["t_ppt"] and a["t_eb"] < b["t_eb"]
                for a, b in zip(threshold_rows, threshold_rows[1:])),
            "Sampled thresholds must increase with eta.")

    certificate = exact.finite_beta_certificate()
    require(certificate["certified_ppt_margin"] > 0.0,
            "Analytical finite-beta PPT margin is not positive.")
    require(certificate["certified_bh_negative_margin"] > 0.0,
            "Analytical finite-beta entanglement margin is not positive.")
    time = certificate["time"]
    state_zero = model.choi(expm(time * model.generator_from_pauli_couplings(1.0, 0.0)))
    state_beta = model.choi(expm(time * model.generator_from_pauli_couplings(1.0, certificate["beta"])))
    trace_distance = float(np.linalg.svd(state_beta - state_zero, compute_uv=False).sum())
    certificate["observed_choi_trace_norm_difference"] = trace_distance
    require(trace_distance < certificate["diamond_distance_upper_bound"],
            "Observed Choi difference exceeds the analytical upper bound.")
    checks.equal("finite_beta_zero_ppt_reference", minimum_eigenvalue(model.partial_transpose(state_zero)),
                 certificate["beta_zero_ppt_margin"])
    checks.equal("finite_beta_zero_bh_reference", minimum_eigenvalue(model.breuer_hall_output(state_zero)),
                 -certificate["beta_zero_bh_negative_margin"])
    require(minimum_eigenvalue(model.partial_transpose(state_beta)) > 0.0,
            "The certified finite-beta point is not numerically PPT.")
    require(minimum_eigenvalue(model.breuer_hall_output(state_beta)) < 0.0,
            "The certified finite-beta point is not detected as entangled.")

    result = {
        "schema_version": 1,
        "scope": "Finite-dimensional numerical checks of the stated analytical results; not interval arithmetic or a capacity-value computation.",
        "environment": {"python": platform.python_version(),
                        "numpy": importlib.metadata.version("numpy"),
                        "scipy": importlib.metadata.version("scipy")},
        "configuration": {"eta_grid": ETA_GRID, "beta_grid": TEMPERATURE_GRID,
                          "absolute_tolerance": TOLERANCE, "times_per_eta": 8},
        "checks": checks.results,
        "commuting_triples": triples,
        "eb_component_count": len(components),
        "thresholds": threshold_rows,
        "small_interference_coefficients": exact.small_eta_coefficients(),
        "thermal_examples": thermal_rows,
        "finite_beta_certificate": certificate,
        "illustrative_distillation_rates": capacity_rows,
    }
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIRECTORY / "verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    with (OUTPUT_DIRECTORY / "thresholds.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(threshold_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(threshold_rows)

    maximum = max(float(entry["max_error"]) for entry in checks.results.values())
    print(json.dumps({"status": "passed", "check_families": len(checks.results),
                      "eta_values": len(ETA_GRID), "beta_values": len(TEMPERATURE_GRID),
                      "maximum_absolute_residual": maximum,
                      "certified_finite_beta_ppt_margin": certificate["certified_ppt_margin"],
                      "certified_finite_beta_entanglement_margin": certificate["certified_bh_negative_margin"],
                      "outputs": ["verification/results/verification.json", "verification/results/thresholds.csv"]},
                     indent=2))


if __name__ == "__main__":
    main()
