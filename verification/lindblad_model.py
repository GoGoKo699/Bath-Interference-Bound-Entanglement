"""Direct finite-dimensional model, independent of the threshold formulas.

Matrices are vectorized in row-major order. Superoperators are constructed by
their action on matrix units. Choi states use a normalized maximally entangled
input and are assembled explicitly, without a reshape-only Choi convention.
"""

from __future__ import annotations

from collections.abc import Callable
from itertools import combinations

import numpy as np


DIM = 4
IDENTITY = np.eye(DIM, dtype=complex)
SINGLE_PAULIS = {
    "I": np.eye(2, dtype=complex),
    "X": np.asarray([[0, 1], [1, 0]], dtype=complex),
    "Y": np.asarray([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.diag([1, -1]).astype(complex),
}
PAULIS = {
    a + b: np.kron(SINGLE_PAULIS[a], SINGLE_PAULIS[b])
    for a in "IXYZ" for b in "IXYZ"
}
ENERGIES = np.asarray([4.0, 2.0, -4.0, -2.0])
HAMILTONIAN = np.diag(ENERGIES)
COUPLING_NAMES = ("IY", "XI", "XX", "XZ", "YI", "YX", "YZ", "ZI", "ZX", "ZZ")


def matrix_unit(row: int, column: int) -> np.ndarray:
    result = np.zeros((DIM, DIM), dtype=complex)
    result[row, column] = 1.0
    return result


def dissipator(jump: np.ndarray, operator: np.ndarray) -> np.ndarray:
    square = jump.conj().T @ jump
    return jump @ operator @ jump.conj().T - (square @ operator + operator @ square) / 2.0


def cross_dissipator(left: np.ndarray, right: np.ndarray,
                     operator: np.ndarray) -> np.ndarray:
    product = right.conj().T @ left
    return left @ operator @ right.conj().T - (product @ operator + operator @ product) / 2.0


def superoperator(action: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    columns = [action(matrix_unit(i, j)).reshape(-1)
               for i in range(DIM) for j in range(DIM)]
    return np.asarray(columns).T


def bohr_components() -> list[tuple[float, np.ndarray]]:
    differences = ENERGIES[:, None] - ENERGIES[None, :]
    result = []
    for name in COUPLING_NAMES:
        for frequency in np.unique(differences):
            jump = PAULIS[name] * (differences == frequency)
            if np.any(jump):
                result.append((float(frequency), jump))
    return result


def generator_from_pauli_couplings(eta: float, beta: float = 0.0) -> np.ndarray:
    """Split the ten Hermitian coupling matrices into their Bohr components."""
    if not 0.0 <= eta <= 1.0 or beta < 0.0:
        raise ValueError("Require 0 <= eta <= 1 and beta >= 0.")
    jumps: list[tuple[float, np.ndarray]] = []
    for frequency, jump in bohr_components():
        rate = float(np.exp(-beta * frequency / 2.0))
        if frequency == 0.0:
            jumps.append((rate, jump))
            continue
        jumps.append((eta * rate, jump))
        for row, column in zip(*np.nonzero(jump)):
            entry_jump = jump[row, column] * matrix_unit(row, column)
            jumps.append(((1.0 - eta) * rate, entry_jump))

    def action(operator: np.ndarray) -> np.ndarray:
        result = np.zeros_like(operator, dtype=complex)
        for rate, jump in jumps:
            result += rate * dissipator(jump, operator)
        return result

    return superoperator(action)


def generator_from_frequency_blocks(eta: float, beta: float = 0.0) -> np.ndarray:
    """Build the same model from the small, signed Kossakowski matrices."""
    blocks = [
        (2.0, (matrix_unit(0, 1), matrix_unit(3, 2)),
         2.0 * np.asarray([[1.0, -eta], [-eta, 1.0]])),
        (4.0, (matrix_unit(1, 3),), np.asarray([[4.0]])),
        (6.0, (matrix_unit(0, 3), matrix_unit(1, 2)),
         2.0 * np.asarray([[1.0, eta], [eta, 1.0]])),
        (8.0, (matrix_unit(0, 2),), np.asarray([[4.0]])),
    ]

    def action(operator: np.ndarray) -> np.ndarray:
        result = dissipator(PAULIS["ZI"], operator) + dissipator(PAULIS["ZZ"], operator)
        for frequency, positive_jumps, coefficients in blocks:
            for sign in (1.0, -1.0):
                jumps = positive_jumps if sign > 0 else tuple(j.conj().T for j in positive_jumps)
                rate = float(np.exp(-sign * beta * frequency / 2.0))
                for a, left in enumerate(jumps):
                    for b, right in enumerate(jumps):
                        result += rate * coefficients[a, b] * cross_dissipator(left, right, operator)
        return result

    return superoperator(action)


def apply(channel: np.ndarray, operator: np.ndarray) -> np.ndarray:
    return (channel @ operator.reshape(-1)).reshape(DIM, DIM)


def choi(channel: np.ndarray) -> np.ndarray:
    result = np.zeros((DIM * DIM, DIM * DIM), dtype=complex)
    for i in range(DIM):
        for j in range(DIM):
            basis = matrix_unit(i, j)
            result += np.kron(basis, apply(channel, basis)) / DIM
    return result


def partial_transpose(operator: np.ndarray, local_dim: int = DIM) -> np.ndarray:
    return operator.reshape(local_dim, local_dim, local_dim, local_dim).transpose(0, 3, 2, 1).reshape(operator.shape)


def breuer_hall_output(state: np.ndarray) -> np.ndarray:
    """The normalized-Choi trace-preserving reduction term is I_16/4."""
    unitary = np.kron(IDENTITY, PAULIS["YI"])
    return np.eye(DIM * DIM) / DIM - state - unitary @ partial_transpose(state) @ unitary.conj().T


def commuting_triples() -> list[tuple[str, str, str]]:
    names = [name for name in PAULIS if name != "II"]
    result = []
    for a, b, c in combinations(names, 3):
        A, B, C = (PAULIS[name] for name in (a, b, c))
        if np.allclose(A @ B, B @ A, atol=1e-14, rtol=0.0) and abs(abs(np.trace(A @ B @ C)) - DIM) < 1e-14:
            result.append((a, b, c))
    return result


def singleton_channel(name: str) -> np.ndarray:
    pauli = PAULIS[name]
    projectors = tuple((IDENTITY + sign * pauli) / 2.0 for sign in (1.0, -1.0))

    def action(operator: np.ndarray) -> np.ndarray:
        return sum(np.trace(projector @ operator) * projector / 2.0 for projector in projectors)

    return superoperator(action)


def triple_channel(names: tuple[str, str, str]) -> np.ndarray:
    left, right = (PAULIS[name] for name in names[:2])
    projectors = tuple((IDENTITY + s * left) @ (IDENTITY + t * right) / 4.0
                       for s in (1.0, -1.0) for t in (1.0, -1.0))

    def action(operator: np.ndarray) -> np.ndarray:
        return sum(np.trace(projector @ operator) * projector for projector in projectors)

    return superoperator(action)


def gibbs_state(beta: float) -> np.ndarray:
    probabilities = np.exp(-beta * ENERGIES)
    return np.diag(probabilities / probabilities.sum()).astype(complex)


def trace_preservation_error(channel: np.ndarray) -> float:
    trace_functional = IDENTITY.reshape(-1)
    return float(np.max(np.abs(trace_functional @ channel - trace_functional)))
