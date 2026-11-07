"""Finite calibrated readout and direct Fisher calculations.

The input basis is ordered as occupied eigenvectors, then kernel vectors.
Effects are fixed throughout all derivative calculations.
"""

import numpy as np


def calibrated_effects(d, r):
    """Return the 2*r*d-r positive rank-one effects in the standard basis."""
    if not 1 <= r <= d:
        raise ValueError("Require 1 <= r <= d")
    k, n = d - r, 2 * (d - r) + 1
    effects = []
    for j in range(r):
        for ell in range(j + 1, r):
            for phase in (1, -1, 1j, -1j):
                vector = np.zeros(d, complex)
                vector[j], vector[ell] = 1 / np.sqrt(2), phase / np.sqrt(2)
                effects.append(np.outer(vector, vector.conj()) / (2 * r))
    for j in range(r):
        for t in range(n):
            vector = np.zeros(d, complex)
            vector[j] = 1
            vector[r:] = np.exp(2j * np.pi * np.arange(1, k + 1) * t / n)
            effects.append(np.outer(vector, vector.conj()) / (r * n))
    return np.asarray(effects)


def tangent_basis(d, r):
    """A real basis of trace-zero Hermitian X with Q X Q=0.

    Off-diagonal basis elements have Hilbert--Schmidt norm one.
    The returned indices select the support--kernel subspace.
    """
    tangents, cross = [], []
    for j in range(r - 1):
        x = np.zeros((d, d), complex)
        x[j, j], x[r - 1, r - 1] = 1, -1
        tangents.append(x)
    for j in range(r):
        for ell in range(j + 1, d):
            for phase in (1, 1j):
                x = np.zeros((d, d), complex)
                x[j, ell], x[ell, j] = phase / np.sqrt(2), phase.conjugate() / np.sqrt(2)
                if ell >= r:
                    cross.append(len(tangents))
                tangents.append(x)
    return np.asarray(tangents), np.asarray(cross, dtype=int)


def probability_derivatives(effects, rho, tangents):
    probabilities = np.einsum("zij,ji->z", effects, rho).real
    derivatives = np.einsum("zij,bji->zb", effects, tangents).real
    return probabilities, derivatives


def classical_fisher(effects, rho, tangents):
    """Ordinary score FI: zero-probability outcomes contribute zero."""
    probabilities, derivatives = probability_derivatives(effects, rho, tangents)
    if probabilities.min() < -1e-13:
        raise ValueError("Negative probability")
    active = probabilities > 0
    if np.any(np.abs(derivatives[~active]) > 1e-12):
        raise ValueError("Nonzero first derivative at a zero-probability outcome")
    dp, p = derivatives[active], probabilities[active]
    return dp.T @ (dp / p[:, None])


def quantum_fisher(eigenvalues, tangents):
    """SLD FI for a diagonal state, from the spectral SLD formula."""
    denominator = eigenvalues[:, None] + eigenvalues[None, :]
    inverse = np.divide(2, denominator, out=np.zeros_like(denominator), where=denominator > 0)
    return np.einsum("aij,bji,ij->ab", tangents, tangents, inverse).real


def diagonal_surplus(lam, tangents):
    r = len(lam)
    result = np.zeros((len(tangents), len(tangents)))
    for j in range(r):
        diagonal = tangents[:, j, j].real
        result += np.outer(diagonal, diagonal) / (2 * r * lam[j])
        for ell in range(j + 1, r):
            pair = (tangents[:, j, j] + tangents[:, ell, ell]).real
            result += np.outer(pair, pair) / (r * (lam[j] + lam[ell]))
    return result


def normalized_fisher(classical, quantum):
    """Cholesky congruence with the same eigenvalues as J^-1/2 I J^-1/2."""
    factor = np.linalg.cholesky(quantum)
    left = np.linalg.solve(factor, classical)
    result = np.linalg.solve(factor, left.T).T
    return (result + result.T) / 2


def calibration_fraction(epsilon, strong_weight, delta, r):
    """Exact weak-support rotation fraction in science/resources.md."""
    c2, s2 = np.cos(delta) ** 2, np.sin(delta) ** 2
    return epsilon / (2 * r) * (c2 / (epsilon + strong_weight * s2)
                                + s2 / (epsilon + strong_weight * c2))
