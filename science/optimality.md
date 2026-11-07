# Sharp optimality for the full fixed-rank tangent space

For every state of rank $`2\le r\lt d`$, the largest fraction of SLD quantum Fisher information that one single-copy measurement can preserve in every regular fixed-rank tangent direction is exactly

```math
c_*(\rho)=\frac1{2r}.
```

The [explicit construction](construction.md) attains this fraction with $`2rd-r`$ positive-probability outcomes. This page proves the matching upper bound for arbitrary finite, countable, or continuous outcome spaces.

The converse is the support–kernel refinement of the Gill–Massar inequality, stated by Zhou and Chen in Theorem 4, Case 3, Eq. (76), and proved in their Appendix D, Eq. (172) [ZC26](../references/RELATED_WORK.md#zc26). It belongs to the information-tradeoff framework of [GM00](../references/RELATED_WORK.md#gm00). We reproduce it using positivity of the effect density, so no rank-one refinement or restriction on the number of outcomes is required.

See [the model](model.md) for the Fisher convention, [estimation](estimation.md) for statistical consequences, [resources](resources.md) for calibration assumptions, and [related work](../references/RELATED_WORK.md) for the prior results.

## Optimization problem

Fix

```math
\rho=\sum_{j=1}^{r}\lambda_j|e_j\rangle\langle e_j|,
\qquad
\lambda_j>0,\qquad \sum_j\lambda_j=1,
```

and write $`P`$ for its support projector, $`Q=\mathbb I-P`$, and $`k=d-r>0`$. The full real tangent space is

```math
\mathcal T_\rho
=\{X=X^\dagger:\mathrm{tr}\,X=0,\ QXQ=0\},
\qquad
\dim\mathcal T_\rho=r(2d-r)-1.
```

The SLD form $`J_\rho`$ is positive definite on this tangent space. For a POVM $`M`$ held fixed at $`\rho`$, let $`I_M`$ be its ordinary first-order score Fisher form. Define

```math
\begin{aligned}
c(M,\rho)
&=\inf_{X\in\mathcal T_\rho,\ X\ne0}
\frac{I_M(X)}{J_\rho(X)},\\
c_*(\rho)
&=\sup_M c(M,\rho).
\end{aligned}
```

In any real tangent coordinate system this is equivalently

```math
c(M,\rho)
=\lambda_{\min}\!\left(
J_\rho^{-1/2}I_MJ_\rho^{-1/2}
\right).
```

The quotient definition makes its independence of coordinates explicit. The upper bound below holds for every POVM with the score convention specified next. The same optimum is obtained if the supremum is restricted to measurements with regular local classical outcome models, because the attaining finite measurement has strictly positive probabilities.

## General POVMs and the score convention

Let $`M`$ be a normalized POVM on a measurable outcome space $`(\Omega,\Sigma)`$:

```math
M(A)\succeq0,\qquad
M(\Omega)=\mathbb I.
```

Use the finite scalar trace measure

```math
\mu(A)=\mathrm{tr}\,M(A),
\qquad
\mu(\Omega)=d.
```

In finite Hilbert-space dimension, the matrix-valued Radon–Nikodym derivative exists:

```math
M(A)=\int_A E(\omega)\,d\mu(\omega),
\qquad
E(\omega)\succeq0,\qquad
\mathrm{tr}\,E(\omega)=1
\quad\text{for }\mu\text{-almost every }\omega.
```

Indeed, each matrix entry of $`M`$ is absolutely continuous with respect to $`\mu`$. Positivity and the unit-trace identity for the density follow from the corresponding measure identities. No finite-outcome assumption enters this representation.

The outcome probability density and its derivative in tangent direction $`X`$ are

```math
p(\omega)=\mathrm{tr}\bigl(\rho E(\omega)\bigr),
\qquad
q_X(\omega)=\mathrm{tr}\bigl(XE(\omega)\bigr).
```

At an outcome with $`p(\omega)=0`$, positivity implies $`E(\omega)P=PE(\omega)=0`$. To see this in the eigenbasis of $`\rho`$, the identity $`\sum_j\lambda_j E_{jj}=0`$ forces every occupied diagonal entry to vanish, and positive semidefiniteness then forces its row and column to vanish. Since $`QXQ=0`$, it follows that $`q_X(\omega)=0`$ for every allowed tangent.

The score and its Fisher form are therefore defined by

```math
\ell_X(\omega)=
\begin{cases}
q_X(\omega)/p(\omega),&p(\omega)>0,\\
0,&p(\omega)=0,
\end{cases}
\qquad
I_M(X,Y)
=\int_{\{p>0\}}\frac{q_Xq_Y}{p}\,d\mu.
```

This is the ordinary score convention: zero-probability outcomes contribute zero at the calibration point. When the classical model is differentiable in quadratic mean, it is its usual regular Fisher form. Direction-dependent limits at zero-probability outcomes are not substituted into this definition. The attaining measurement avoids the issue because every outcome probability is positive; the operational regularity discussion is in [estimation](estimation.md).

These forms are finite. For an SLD $`L_X`$, Cauchy–Schwarz gives pointwise

```math
q_X(\omega)^2
\le
p(\omega)\,
\mathrm{tr}\bigl(\rho L_XE(\omega)L_X\bigr).
```

Integrating and using normalization gives

```math
I_M(X)\le
\mathrm{tr}(\rho L_X^2)=J_\rho(X).
```

## Information budget for support rotations

Consider the tangent subspace

```math
\mathcal C_\rho
=\left\{
\begin{pmatrix}
0&B\\
B^\dagger&0
\end{pmatrix}
:\ B\in\mathbb C^{r\times k}
\right\}
\subset\mathcal T_\rho.
```

It has real dimension $`2rk`$. These are legitimate two-sided rank-preserving tangents. Explicitly, let $`D=\mathrm{diag}(\lambda_1,\ldots,\lambda_r)`$ and define the skew-Hermitian generator

```math
K_B=
\begin{pmatrix}
0&-D^{-1}B\\
B^\dagger D^{-1}&0
\end{pmatrix}.
```

The path $`\rho_t=e^{tK_B}\rho e^{-tK_B}`$ has rank $`r`$ for both signs of $`t`$, and

```math
\left.\frac{d\rho_t}{dt}\right|_{t=0}
=[K_B,\rho]
=
\begin{pmatrix}
0&B\\
B^\dagger&0
\end{pmatrix}.
```

Choose an orthonormal kernel basis $`f_1,\ldots,f_k`$ and the real tangent basis

```math
\begin{aligned}
R_{ja}
&=|e_j\rangle\langle f_a|+
|f_a\rangle\langle e_j|,\\
S_{ja}
&=i|e_j\rangle\langle f_a|-
i|f_a\rangle\langle e_j|.
\end{aligned}
```

In these coordinates the SLD Fisher matrix restricted to $`\mathcal C_\rho`$ is diagonal:

```math
J_{\mathcal C}
=\mathrm{diag}_{j,a}
\left(\frac4{\lambda_j},\frac4{\lambda_j}\right).
```

For an effect density, abbreviate

```math
E_{ja}=\langle e_j|E|f_a\rangle,\qquad
E_{jj}=\langle e_j|E|e_j\rangle,\qquad
E_{aa}^{K}=\langle f_a|E|f_a\rangle.
```

The derivatives in the two basis directions are

```math
q_{R_{ja}}=2\mathrm{Re}\,E_{ja},
\qquad
q_{S_{ja}}=2\mathrm{Im}\,E_{ja}.
```

Consequently,

```math
\mathrm{tr}\!\left(J_{\mathcal C}^{-1}I_{\mathcal C}\right)
=
\int_{\{p>0\}}
\frac{\displaystyle\sum_{j=1}^{r}\sum_{a=1}^{k}
\lambda_j|E_{ja}|^2}
{p}\,d\mu.
```

Every positive semidefinite matrix satisfies

```math
|E_{ja}|^2\le E_{jj}E_{aa}^{K}.
```

For each kernel index $`a`$, this gives

```math
\sum_j\lambda_j|E_{ja}|^2
\le
\left(\sum_j\lambda_jE_{jj}\right)E_{aa}^{K}
=p\,E_{aa}^{K}.
```

Summing over $`a`$, integrating over $`\{p>0\}`$, and using completeness establishes the refined bound:

```math
\begin{aligned}
\mathrm{tr}\!\left(J_{\mathcal C}^{-1}I_{\mathcal C}\right)
&\le
\int_{\{p>0\}}\mathrm{tr}(QE)\,d\mu\\
&\le
\int_\Omega\mathrm{tr}(QE)\,d\mu\\
&=\mathrm{tr}\,Q=k=d-r.
\end{aligned}
```

Thus

```math
\boxed{
\mathrm{tr}\!\left(J_{\mathcal C}^{-1}I_{\mathcal C}\right)
\le d-r.
}
```

This is [ZC26](../references/RELATED_WORK.md#zc26), Eq. (76), with no condition-number assumption needed for the converse. The argument applies to all positive effect densities. It therefore covers finite, countable, and continuous outcome spaces directly.

## Sharp fraction on the full tangent space

Suppose a POVM preserves a fraction $`c`$ in every full tangent direction:

```math
I_M\succeq cJ_\rho
\quad\text{on }\mathcal T_\rho.
```

Restricting the two forms to $`\mathcal C_\rho`$ gives

```math
J_{\mathcal C}^{-1/2}I_{\mathcal C}
J_{\mathcal C}^{-1/2}
\succeq c\,\mathbb I_{2rk}.
```

Taking the trace and applying the support-rotation bound yields

```math
2rk\,c
\le
\mathrm{tr}\!\left(J_{\mathcal C}^{-1}I_{\mathcal C}\right)
\le k.
```

Since $`k>0`$,

```math
c\le\frac1{2r}.
```

The [construction](construction.md#exact-fisher-identity) satisfies $`I_{M_\rho}\succeq J_\rho/(2r)`$ on all of $`\mathcal T_\rho`$, and every nonzero support–kernel tangent has equality. Hence the supremum is attained and

```math
\boxed{
c_*(\rho)=\frac1{2r}
\qquad (2\le r\lt d).
}
```

For $`r=1`$, the same conclusion is the established pure-state value $`1/2`$ [Li16](../references/RELATED_WORK.md#li16). The present argument requires a nonempty kernel; it makes no formula claim for the full-rank problem $`r=d`$.

## Meaning and scope

The converse allocates at most $`d-r`$ units of normalized Fisher information across $`2r(d-r)`$ real support-rotation directions. Their number and their information budget both grow linearly with the kernel dimension. The largest uniform fraction is therefore bounded by $`1/(2r)`$. The explicit measurement reaches that fraction on these directions while providing at least as much relative information throughout the support tangent space.

The optimization is over one measurement that protects **all** directions at the calibration state. A restricted parameter submodel can admit a larger fraction; in particular, a regular single-parameter model admits its SLD-optimal measurement. Randomized measurement settings with their labels retained are included in the POVM formulation, as are arbitrary outcome counts.

The theorem determines a local Fisher-information fraction. It does not identify $`2r`$ with an exact collective-versus-individual cost ratio, because the SLD benchmark need not be jointly attainable. The justified cost implication and calibration requirements are given in [estimation](estimation.md) and [resources](resources.md).
