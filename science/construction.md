# Explicit measurement and Fisher information

An eigenbasis-calibrated measurement with $`2rd-r`$ outcomes preserves at least the fraction $`1/(2r)`$ of the symmetric logarithmic derivative quantum Fisher information in every tangent direction of a rank-$`r`$ state. The effects depend on the rank and the calibrated basis; their weights do not depend on the positive eigenvalues, the parameter submodel, or the estimation cost. This page gives the effects and their exact Fisher information. The [optimality proof](optimality.md) shows that the fraction is sharp when the full rank-$`r`$ tangent space is required.

See [the model](model.md) for the statistical setting, [estimation](estimation.md) for operational consequences, [resources](resources.md) for calibration and measurement costs, and [related work](../references/RELATED_WORK.md) for attribution.

## State, tangent space, and fixed calibration

Let $`\mathcal H`$ have finite dimension $`d`$, and fix a state

```math
\rho=\sum_{j=1}^{r}\lambda_j |e_j\rangle\langle e_j|,
\qquad
2\le r\lt d,
\qquad
\lambda_j>0,
\qquad
\sum_{j=1}^{r}\lambda_j=1.
```

Write $`P`$ for its support projector and $`Q=\mathbb I-P`$ for its kernel projector. Set $`k=d-r`$, and choose an orthonormal kernel basis $`f_1,\ldots,f_k`$. Degenerate positive eigenvalues cause no difficulty: any orthonormal eigenbasis inside each degenerate eigenspace is allowed.

The real tangent space of the manifold of states of exact rank $`r`$ is

```math
\mathcal T_\rho
=\{X=X^\dagger:\operatorname{tr}X=0,\ QXQ=0\}.
```

In the decomposition $`P\mathcal H\oplus Q\mathcal H`$, its elements have the form

```math
X=
\begin{pmatrix}
A&B\\
B^\dagger&0
\end{pmatrix},
\qquad
A=A^\dagger,\quad \operatorname{tr}A=0.
```

For such a tangent, use the notation

```math
x_j=\langle e_j|X|e_j\rangle,\qquad
x_{j\ell}=\langle e_j|X|e_\ell\rangle,\qquad
b_{ja}=\langle e_j|X|f_a\rangle.
```

The symmetric logarithmic derivative (SLD) Fisher form is

```math
\begin{aligned}
J_\rho(X)
={}&
\sum_{j=1}^{r}\frac{x_j^2}{\lambda_j}
+4\sum_{1\le j\lt\ell\le r}
\frac{|x_{j\ell}|^2}{\lambda_j+\lambda_\ell}
+4\sum_{j=1}^{r}\sum_{a=1}^{k}
\frac{|b_{ja}|^2}{\lambda_j}.
\end{aligned}
```

For example, this follows by solving $`X=(\rho L_X+L_X\rho)/2`$, choosing the kernel block of $`L_X`$ to be zero, and evaluating $`J_\rho(X)=\operatorname{tr}(\rho L_X^2)`$. The support–kernel SLD entry is $`2b_{ja}/\lambda_j`$; both conjugate entries are included in the displayed metric.

All effects below are chosen at this calibration state and then **held fixed when differentiating the outcome probabilities**. In particular, if $`\rho_\theta`$ is a smooth local model through $`\rho`$, derivatives act on $`\rho_\theta`$, not on the eigenvectors used to build the measurement.

## Measurement effects

The measurement consists of two families of positive rank-one effects.

### Support-pair effects

For each $`1\le j\lt\ell\le r`$ and each $`\zeta\in\{1,-1,i,-i\}`$, define

```math
|\psi_{j\ell,\zeta}\rangle
=\frac{|e_j\rangle+\zeta|e_\ell\rangle}{\sqrt 2},
\qquad
G_{j\ell,\zeta}
=\frac{1}{2r}
|\psi_{j\ell,\zeta}\rangle
\langle\psi_{j\ell,\zeta}|.
```

These effects resolve the real and imaginary coherences between occupied eigenvectors. Such pair measurements are a standard ingredient of adaptive tomography; see [Pereira20](../references/RELATED_WORK.md#pereira20).

### Fourier effects on one support vector and the kernel

Set

```math
N=2k+1,
\qquad
\omega=\exp(2\pi i/N).
```

For each $`j=1,\ldots,r`$ and $`t=0,\ldots,N-1`$, define the unnormalized vector

```math
|v_{jt}\rangle
=|e_j\rangle+\sum_{a=1}^{k}\omega^{at}|f_a\rangle
```

and the effect

```math
F_{jt}
=\frac{1}{rN}|v_{jt}\rangle\langle v_{jt}|.
```

For fixed $`j`$, the effects $`|v_{jt}\rangle\langle v_{jt}|/N`$ form a pure-state Fisher-symmetric measurement on $`\operatorname{span}\{e_j\}\oplus Q\mathcal H`$, locally about $`|e_j\rangle`$. Pure-state Fisher-symmetric measurements are established in [Li16](../references/RELATED_WORK.md#li16). The factor $`1/r`$ allows these $`r`$ families to coexist in one complete measurement on $`\mathcal H`$.

## Completeness

The root-of-unity identity

```math
\frac1N\sum_{t=0}^{N-1}\omega^{nt}
=
\begin{cases}
1,& n\equiv0\pmod N,\\
0,& n\not\equiv0\pmod N
\end{cases}
```

gives, for each $`j`$,

```math
\sum_{t=0}^{N-1}F_{jt}
=\frac1r\bigl(|e_j\rangle\langle e_j|+Q\bigr).
```

Indeed, the support–kernel terms average to zero, and the kernel matrix element with indices $`a,b`$ survives exactly when $`a=b`$. Summing over the occupied eigenvectors gives

```math
\sum_{j,t}F_{jt}=\frac1r P+Q.
```

For a support pair, cancellation of the four phases gives

```math
\sum_{\zeta\in\{1,-1,i,-i\}}G_{j\ell,\zeta}
=\frac1r
\bigl(|e_j\rangle\langle e_j|+
|e_\ell\rangle\langle e_\ell|\bigr).
```

Each occupied eigenvector occurs in $`r-1`$ pairs, so

```math
\sum_{j\lt\ell,\zeta}G_{j\ell,\zeta}
=\frac{r-1}{r}P.
```

Consequently,

```math
\sum_{j,t}F_{jt}
+\sum_{j\lt\ell,\zeta}G_{j\ell,\zeta}
=P+Q=\mathbb I.
```

This proves that the union of the two effect families is a POVM.

## Probabilities and outcome count

At the calibration state,

```math
\operatorname{tr}(\rho F_{jt})
=\frac{\lambda_j}{rN}>0,
\qquad
\operatorname{tr}(\rho G_{j\ell,\zeta})
=\frac{\lambda_j+\lambda_\ell}{4r}>0.
```

There are finitely many outcomes and all have positive probability. Thus, for any smooth local rank-$`r`$ model, its classical outcome model has ordinary smooth scores in a neighborhood of the calibration point. The construction introduces no zero-probability residual outcome.

The number of labeled outcomes is

```math
r(2k+1)+4\binom r2
=r\bigl(2(d-r)+1\bigr)+2r(r-1)
=2rd-r.
```

This is the size of the displayed construction; no minimum-outcome claim is needed for the Fisher-optimality theorem.

## Fisher information of the Fourier effects

For a tangent $`X`$, the derivative of a Fourier outcome probability is

```math
\operatorname{tr}(XF_{jt})
=\frac1{rN}
\left(x_j+2\operatorname{Re}
\sum_{a=1}^{k}\omega^{at}b_{ja}\right).
```

There is no kernel–kernel contribution because $`QXQ=0`$. For fixed $`j`$, put

```math
z_t=\sum_{a=1}^{k}\omega^{at}b_{ja}.
```

The choice $`N=2k+1`$ ensures

```math
\frac1N\sum_t z_t=0,\qquad
\frac1N\sum_t |z_t|^2=\sum_a|b_{ja}|^2,\qquad
\frac1N\sum_t z_t^2=0.
```

For the last identity, every frequency $`a+b`$ lies between $`2`$ and $`2k=N-1`$, so no such frequency is zero modulo $`N`$. It follows that

```math
\frac1N\sum_t
\bigl(x_j+2\operatorname{Re}z_t\bigr)^2
=x_j^2+2\sum_a|b_{ja}|^2.
```

Hence the Fisher contribution of the $`j`$th Fourier family is exactly

```math
\begin{aligned}
I_{F,j}(X)
&=\sum_{t=0}^{N-1}
\frac{\bigl[\operatorname{tr}(XF_{jt})\bigr]^2}
{\operatorname{tr}(\rho F_{jt})}\\
&=\frac1{r\lambda_j}
\left(x_j^2+2\sum_{a=1}^{k}|b_{ja}|^2\right).
\end{aligned}
```

In particular, the phases cancel the Fisher cross terms between a diagonal variation and a support–kernel coherence, and between distinct kernel coordinates.

## Fisher information of the support pairs

For a fixed pair, write $`s=x_j+x_\ell`$ and $`z=x_{j\ell}`$. Then

```math
\operatorname{tr}(XG_{j\ell,\zeta})
=\frac1{2r}
\left(\frac{s}{2}+\operatorname{Re}(\zeta z)\right).
```

The four phases obey

```math
\sum_\zeta \operatorname{Re}(\zeta z)=0,
\qquad
\sum_\zeta [\operatorname{Re}(\zeta z)]^2=2|z|^2.
```

Dividing the squared derivatives by the common outcome probability and summing yields

```math
\begin{aligned}
I_{G,j\ell}(X)
&=\sum_{\zeta}
\frac{\bigl[\operatorname{tr}(XG_{j\ell,\zeta})\bigr]^2}
{\operatorname{tr}(\rho G_{j\ell,\zeta})}\\
&=\frac{(x_j+x_\ell)^2+2|x_{j\ell}|^2}
{r(\lambda_j+\lambda_\ell)}.
\end{aligned}
```

## Exact Fisher identity

Let $`M_\rho`$ denote the complete POVM above. Adding the two families gives

```math
\begin{aligned}
I_{M_\rho}(X)
={}&\frac1r\sum_{j=1}^{r}\frac{x_j^2}{\lambda_j}
+\frac1r\sum_{j\lt\ell}
\frac{(x_j+x_\ell)^2+2|x_{j\ell}|^2}
{\lambda_j+\lambda_\ell}\\
&+\frac2r\sum_{j=1}^{r}\sum_{a=1}^{k}
\frac{|b_{ja}|^2}{\lambda_j}.
\end{aligned}
```

Comparison with the SLD metric gives the exact identity

```math
\boxed{
I_{M_\rho}(X)
=\frac1{2r}J_\rho(X)
+\frac1{2r}\sum_{j=1}^{r}\frac{x_j^2}{\lambda_j}
+\frac1r\sum_{j\lt\ell}
\frac{(x_j+x_\ell)^2}{\lambda_j+\lambda_\ell}.
}
```

Both additional quadratic forms are nonnegative. Therefore

```math
I_{M_\rho}\succeq\frac1{2r}J_\rho
\quad\text{on }\mathcal T_\rho.
```

Equality in the quadratic-form inequality holds precisely when all the support diagonal entries $`x_j`$ vanish. In particular, every nonzero support–kernel tangent realizes the ratio $`1/(2r)`$. Polarization of the identity gives the corresponding bilinear and matrix identities.

For a smooth submodel with tangent map

```math
X(u)=\sum_{\alpha}u_\alpha\,
\partial_\alpha\rho_\theta\big|_{\theta=\theta_0},
```

substituting $`X(u)`$ proves the same matrix inequality for its classical and quantum Fisher matrices. The measurement remains fixed at $`M_{\rho_{\theta_0}}`$ throughout this differentiation. [Estimation](estimation.md) states the resulting cost bounds and their regularity conditions.

## Why the ambient dimension does not set the fraction

Each occupied eigenvector is measured coherently against the entire kernel. A Fourier family spends $`1/r`$ of the completeness weight on its occupied vector and on every kernel direction. The $`r`$ families therefore exhaust the kernel completeness weight while using only $`1/r`$ of the weight on each occupied vector. The support-pair effects use the remaining $`(r-1)/r`$ weight there.

Adding kernel directions increases the number of Fourier outcomes. It does not increase the number of occupied vectors sharing the kernel weight. This allocation produces exactly the same relative Fisher information in all support–kernel directions, while the remaining effects supply the information required inside the support.

The formula is valid for every positive spectrum in the chosen eigenbasis, including degenerate or poorly conditioned spectra. For $`r=1`$, the support-pair family disappears and the formula reduces to the known pure-state Fisher symmetry $`I=J/2`$ [Li16](../references/RELATED_WORK.md#li16).

This is a local calibrated statement. The dependence of finite-sample calibration accuracy on small positive eigenvalues, and the distinction between POVM existence and an efficient implementation with restricted hardware, are recorded in [resources](resources.md).
