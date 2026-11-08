# From a calibrated source to an optimal common readout

Consider a three-level source with orthonormal states $`|e_1\rangle,|e_2\rangle,|e_3\rangle`$ and nominal density matrix

```math
\rho_0=\tfrac12|e_1\rangle\langle e_1|
      +\tfrac12|e_2\rangle\langle e_2|.
```

The first two levels are occupied; the third is empty. A new specimen can differ slightly from this calibration. Its populations can change, coherences can appear, and its occupied subspace can rotate toward the third level. The readout must respond to all these possibilities using one fixed measurement on each specimen.

This project constructs such a measurement and determines its best possible worst-direction sensitivity. For a state of rank $`r\lt d`$, the optimal retained fraction of SLD quantum Fisher information is exactly $`1/(2r)`$. The qutrit above has $`r=2`$, so its sharp fraction is $`1/4`$. The statement concerns the complete smooth rank-two model, including motion of the occupied subspace. [The model](../science/model.md) fixes these quantifiers.

The [thirty-milestone map](MILESTONES.md) organizes the background and the construction into 12 preliminary and 18 narrative milestones. The sole educational anchor, [DDG20 v2](ANCHOR.md), supplies the estimation framework. This bridge develops the qutrit experiment first, then connects it to the general theorem and its statistical meaning.

## What can change while rank stays two?

A tangent $`X`$ records the first derivative of a physical state curve. It is Hermitian and trace zero. For this qutrit, its diagonal entries are $`a,-a,0`$, and its three upper off-diagonal entries are $`X_{j\ell}=x_{j\ell}+iy_{j\ell}`$. These are seven independent real coordinates:

| Change | Coordinates | Number of directions |
| --- | --- | ---: |
| Redistribution within the occupied support | $`a`$ | 1 |
| Coherence between the occupied levels | $`x_{12},y_{12}`$ | 2 |
| Motion of the support toward the empty level | $`x_{13},y_{13},x_{23},y_{23}`$ | 4 |

The zero third diagonal entry is a first-order condition. Replacing $`|e_1\rangle`$ by $`\cos\phi|e_1\rangle+\sin\phi|e_3\rangle`$ preserves rank two while creating a support-to-kernel coherence at first order and an occupation of the third level at second order. A straight line $`\rho_0+tX`$ need not remain positive; the physical curve can bend.

In general, if $`Q`$ projects onto the kernel, the allowed tangent condition is $`QXQ=0`$. It permits arbitrary motion between support and kernel. [M01–M12](MILESTONES.md#phase-i-background-and-preliminaries) develop this geometry together with measurement probabilities, local statistics, and the optimization criterion.

## Ten effects make one measurement

A positive-operator-valued measure, or POVM, is a collection of positive effects $`E_z`$ summing to the identity. Its outcome probability is $`p_z=\mathrm{tr}(\rho E_z)`$. One measured specimen produces one label $`z`$. The qutrit construction has ten possible labels, assembled from two families.

The four support-pair effects are

```math
G_\zeta=\frac14|\psi_\zeta\rangle\langle\psi_\zeta|,
\qquad
|\psi_\zeta\rangle=\frac{|e_1\rangle+\zeta|e_2\rangle}{\sqrt2},
\qquad \zeta\in\{1,-1,i,-i\}.
```

The relative phases distinguish the real and imaginary occupied coherence. Writing $`P_j=|e_j\rangle\langle e_j|`$, the four effects sum to $`(P_1+P_2)/2`$. Each has nominal probability $`1/8`$.

The other six effects connect each occupied level to the kernel. With $`\omega=e^{2\pi i/3}`$, define

```math
F_{jt}=\frac16|v_{jt}\rangle\langle v_{jt}|,
\qquad |v_{jt}\rangle=|e_j\rangle+\omega^t|e_3\rangle,
\qquad j=1,2,\quad t=0,1,2.
```

The vectors $`v_{jt}`$ are unnormalized. The factor $`1/6`$ is part of the effect definition and must be kept when computing probabilities. Since $`1+\omega+\omega^2=0`$, each three-effect family sums to $`(P_j+P_3)/2`$. Adding both families to the support-pair effects gives

```math
\sum_\zeta G_\zeta+\sum_{j,t}F_{jt}
=\tfrac12(P_1+P_2)
 +\tfrac12(P_1+P_3)+\tfrac12(P_2+P_3)
=\mathbb I.
```

Each Fourier effect has probability $`1/12`$ at $`\rho_0`$, so the full record is normalized: $`4(1/8)+6(1/12)=1`$. Every outcome has positive probability. There is no discarded outcome or postselection. [M13–M17](MILESTONES.md#m13) connect these effects to the general construction and its resource count.

## How much information survives?

With the apparatus fixed, the probability derivative in direction $`X`$ is $`\mathrm{tr}(XE_z)`$. Classical Fisher information measures the squared relative response of the outcome distribution:

```math
I_M(X,X)=\sum_z
\frac{[\mathrm{tr}(XE_z)]^2}{p_z}.
```

The quantum comparison scale is the symmetric logarithmic derivative, or SLD, metric. Solve $`2X=\rho L_X+L_X\rho`$ and set $`J_\rho(X,X)=\mathrm{tr}(\rho L_X^2)`$. This is the information available when a measurement can be optimized for one specified direction. A common measurement can face incompatible requirements from different directions. DDG20 [Sections 2.1–2.2](https://arxiv.org/html/2001.11742v2#S2.SS1) establish this statistical framework; the [notation translation](ANCHOR.md#notation-translation) identifies the symbols used here.

For the ten-effect qutrit POVM, both matrices are diagonal in the seven coordinates above:

| Coordinate | Quantum information $`J`$ | Readout information $`I_M`$ | Retained fraction |
| --- | ---: | ---: | ---: |
| $`a`$ | 4 | 2 | $`1/2`$ |
| $`x_{12},y_{12}`$, each | 4 | 1 | $`1/4`$ |
| $`x_{13},y_{13},x_{23},y_{23}`$, each | 8 | 2 | $`1/4`$ |

For example, a unit change of $`x_{12}`$ changes the two real-phase pair probabilities with derivatives $`+1/4`$ and $`-1/4`$. The other eight derivatives vanish. Thus its classical information is $`2(1/4)^2/(1/8)=1`$, compared with quantum information 4.

The smallest retained fraction is $`1/4`$. More generally, $`I_M\succeq cJ`$ means that this comparison holds for every tangent, including combinations of coordinates. It is equivalent to a smallest eigenvalue of at least $`c`$ for $`J^{-1/2}I_MJ^{-1/2}`$. The normalization matters: raw Fisher entries depend on parameter units. This measurement is optimal for the least favorable normalized direction even though its population direction retains more information. [M18–M20](MILESTONES.md#m18) and the [full qutrit example](../science/examples.md) develop the calculation.

## Why rank sets the sharp fraction

For general rank $`r`$, let $`P`$ project onto the occupied support and let $`k=d-r`$ be the kernel dimension. Four phase-sensitive effects are assigned to every occupied pair. For each occupied vector, another family coherently combines that vector with all kernel vectors using $`N=2k+1`$ equally spaced Fourier phases.

The normalization makes all Fourier families sum to $`P/r+Q`$. All support-pair effects sum to $`(r-1)P/r`$. Their union is therefore complete. Fourier cancellation also removes cross terms in the score calculation. The resulting exact identity has the form

```math
I_{M_\rho}(X,X)
=\frac{J_\rho(X,X)}{2r}
 +\text{nonnegative population terms}.
```

The [full formula](../science/construction.md#exact-fisher-identity) identifies those terms explicitly. They vanish whenever the occupied diagonal of $`X`$ vanishes, including every support-rotation tangent. The measurement coefficients require the rank and calibrated eigenbasis, but no occupied eigenvalue values. The construction has $`2rd-r`$ outcomes with positive nominal probabilities for every positive occupied spectrum, including degeneracies.

The matching obstruction comes from support motion. There are $`2r(d-r)`$ real support-rotation directions. A refinement of the Gill–Massar bound limits their total normalized Fisher information to $`d-r`$. Consequently a measurement preserving a fraction $`c`$ in all directions must obey

```math
2r(d-r)c\le d-r,
\qquad c\le\frac1{2r}.
```

The converse is inherited from [ZC26](../references/RELATED_WORK.md#zc26). The project assembles the known pure-state Fisher-symmetric ingredient [Li16](../references/RELATED_WORK.md#li16) and support-pair ingredient [Pereira20](../references/RELATED_WORK.md#pereira20) into a finite measurement attaining this bound on the entire mixed-state tangent. The [optimality proof](../science/optimality.md) also covers continuous outcome spaces and states its ordinary-score convention at zero-probability outcomes.

The tangent model is essential. If the qutrit's occupied two-dimensional support is known to remain fixed, the four support-motion coordinates disappear. At the maximally mixed qubit state the optimal fraction is then $`1/3`$. Allowing unknown motion into an empty level changes the problem. The proof of $`1/(2r)`$ requires $`r\lt d`$ and makes no corresponding formula claim for general full-rank states. These distinctions complete [M21–M24](MILESTONES.md#m21).

## From information to estimation

For an identifiable local parameter $`\theta`$, suppose the calibrated point is $`\theta_0`$. Define the score vector $`s_z=\nabla_\theta\log p_z|_{\theta_0}`$ and Fisher matrix $`I_0`$. On $`n`$ independently measured specimens, the estimator

```math
\widehat\theta_n
=\theta_0+I_0^{-1}\frac1n\sum_{i=1}^n s_{Z_i}
```

has mean $`\theta_0`$, first derivative of its mean equal to the identity, and covariance $`I_0^{-1}/n`$ at the nominal point. These are local unbiasedness statements. This score-estimator construction is the one in DDG20 [Section 2.1, Eq. (9)](https://arxiv.org/html/2001.11742v2#S2.SS1).

Matrix inversion converts the measurement guarantee into

```math
I_0^{-1}\preceq2rJ_0^{-1},
\qquad
\mathrm{tr}(WI_0^{-1})
\le2r\mathrm{tr}(WJ_0^{-1})
```

for every positive semidefinite loss weight $`W`$. One measurement therefore supplies a simultaneous approximation guarantee for all quadratic costs. A cost chosen in advance can admit a better specialized measurement. Nuisance parameters must remain in the full information matrix before the relevant inverse block is taken; [M25](MILESTONES.md#m25) and [estimation](../science/estimation.md) make this distinction explicit.

The comparison with collective measurements uses local asymptotic minimax risk over $`\theta_0+h/\sqrt n`$, with bounded $`h`$ before taking the large-neighborhood limit. The individual strategy above supplies an upper bound. A Bayesian Cramér–Rao argument supplies the collective lower bound, allowing biased estimators. Together they give $`C_{\mathrm{ind}}\le2rC_{\mathrm{coll}}`$ under the stated local model. This upper factor need not be the sharp cost ratio: the SLD information benchmark need not be jointly attainable. [M28](MILESTONES.md#m28) separates these optimizations.

## What calibration costs

If the operating point is unknown, a pilot sample can estimate it before the remaining specimens are measured. The project's [pilot argument](../science/estimation.md#learning-the-calibration-with-a-pilot-sample) uses $`n_0=\lceil n^\alpha\rceil`$ copies with $`1/2\lt \alpha\lt 1`$. Under its smoothness, identifiability, localization, and moment conditions, the pilot fraction vanishes while its error is small enough for a subsequent score correction.

The dimension, rank, and true state are fixed in this argument. The occupied eigenvalues have a positive lower bound on the chosen local region. No gap between occupied eigenvalues is required: after each pilot result, any eigenbasis within a degenerate occupied block can be selected and held fixed. The argument never differentiates that basis or assumes it converges. DDG20's general full-rank asymptotic theory does not supply this rank-deficient result; the [anchor scope note](ANCHOR.md#scope-of-the-bridge) records the boundary.

Small occupations still matter for finite calibration accuracy. In the [strong-error example](../science/paid-calibration.md#strong-eigenvector-error-and-nuisance-coupling), an angular error $`\delta`$ moves population of order $`\delta^2`$ from the strong level into outcomes intended to resolve weak occupation $`b`$. A separate [weak-eigenvector error](../science/paid-calibration.md#weak-eigenvector-error-has-a-different-limit) introduces no strong background. Its small-angle full-matrix fraction remains positive as $`b\downarrow0`$, although its two quadratures differ. Thus “basis error” is not one spectrum-dependent penalty.

## Pay for the record, then compare measurement classes

A pilot supplies both a random estimate and an observed record. Conditional on its record $`Y`$, the selected apparatus $`M_Y`$ is fixed. Scores of later independent specimens have conditional mean zero, giving

```math
I_{\rm total}=I_Y+(N-m)\mathbb E_Y[I_{M_Y}].
```

This is a matrix identity, including nuisance coordinates. Averaging the conditional FI is different from evaluating it at the mean squared error of the estimated basis. [M26–M28](MILESTONES.md#m26) connect this accounting to the [exact paid binomial pilot](../science/paid-calibration.md#an-exact-paid-real-angle-pilot). Even a tie in the pilot counts can matter near a rare outcome; a Gaussian approximation can miss such an atom.

The [geometric calibration argument](../science/paid-calibration.md#geometric-calibration-requirements) uses distinguishability of two states. Uniform strong-angle accuracy $`o(\sqrt b)`$ or weak-angle consistency $`o(1)`$ requires $`mb\to\infty`$. This constrains a named task of recovering a basis. It does not prove that every useful readout must recover that basis or that total FI has a universal threshold at $`mb\sim1`$.

Finally, apply the one-copy support budget to every realized conditional apparatus. Summing over the complete transcript leaves the full-model one-copy fraction at most $`1/4`$, however the pilot is chosen using separate fresh copies. The complementary [Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold) changes the measurement class by coupling pairs. Its [continuous-Haar parity-pair readout](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/blob/main/science/haar-pair-readout.md) has a full-model minimum fraction strictly above $`1/4`$ for sufficiently small positive $`b`$, approaching $`1/4`$ as $`b\downarrow0`$. All input copies and both parity branches count. The exact Haar result does not determine the finite Clifford constant or establish finite-sample risk dominance.

[M29–M30](MILESTONES.md#m29) assemble these distinctions: the sharp calibrated construction, the conditional adaptive ceiling, paid geometric calibration, and coherent pair readout answer different questions in the same local statistical framework. The [attribution](../references/RELATED_WORK.md) identifies inherited ingredients, and the [verification guide](../verification/README.md) separates direct finite checks from the analytical proofs. No universal crossover law is needed to state the supported comparison.
