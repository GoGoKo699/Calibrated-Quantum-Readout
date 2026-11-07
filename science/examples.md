# A rank-two qutrit

The smallest mixed-state example has two occupied levels and one empty level. It shows how one readout can protect all local directions even when one occupied probability is very small.

## 1. Seven local directions

Take

```math
\rho_p=\operatorname{diag}(p,1-p,0),\qquad 0\lt p\lt1.
```

A general tangent to the rank-two manifold has the form

```math
X=\begin{pmatrix}
a&x_{12}+iy_{12}&x_{13}+iy_{13}\\
x_{12}-iy_{12}&-a&x_{23}+iy_{23}\\
x_{13}-iy_{13}&x_{23}-iy_{23}&0
\end{pmatrix}.
```

The coordinate $`a`$ changes the occupied populations. The two $`12`$ coordinates create occupied coherences. The four remaining coordinates move the occupied support into the empty third level. These seven coordinates describe physical constant-rank curves locally, as explained in the [model](model.md).

In the coordinate order $`(a,x_{12},y_{12},x_{13},y_{13},x_{23},y_{23})`$,

```math
J=\operatorname{diag}\left(
\frac1{p(1-p)},\ 4,\ 4,\ \frac4p,\ \frac4p,
\ \frac4{1-p},\ \frac4{1-p}\right).
```

As $`p`$ tends to zero, the absolute quantum information in the population and first-level support-rotation directions grows. The theorem compares the measurement with these direction-dependent quantum scales, rather than comparing raw Fisher eigenvalues in arbitrary units.

## 2. Ten effects

For the occupied pair, use

```math
\frac14|\pm_x\rangle\langle\pm_x|,
\qquad \frac14|\pm_y\rangle\langle\pm_y|,
\qquad
|\pm_x\rangle=\frac{e_1\pm e_2}{\sqrt2},
\quad |\pm_y\rangle=\frac{e_1\pm i e_2}{\sqrt2}.
```

For each $`j=1,2`$, include three Fourier effects

```math
F_{jt}=\frac16|e_j+\omega^t e_3\rangle
\langle e_j+\omega^t e_3|,
\qquad \omega=e^{2\pi i/3},\qquad t=0,1,2.
```

The four pair effects contribute $`(P_1+P_2)/2`$. The three effects associated with $`j`$ sum to $`(P_j+P_3)/2`$. Adding both Fourier families therefore completes the identity.

The pair probabilities are all $`1/8`$. The first Fourier family has three probabilities $`p/6`$, and the second has three probabilities $`(1-p)/6`$. They sum to one, and every outcome remains positive at each fixed $`0\lt p\lt1`$. There is no discarded or postselected branch.

## 3. Information in each direction

Substituting in the [exact Fisher identity](construction.md) gives

```math
I=\operatorname{diag}\left(
\frac1{2p(1-p)},\ 1,\ 1,\ \frac1p,\ \frac1p,
\ \frac1{1-p},\ \frac1{1-p}\right).
```

Consequently,

```math
J^{-1/2}IJ^{-1/2}
=\operatorname{diag}\left(\frac12,
\frac14,\frac14,\frac14,\frac14,\frac14,\frac14\right).
```

The worst fraction is exactly $`1/4`$ for every positive spectrum. The population direction receives a larger fraction. Thus an E-optimal measurement need not have its whole Fisher matrix proportional to $`J`$; the mixed-state construction is not claimed to be Fisher symmetric on the full tangent.

The normalized trace is two, saturating the full Gill–Massar budget $`d-1`$. The four support-rotation directions alone have normalized trace one, saturating the sharper budget $`d-r`$. If all four of those fractions exceeded $`1/4`$, their sum would exceed one. This is the exact obstruction that makes the readout optimal.

For the illustrative weight $`W=J`$, the local score estimator's attained cost per inverse sample size is

```math
\operatorname{Tr}(JI^{-1})=2+6\times4=26,
\qquad \operatorname{Tr}(JJ^{-1})=7.
```

The first value is the cost of this E-optimal readout. It is not asserted to minimize that scalar cost over all measurements. E-optimality optimizes the least information fraction; minimizing a specified weighted sum of variances is a different design problem.

## 4. Why an empty level matters

Suppose instead that the occupied two-dimensional support is fixed and known to remain fixed. The four $`13`$ and $`23`$ coordinates are absent. The experiment becomes ordinary full-qubit tomography, whose calibrated normalized E-optimum is $`1/3`$ [Suzuki20](../references/RELATED_WORK.md#suzuki20).

Allowing that support to move into one additional empty level changes the optimum to $`1/4`$. The state has the same two nonzero eigenvalues, but the readout must now resolve four additional directions. The common kernel receives a finite measurement budget, and those support-motion directions set the optimal worst-direction fraction.

This is why measuring only within the estimated occupied subspace would miss part of the problem. The Fourier effects interfere each occupied eigenvector with the empty level before readout, retaining first-order sensitivity to support motion.

## 5. Calibration and verification

The displayed measurement uses the true nominal eigenbasis. The [resource account](resources.md) analyzes what happens when that basis is misaligned. In particular, a fixed small basis error can add background to a rare outcome and destroy a spectrum-uniform relative-information guarantee as $`p`$ tends to zero. That concerns learning or maintaining the apparatus, while the exact theorem concerns its performance at the calibrated point.

The [verification suite](../verification/README.md) constructs the ten effects directly, differentiates all seven outcome probabilities, and compares the resulting classical Fisher matrix with the matrix above. It also changes $`p`$, rotates the physical basis, tests higher ranks, and checks the general algebraic identity. The analytical [construction](construction.md) and [converse](optimality.md) establish the theorem for arbitrary dimensions and spectra.
