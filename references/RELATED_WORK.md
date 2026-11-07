# Related work and attribution

This account compares the calibrated local measurement problem with the primary sources inspected as of 7 November 2026. Citation keys match [references.bib](references.bib). Versioned preprint links identify the texts used for equation and theorem numbers.

## The exact problem being compared

Fix a nominal density operator $`\rho`$ of rank $`1\le r<d`$. The statistical tangent is the entire smooth manifold of exactly rank-$`r`$, trace-one states, including changes in eigenvalues, rotations within the support, and rotations from the support into the kernel. A single-copy POVM may depend on the nominal eigenbasis and rank. It is held fixed when derivatives are taken. Let $`J_\rho`$ be the symmetric logarithmic derivative (SLD) Fisher metric and $`I_M`$ the ordinary score Fisher information of the POVM.

The quantity studied here is

```math
c_*(\rho)
=\sup_M\inf_{0\ne X\in T_\rho\mathcal M_r}
\frac{I_M(X,X)}{J_\rho(X,X)}.
```

The result is $`c_*(\rho)=1/(2r)`$, for every positive occupied spectrum. The construction has $`r(2d-1)`$ outcomes and strictly positive nominal probabilities. Its weights do not require the values of the nonzero eigenvalues. The exact optimum is for the full tangent model; a restricted submodel can have a larger optimum while inheriting the same lower guarantee.

The support-rotation upper bound and the pure-state and support-pair measurement ingredients are known. The construction combines these ingredients to attain the bound while controlling the entire mixed-state rank-$`r`$ tangent. The contribution concerns $`2\le r<d`$; the pure-state endpoint is established prior work.

## Closest primary comparisons

| Source | Established result and location | Relation to the present problem |
|---|---|---|
| **[GM00] Gill–Massar** | A Fisher-information tradeoff for single-copy/separable estimation and an attainable characterization for qubits. | The information-budget method and the need to distinguish separable from collective measurements are inherited. The sharper support-rotation budget used here is explicitly available in [ZC26]. |
| **[Das25] Das et al.** | Theorem 2 gives the Nagaoka–Hayashi-to-Holevo ratio $`d+1`$ for full orthonormal-basis tomography at the maximally mixed state. Section 5.6 establishes attainability of the individual-measurement cost there, hence the same true individual-to-Holevo ratio. | The known-support instance with dimension $`r`$ gives the attributed $`r+1`$ collective-advantage example in [estimation](../science/estimation.md). It supplies context for the upper factor $`2r`$, not the full moving-support Fisher optimum. |
| **[Li16] Li et al.** | Pure-state Fisher-symmetric POVMs with $`I=J/2`$ and finite constructions using the minimal $`2d-1`$ outcomes. Their normalized-Fisher formulation also discusses mixed states. | Supplies the pure-state ingredient embedded in each occupied-vector-plus-kernel subspace. Their mixed-state purity criterion is not the same as maximizing the smallest normalized-Fisher eigenvalue. The present mixed-state POVM is generally anisotropic. |
| **[Pereira20] Pereira et al.** | Adaptive tomography using an estimated eigenbasis and real/imaginary pair-superposition bases. Equation (17) gives $`I\succeq J/[2d-1+(d\bmod2)]`$ in the full ambient dimension. | Supplies the calibrated support-pair ingredient and already establishes a dimension-dependent matrix guarantee. Applying that method only inside the support leaves support-to-kernel directions untreated; the shared-kernel assembly here controls those directions simultaneously. |
| **[ZC26] Zhou–Chen** | State-independent three-design readout. Theorem 4 and Eq. (73) provide $`I\succeq (d+2)J/[2(d+1)(1+r\kappa)]`$ for the relevant rank-$`r`$ model, with occupied-spectrum condition number $`\kappa`$. Equation (76) and Appendix D bound the normalized support-rotation Fisher trace by $`d-r`$. | This is the closest matrix comparison and the source of the exact converse $`c\le1/(2r)`$. The present construction supplies calibrated attainment for every occupied spectrum. Their Eq. (73) is already a matrix inequality; the difference is not merely scalar versus matrix control. Their state-independent apparatus and efficient randomized implementations use different resources. |
| **[Suzuki20] Suzuki** | Quantum experimental-design formulation, including A-, D-, and E-optimality; analytic solutions for qubit models. Section VII identifies further higher-dimensional design questions. | The objective here is standard E-optimality after choosing coordinates in which the SLD metric is the identity. The contribution is an exact higher-dimensional rank-deficient solution, not a new optimality criterion. |
| **[ZH18] Zhu–Hayashi** | Universally Fisher-symmetric measurements on pairs of copies for pure states, and special universal constructions for qubits; constraints on two-copy Fisher information. | Universal state-independent two-copy symmetry and calibrated single-copy E-optimality are different requirements. Exact isotropy of the whole Fisher matrix is not asserted here. |
| **[Saini25] Saini et al.** | For a supplied informationally complete POVM at a full-rank reference state, Theorem 1 and Eqs. (14)–(18) identify the best and worst normalized-Fisher directions through the frame spectrum. | The extremal-eigenvalue interpretation is established. Their theorem characterizes a fixed measurement and full-rank state; the present problem optimizes over measurements on the full fixed-rank tangent. |

The converse deserves explicit credit. Write $`I_{\rm cross}`$ and $`J_{\rm cross}`$ for restrictions to the $`2r(d-r)`$ real directions that rotate support into kernel. The known inequality gives

```math
\mathrm{Tr}(J_{\rm cross}^{-1}I_{\rm cross})\le d-r.
```

Consequently, domination by $`cJ_\rho`$ on every tangent requires $`2r(d-r)c\le d-r`$. The construction attains equality on this entire subspace and has nonnegative excess information on the remaining tangent directions. This explains both why the constant is optimal and why optimality does not require Fisher symmetry on every direction.

## What “all quadratic costs” means

After calibration at one nominal point, the same POVM satisfies $`I_M\succeq J_\rho/(2r)`$ independently of a later choice of positive semidefinite quadratic weight $`W`$. On identifiable coordinates, inverse order yields

```math
\mathrm{Tr}(W I_M^{-1})
\le 2r\mathrm{Tr}(WJ_\rho^{-1}).
```

This is a simultaneous approximation guarantee, not a claim that the POVM individually minimizes every weighted risk. It concerns an explicit attainable classical information matrix. Under the [local asymptotic minimax definitions](../science/estimation.md#individual-and-collective-cost-comparison), the score upper bound and Bayesian lower bound give $`C_{\mathrm{ind}}\le2rC_{\mathrm{SLD}}\le2rC_{\mathrm{coll}}`$. Since the Holevo bound also obeys $`C_H\ge C_{\mathrm{SLD}}`$, one has $`C_{\mathrm{ind}}\le2rC_H`$ without assuming $`C_H=C_{\mathrm{coll}}`$. Neither comparison determines its exact cost ratio or identifies a Nagaoka–Hayashi relaxation with the true optimized individual-measurement cost.

The pointwise statement assumes a calibrated nominal eigenbasis and rank. An unknown-state implementation requires localization before choosing this POVM. Although the measurement weights do not depend on the occupied eigenvalues, the localization accuracy and sample cost can depend on small occupied eigenvalues. The present theorem alone is neither a spectrum-uniform finite-sample calibration guarantee nor an unknown-rank procedure. Rank-changing directions and singular, direction-dependent definitions of information at zero-probability outcomes are outside its ordinary-score fixed-rank model.

## Adjacent tomography results

**Random measurement tomography.** Acharya–Kypraios–Guţă [AKG16] show Fisher concentration for certain rank-$`r`$ states using $`O(r\log d)`$ random bases. Acharya–Guţă [AG17] obtain spectrum-uniform Frobenius-risk scaling $`O(rd/N)`$ and explicitly distinguish it from infidelity behavior near the boundary. These results make low-rank statistical efficiency and Fisher methods established territory. Frobenius-risk control does not by itself imply a condition-independent lower bound relative to the singularly weighted SLD metric in every tangent direction.

**Global trace-norm tomography.** Nayak–Zhou [NZ26] prove, for sufficiently small error and constant success probability, the bounded-block sample complexity

```math
\Theta\!\left(\frac{dr}{\epsilon^2}
\max\left\{1,\frac r{\sqrt t}\right\}\right),
```

where one measurement may act on at most $`t`$ copies. Their lower bound allows classical adaptation and their matching upper bound is nonadaptive. Thus a broad statement that rank controls the advantage of collective tomography is already known. The present question is the exact local relative-SLD matrix optimum at each spectrum, with a calibrated single-copy apparatus, rather than a global trace-norm minimax sample rate.

**Task-specific local design.** Chen–Gong–Zhou [CGZ26] characterize high-precision shadow tomography through inverse-Fisher optimization and a two-stage coarse-tomography/local-estimation method. Their specified observable family and loss determine the statistical task. The present construction gives one explicit pointwise matrix guarantee for every tangent and quadratic cost. The general strategy of localization followed by measurement design is inherited.

**Purification protocols.** Zhou [ZhouPurification26], Theorem 2 and Eqs. (17)–(19), obtains Holevo-optimal or twice-SLD asymptotic covariance using random purification followed by individual measurements. The protocol first applies a global purification channel to all input copies, as stated immediately after Eq. (19). Its individual final readout therefore does not make the overall protocol a single-copy measurement on the original mixed-state samples. Its resource model does not contradict the $`1/(2r)`$ ceiling here.

## Relation to Quantum-Readout-Rank-Threshold

The internal comparator [RankThreshold26] was inspected at commit `b73e3b5eab18a11ddfe5e992b45412c9567a61af`, specifically its README, `science/model.md`, `science/interpretation.md`, and `references/RELATED_WORK.md`.

| Assumption | Quantum-Readout-Rank-Threshold | Calibrated-Quantum-Readout |
|---|---|---|
| Apparatus | State-independent fixed measurement on a bounded block of copies. | Single-copy POVM chosen from a nominal eigenbasis and rank. |
| Calibration between blocks | Learned calibration is explicitly excluded from that model. | Pointwise calibration is an allowed resource. |
| Question | Whether one fixed apparatus retains a spectrum-uniform fraction of QFI throughout the stated state family. | The best simultaneous local fraction after choosing a POVM for one nominal state. |
| Result being compared | Rank-two/rank-three threshold for bounded coherent blocks under its fixed-apparatus assumption. | Exact $`c_*(\rho)=1/(2r)`$ for every rank-deficient nominal state on its full fixed-rank tangent. |

The fixed-apparatus obstruction and the calibrated theorem have different quantifiers. The calibrated result does not invalidate the obstruction, and it does not supply the uniform localization cost that would connect their operational models.

Pinned sources: [model](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/b73e3b5eab18a11ddfe5e992b45412c9567a61af/science/model.md), [interpretation](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/b73e3b5eab18a11ddfe5e992b45412c9567a61af/science/interpretation.md), and [related work](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/b73e3b5eab18a11ddfe5e992b45412c9567a61af/references/RELATED_WORK.md).

## Older optimal-design coverage and access limitation

Zhu [Zhu14] treats informationally overcomplete measurements and optimal reconstruction, including matrix-valued error criteria. Its measurement comparison establishes the limits of fixed nonadaptive measurements for monotone-metric losses, while its reconstruction can depend on the nominal state. This does not provide the rank-deficient measurement optimization above. The paper explicitly develops material from Zhu's 2012 thesis [Zhu12], making it a relevant accessible partial source for that earlier line of work.

The cited NUS repository and PDF endpoints for [Zhu12] returned HTTP 403. The thesis was not inspected in full; [Zhu14] cannot substitute for all of its contents. The older mixed-state optimal-design and Fisher-symmetry comparison rests on accessible primary papers, including [Li16], [ZH18], [Zhu14], and [Suzuki20]. No exhaustive priority claim is made.

## Source and version register

### DDG20

R. Demkowicz-Dobrzański, W. Górecki, and M. Guţă, *Multi-parameter estimation beyond quantum Fisher information*, J. Phys. A: Math. Theor. **53**, 363001 (2020), [DOI](https://doi.org/10.1088/1751-8121/ab8ef3). The sole educational anchor is [2001.11742v2](https://arxiv.org/abs/2001.11742v2), 1 September 2020, with [open full text](https://arxiv.org/html/2001.11742v2). Section 2.1, Eq. (9), supplies the classical local score-estimator foundation. Section 4.6.3 explicitly limits its general QLAN treatment to full-rank states; the project's fixed-rank pilot argument is supplied separately in [estimation](../science/estimation.md#learning-the-calibration-with-a-pilot-sample).

### GM00

R. D. Gill and S. Massar, *State estimation for large ensembles*, Phys. Rev. A **61**, 042312 (2000), [DOI](https://doi.org/10.1103/PhysRevA.61.042312). [quant-ph/9902063v2](https://arxiv.org/abs/quant-ph/9902063v2), 26 October 1999. Publication year follows the APS record.

### Das25

A. Das, L. O. Conlon, J. Suzuki, S. K. Yung, P. K. Lam, and S. M. Assad, *Holevo Cramér-Rao bound: How close can we get without entangling measurements?*, Quantum **9**, 1867 (2025), [journal full text](https://quantum-journal.org/papers/q-2025-09-30-1867/), [DOI](https://doi.org/10.22331/q-2025-09-30-1867). [2405.09622v2](https://arxiv.org/pdf/2405.09622v2), 25 September 2025; Theorem 2, Section 5.6, and Appendix I distinguish the relaxed and attainable costs.

### Li16

N. Li, C. Ferrie, J. A. Gross, A. Kalev, and C. M. Caves, *Fisher-Symmetric Informationally Complete Measurements for Pure States*, Phys. Rev. Lett. **116**, 180402 (2016), [DOI](https://doi.org/10.1103/PhysRevLett.116.180402). [1507.06904v2](https://arxiv.org/pdf/1507.06904v2), 16 February 2016; finite pure-state construction and normalized-Fisher criterion.

### Pereira20

L. Pereira, D. Martínez, G. Cañas, E. S. Gómez, S. P. Walborn, G. Lima, and A. Delgado, *High-accuracy adaptive quantum tomography for high-dimensional quantum systems*. [2009.04791v1](https://arxiv.org/pdf/2009.04791v1), 10 September 2020, Eq. (17). Cited as a preprint.

### ZC26

S. Zhou and S. Chen, *Randomized Measurements for Multiparameter Quantum Metrology*, PRX Quantum **7**, 010314 (2026), [DOI](https://doi.org/10.1103/s27y-gbrp). [2502.03536v3](https://arxiv.org/html/2502.03536v3), 15 January 2026; Theorem 4, Eqs. (73), (76), Appendix D.

### Suzuki20

J. Suzuki, *Quantum-state estimation problem via optimal design of experiments*, Int. J. Quantum Inf. **19**(08), 2040007 (2021), [DOI](https://doi.org/10.1142/S0219749920400079). [2012.11949v1](https://arxiv.org/pdf/2012.11949v1), 22 December 2020. Key reflects preprint year; journal publication is 2021.

### ZH18

H. Zhu and M. Hayashi, *Universally Fisher-Symmetric Informationally Complete Measurements*, Phys. Rev. Lett. **120**, 030404 (2018), [DOI](https://doi.org/10.1103/PhysRevLett.120.030404). [1709.06112v2](https://arxiv.org/pdf/1709.06112v2), 24 January 2018, including supplement.

### Saini25

R. Saini, J. Kiukas, D. Burgarth, and A. Gilchrist, *Characterizing Fisher information of quantum measurement*. [2512.15428v1](https://arxiv.org/html/2512.15428v1), 17 December 2025, Theorem 1. The arXiv record also lists related DOI [10.1103/9xzl-1xkp](https://doi.org/10.1103/9xzl-1xkp); the inspected text is the preprint.

### AKG16

A. Acharya, T. Kypraios, and M. Guţă, *Statistically efficient tomography of low rank states with incomplete measurements*, New J. Phys. **18**, 043018 (2016), [DOI](https://doi.org/10.1088/1367-2630/18/4/043018). [1510.03229v2](https://arxiv.org/pdf/1510.03229v2), 23 October 2015.

### AG17

A. Acharya and M. Guţă, *Statistical analysis of compressive low rank tomography with random measurements*, J. Phys. A: Math. Theor. **50**, 195301 (2017), [DOI](https://doi.org/10.1088/1751-8121/aa682e). [1609.03758v1](https://arxiv.org/pdf/1609.03758v1), 13 September 2016; preprint title uses “low rank tomography with compressive random measurements.”

### NZ26

A. Nayak and X. Zhou, *Optimal Low-Rank Quantum State Tomography with Bounded-Sample Joint Measurements*. [2609.10514v2](https://arxiv.org/pdf/2609.10514v2), 5 October 2026.

### CGZ26

S. Chen, W. Gong, and S. Zhou, *Instance-optimal high-precision shadow tomography with few-copy measurements: A metrological approach*, Proceedings of the 39th Conference on Learning Theory, PMLR **336**, 1115–1185 (2026). [2602.04952v2](https://arxiv.org/pdf/2602.04952v2), 27 September 2026. Conference metadata follows the primary arXiv record.

### ZhouPurification26

S. Zhou, *Quantum metrology of mixed states via purification*. [2605.03975v2](https://arxiv.org/html/2605.03975v2), 10 August 2026, Theorem 2 and Eqs. (17)–(19).

### Zhu14

H. Zhu, *Quantum state estimation with informationally overcomplete measurements*, Phys. Rev. A **90**, 012115 (2014), [DOI](https://doi.org/10.1103/PhysRevA.90.012115). [1404.3453v2](https://arxiv.org/pdf/1404.3453v2), 5 August 2014, especially Sections II–III and V.

### Zhu12

H. Zhu, *Quantum State Estimation and Symmetric Informationally Complete POMs*, PhD thesis, National University of Singapore (2012). [NUS record](https://scholarbank.nus.edu.sg/handle/10635/35247). Bibliographic provenance from later primary papers; full text inaccessible during this audit.

### RankThreshold26

GoGoKo699, *Quantum-Readout-Rank-Threshold*, research repository. [Commit b73e3b5eab18a11ddfe5e992b45412c9567a61af](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/tree/b73e3b5eab18a11ddfe5e992b45412c9567a61af).
