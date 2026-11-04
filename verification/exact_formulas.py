"""Analytical formulas proved in science/exact_thresholds.md.

The verification program compares these expressions with a separately constructed
Lindblad generator. This module does not construct that generator.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.optimize import brentq


PAULI_NAMES = tuple(a + b for a in "IXYZ" for b in "IXYZ")
GAMMAS = ("IZ", "IX", "XY", "YY", "ZY")
V_MODES = ("IY", "XX", "YX", "ZX")
B_MODES = ("XI", "XZ", "YI", "YZ", "ZI", "ZZ")


def parameters(eta: float, time: float) -> dict[str, float]:
    if not 0.0 <= eta <= 1.0 or time < 0.0:
        raise ValueError("Require 0 <= eta <= 1 and time >= 0.")
    return {
        "r": math.exp(-8.0 * time),
        "u": math.exp(-(10.0 - 2.0 * eta) * time),
        "v": math.exp(-(10.0 + 2.0 * eta) * time),
        "b": math.exp(-12.0 * time),
    }


def multipliers(eta: float, time: float) -> dict[str, float]:
    q = parameters(eta, time)
    result = {"II": 1.0, "IZ": q["r"]}
    result.update({name: q["u"] for name in GAMMAS[1:]})
    result.update({name: q["v"] for name in V_MODES})
    result.update({name: q["b"] for name in B_MODES})
    return result


def thresholds(eta: float) -> tuple[float, float]:
    if not 0.0 <= eta <= 1.0:
        raise ValueError("Require 0 <= eta <= 1.")

    def ppt_equation(time: float) -> float:
        q = parameters(eta, time)
        return q["r"] + 2.0 * q["u"] + 2.0 * q["v"] - 1.0

    def eb_equation(time: float) -> float:
        q = parameters(eta, time)
        return q["r"] + 4.0 * q["u"] - 1.0

    options = {"xtol": 5e-15, "rtol": 1e-14}
    return (
        float(brentq(ppt_equation, 0.0, 1.0, **options)),
        float(brentq(eb_equation, 0.0, 1.0, **options)),
    )


def ppt_spectrum(eta: float, time: float) -> np.ndarray:
    q = parameters(eta, time)
    r, u, v, b = (q[name] for name in ("r", "u", "v", "b"))
    eigenvalues = (
        [1 + r + 2 * b] * 6
        + [1 - r + 2 * u + 2 * v] * 4
        + [1 - r - 2 * u - 2 * v] * 4
        + [1 + r - 6 * b + 4 * (u - v), 1 + r - 6 * b - 4 * (u - v)]
    )
    return np.sort(np.asarray(eigenvalues, dtype=float) / 16.0)


def projected_state(eta: float, time: float) -> tuple[float, np.ndarray]:
    q = parameters(eta, time)
    r, u, v, b = (q[name] for name in ("r", "u", "v", "b"))
    a, d, c = 1.0 + r + 2.0 * b, 1.0 - r, 2.0 * (u + v)
    state = np.asarray([[a, 0, 0, c], [0, d, 0, 0],
                        [0, 0, d, 0], [c, 0, 0, a]], dtype=complex)
    return (1.0 + b) / 4.0, state / (4.0 * (1.0 + b))


def small_eta_coefficients() -> dict[str, float]:
    time_zero, _ = thresholds(0.0)
    s_zero = math.exp(-10.0 * time_zero)
    return {
        "t_zero": time_zero,
        "s_zero": s_zero,
        "ppt_quadratic_coefficient": time_zero**2 * s_zero / (1.0 + s_zero),
        "eb_linear_coefficient": time_zero * s_zero / (1.0 + s_zero),
        "width_linear_coefficient": time_zero * s_zero / (1.0 + s_zero),
    }


def finite_beta_certificate(beta: float = 1e-4) -> dict[str, float]:
    time = math.log(25.0 / 12.0) / 4.0
    delta = 52.0 * time * math.expm1(4.0 * beta)
    return {
        "beta": beta,
        "eta": 1.0,
        "time": time,
        "diamond_distance_upper_bound": delta,
        "beta_zero_ppt_margin": 1369.0 / 250000.0,
        "beta_zero_bh_negative_margin": 19.0 / 1000.0,
        "certified_ppt_margin": 1369.0 / 250000.0 - delta,
        "certified_bh_negative_margin": 19.0 / 1000.0 - 2.0 * delta,
    }
