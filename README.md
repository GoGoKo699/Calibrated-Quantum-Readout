# Calibrated Quantum Readout

How much quantum Fisher information can one measurement preserve simultaneously in every local direction of a mixed state? For a state of exact rank $`r\lt d`$, an eigenbasis-calibrated measurement can retain the fraction $`1/(2r)`$ in every direction of the full fixed-rank model. No single-copy measurement can guarantee a larger fraction.

The result depends on the occupied rank, even when the positive eigenvalues are very unequal and the empty subspace is large. Calibration supplies the nominal eigenbasis. It changes the permitted measurement design and has a statistical cost of its own.

## Exact result

Let $`\rho`$ have rank $`2\le r\lt d`$, and let $`\mathcal T_\rho`$ be the full real tangent space of states that remain exactly rank $`r`$. For a POVM $`M`$ chosen at $`\rho`$ and held fixed during differentiation, write $`I_M`$ for ordinary score Fisher information and $`J_\rho`$ for symmetric logarithmic derivative quantum Fisher information. Then

```math
\boxed{
\sup_M\ \inf_{0\ne X\in\mathcal T_\rho}
\frac{I_M(X,X)}{J_\rho(X,X)}
=\frac1{2r}.
}
```

The [explicit measurement](science/construction.md) has **$`2rd-r`$ positive-probability outcomes** and acts on one copy. Its settings depend on the rank and an eigenbasis, but not on the occupied eigenvalue values, a chosen parameter submodel, or a loss matrix. The exact identity

```math
I_M(X)
=\frac{J_\rho(X)}{2r}
+\frac1{2r}\sum_{j=1}^{r}\frac{X_{jj}^2}{\lambda_j}
+\frac1r\sum_{j\lt \ell\le r}
\frac{(X_{jj}+X_{\ell\ell})^2}{\lambda_j+\lambda_\ell}
```

exhibits the guarantee and its equality directions. The [matching converse](science/optimality.md) is the established support-rotation information budget of Zhou and Chen. The construction combines pure-state Fisher-symmetric measurements with occupied-pair measurements; the [attribution and comparison](references/RELATED_WORK.md) identify the inherited ingredients and the intermediate-rank attainment addressed here.

## Paid calibration and two-copy readout

[Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold) is the complementary sister project: it studies fixed readout without a supplied eigenbasis. The [paid-calibration account](science/paid-calibration.md) puts both experiments on one fully counted information budget, starting with $`\rho_b=\mathrm{diag}(1-b,b,0)`$.

Strong-eigenvector error can leak population into rare outcomes; a separate small weak-eigenvector error has a different, uniformly robust limit. For a pilot record $`Y`$ from $`m`$ copies and a subsequent apparatus $`M_Y`$,

```math
I_{\rm total}=I_Y+(N-m)\mathbb E_Y[I_{M_Y}].
```

All pilot outcomes and settings count. The inherited support budget bounds the full-model worst fraction of every classically adaptive one-copy protocol by $`1/4`$. The sister project's [exact continuous-Haar pair readout](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/c4356840cb334f93b3e8367870b79fee45f937c2/science/haar-pair-readout.md) has fraction strictly above $`1/4`$ for all sufficiently small positive $`b`$, tending to $`1/4`$ as $`b\downarrow0`$. This is a local full-model information separation. The continuous-Haar calculation does not set the finite Clifford constant or establish finite-sample risk dominance.

The exact paid binomial pilot and geometric calibration lower bound are developed here; the exact Haar pair calculation has its authoritative home in the sister repository. No universal calibration-budget crossover is assumed or established.

## Scientific route

Start with the [scientific overview](science/README.md), or go directly to the relevant question.

| Question | Authoritative account |
| --- | --- |
| What is optimized, and which state variations are allowed? | [Model and theorem](science/model.md) |
| What are the effects, and why do they retain this information? | [Construction and exact Fisher identity](science/construction.md) |
| Why can no single-copy POVM do better in every direction? | [Optimality](science/optimality.md) |
| What does this mean in the smallest mixed-state example? | [Rank-two qutrit](science/examples.md) |
| How does the matrix bound become an estimation guarantee? | [Score estimation, pilot calibration, and costs](science/estimation.md) |
| What calibration and hardware resources are assumed? | [Resources and sensitivity to basis error](science/resources.md) |
| What changes near a shrinking occupied eigenvalue? | [Complete-record information, strong/weak errors, and paid calibration](science/paid-calibration.md) |
| Which earlier results are used or compared? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| How can the finite-dimensional calculations be reproduced? | [Verification guide](verification/README.md) |

The [LLM reading guide](llms.txt) maps the same questions to source files.

## Learning route

The selected educational anchor is Demkowicz-Dobrzański, Górecki, and Guţă, *Multi-parameter estimation beyond Quantum Fisher Information*, [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2), published in J. Phys. A **53**, 363001 (2020).

Start with the [source-to-project bridge](learning/README.md). The [anchor guide](learning/ANCHOR.md) identifies the relevant sections, translates notation, and records which arguments are supplied by this project. The [30-milestone map](learning/MILESTONES.md) develops the background in M01–M12 and the construction, optimality, and operational meaning in M13–M30. Each phase ends by connecting its parts into the complete problem or result.

## Estimation and scope

The matrix inequality pulls back to every identifiable smooth submodel of the fixed-rank manifold. A locally unbiased score estimator at the calibrated point has covariance $`I_M^{-1}/n\preceq 2rJ_\rho^{-1}/n`$. Under explicit fixed-state local regularity and localization conditions, a pilot using a vanishing fraction of the copies supplies an asymptotic implementation; [estimation](science/estimation.md) gives the risk statement, including nuisance parameters and degenerate positive eigenvalues.

The exact optimum concerns the worst simultaneous **Fisher-information fraction**. The resulting factor $`2r`$ for individual versus collective estimation costs is an upper bound; the sharp collective-cost ratio is a separate problem. Restricted submodels can also have better Fisher optima.

The rank is exactly constant in the local model. The guarantee does not provide a uniform finite-sample cost for learning an arbitrarily small occupied eigenvalue or its eigenspace. The [calibration example](science/resources.md#calibration-sensitivity-for-a-weakly-occupied-direction) quantifies how strong-state leakage can obscure a weakly occupied direction. Arbitrary single-copy POVM control is allowed; an efficient many-qubit circuit implementation is not assumed.

## Reproduce the calculations

With Python 3.12 and the pinned dependencies:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_readout.py
python verification/check_paid_calibration.py
python verification/plot_calibration.py
```

The checks compare direct Born-rule probabilities and derivatives with the full Fisher identity, the support-rotation trace budget, the qutrit matrices, exact score-estimator moments, the calibration formulas, and an explicitly enumerated complete adaptive record. The [verification guide](verification/README.md) describes the cases, tolerances, and limits of these numerical checks. The proofs establish the general result.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
