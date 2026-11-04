# What the two thresholds mean operationally

For the infinite-temperature family $`\Phi_{\eta,t}=e^{t\mathcal L_{0,\eta}}`$, the two thresholds mark different losses of quantum functionality:

```math
\boxed{
Q_{\leftrightarrow}(\Phi_{\eta,t})>0
\quad\Longleftrightarrow\quad t\lt t_P(\eta),
\qquad
\Phi_{\eta,t}\text{ is measure-and-prepare}
\quad\Longleftrightarrow\quad t\geq t_E(\eta).
}
```

Here $`Q_{\leftrightarrow}`$ is the quantum capacity per independent use of the channel with unlimited two-way classical communication. The time $`t`$ is the duration of each noisy use. The capacity statement allows encoding across arbitrarily many independent uses and adaptive local operations with classical communication.

Every positive interference parameter has $`t_P\lt t_E`$. In the interval $`[t_P,t_E)`$, the channel has zero two-way quantum capacity and still cannot be represented by measuring its input and preparing an output state. Its normalized Choi state is PPT and entangled. This is the binding-entanglement regime. The term and the channel/state connection have a longstanding precedent in [Horodecki, Horodecki and Horodecki, *Binding entanglement channels* (2000)](https://doi.org/10.1080/09500340008244047).

The proof uses an explicit two-qubit distillation certificate before PPT onset. It does not assume that arbitrary NPT states are distillable.

## 1. A local projection before PPT onset

Let $`J_{\eta,t}`$ be the normalized Choi state. Use the multipliers from the [exact solution](exact_thresholds.md):

```math
r=e^{-8t},\qquad u=e^{-(10-2\eta)t},\qquad
v=e^{-(10+2\eta)t},\qquad b=e^{-12t}.
```

Alice prepares $`\Omega_4`$, keeps its reference half, and sends its other half through the channel. Alice and Bob then each measure the two-outcome projection with successful projector

```math
\Pi=\lvert0\rangle\langle0\rvert+\lvert1\rangle\langle1\rvert.
```

They keep a pair only when both report success. In the successful two-qubit basis $`00,01,10,11`$, the unnormalized state is

```math
(\Pi\otimes\Pi)J_{\eta,t}(\Pi\otimes\Pi)
=\frac1{16}
\begin{pmatrix}
1+r+2b&0&0&2(u+v)\\
0&1-r&0&0\\
0&0&1-r&0\\
2(u+v)&0&0&1+r+2b
\end{pmatrix}.
```

Its success probability is

```math
p_{\rm proj}=\frac{1+b}{4}\geq\frac14.
```

The conditional state $`\sigma_{\eta,t}`$ is therefore the displayed numerator matrix divided by $`4(1+b)`$. Neither a vanishing-probability limit nor a change of local subspace with $`t`$ is needed.

The fixed Schmidt-rank-two vector

```math
\lvert\psi^-_{01}\rangle
=\frac{\lvert0,1\rangle-\lvert1,0\rangle}{\sqrt2}
```

is an eigenvector of $`J_{\eta,t}^{\Gamma}`$ with eigenvalue

```math
\frac{1-r-2u-2v}{16}.
```

After conditioning, its partial-transpose expectation is $`(1-r-2u-2v)/[4(1+b)]`$. It is negative exactly when $`t\lt t_P`$. Thus the successful two-qubit state is entangled throughout the entire pre-PPT interval.

Every entangled two-qubit state is distillable, as established by [Horodecki, Horodecki and Horodecki (1997)](https://doi.org/10.1103/PhysRevLett.78.574). Consequently the channel has positive two-way-assisted quantum capacity for every fixed $`t\lt t_P`$.

### An explicit positive-rate route

The conditional state is Bell diagonal. Its overlap with $`\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2`$ is

```math
F=\frac{1+r+2b+2(u+v)}{4(1+b)}.
```

The condition $`F>1/2`$ is precisely $`r+2u+2v>1`$. An LOCC isotropic twirl preserves $`F`$ and produces Bell probabilities $`(F,g,g,g)`$, where $`g=(1-F)/3`$.

The standard two-pair recurrence protocol has success probability and updated fidelity

```math
p_{\rm rec}(F)=F^2+2Fg+5g^2,
\qquad
F'=\frac{F^2+g^2}{F^2+2Fg+5g^2}.
```

Retwirl the successful pairs after each recurrence round, preserving their fidelity, so the next round again starts with probabilities $`(F_j,g_j,g_j,g_j)`$. For $`1/2\lt F\lt 1`$, the update increases $`F`$ strictly and repeated updates converge to one. After a finite number $`k`$ of rounds, the hashing yield

```math
1-h_2(F_k)-(1-F_k)\log_2 3
```

is positive. Here $`h_2`$ is binary entropy in bits. Projecting independent Choi pairs, applying these recurrence rounds, and hashing therefore gives the explicit strictly positive lower bound

```math
Q_{\leftrightarrow}(\Phi_{\eta,t})
\geq
p_{\rm proj}\,2^{-k}
\left(\prod_{j=0}^{k-1}p_{\rm rec}(F_j)\right)
\left[1-h_2(F_k)-(1-F_k)\log_2 3\right]>0.
```

This bound is illustrative and is not an optimization of the capacity. The recurrence and hashing ingredients are inherited from [Bennett et al., *Purification of noisy entanglement and faithful teleportation via noisy channels* (1996)](https://doi.org/10.1103/PhysRevLett.76.722) and [Bennett et al., *Mixed-state entanglement and quantum error correction* (1996)](https://doi.org/10.1103/PhysRevA.54.3824). The family-specific ingredient is that the same local projection has $`F>1/2`$ all the way to the exact PPT boundary.

## 2. Zero capacity after PPT onset, including adaptive protocols

For a channel $`\Phi`$, positivity of its partially transposed Choi matrix is equivalent to complete positivity of $`T\circ\Phi`$, where $`T`$ is transposition on the output. If $`\Phi`$ is PPT, then for every positive input $`\rho_{RA}`$,

```math
\bigl[(\operatorname{id}_R\otimes\Phi)(\rho_{RA})\bigr]^{\Gamma_B}
=(\operatorname{id}_R\otimes T\circ\Phi)(\rho_{RA})\geq0.
```

The conclusion extends to arbitrary adaptive protocols. Suppose Alice and Bob currently share a state $`\rho_{A'A_0B}`$ that is PPT across Alice versus Bob, and Alice sends $`A_0`$ through a PPT channel to create $`B_0`$. Then

```math
\rho_{A'BB_0}'{}^{\Gamma_{BB_0}}
=\bigl(\operatorname{id}_{A'B}\otimes T_{B_0}\circ\Phi_{A_0\to B_0}\bigr)
(\rho_{A'A_0B}^{\Gamma_B})\geq0.
```

The map on the right is completely positive. Local operations and classical communication preserve PPT in every conditioned branch. Starting with a separable state, induction over channel uses and intervening LOCC therefore keeps the full shared state PPT, even when later inputs depend on earlier outcomes.

A PPT state $`\omega`$ cannot approximate a maximally entangled state of Schmidt rank $`D>1`$ with high fidelity. In the pure-target overlap convention,

```math
\begin{aligned}
\langle\Omega_D\rvert\omega\lvert\Omega_D\rangle
&=\operatorname{Tr}\!\left[
\left(\lvert\Omega_D\rangle\langle\Omega_D\rvert\right)^\Gamma
\omega^\Gamma\right]\\
&=\frac1D\operatorname{Tr}(F_{\rm swap}\omega^\Gamma)
\leq\frac1D,
\end{aligned}
```

because $`\omega^\Gamma\geq0`$, its trace is one, and $`F_{\rm swap}\leq I`$. Thus no positive rate of reliable quantum communication is possible. This is the PPT obstruction to distillation introduced in [Horodecki, Horodecki and Horodecki (1998)](https://doi.org/10.1103/PhysRevLett.80.5239), applied here to the complete adaptive channel protocol.

For the present family, the [exact PPT criterion](exact_thresholds.md#2-exact-ppt-criterion) therefore proves

```math
Q_{\leftrightarrow}(\Phi_{\eta,t})=0
\qquad\text{for every }t\geq t_P(\eta).
```

## 3. Entanglement breaking at the later threshold

For $`t_P\leq t\lt t_E`$, sending half of $`\Omega_4`$ still creates an entangled Choi state, certified by the Breuer–Hall witness. Every such state is PPT, so its entanglement is undistillable by LOCC. The surviving correlation does not establish a positive private capacity or a storage advantage.

At $`t=t_E`$, the [twenty-component decomposition](exact_thresholds.md#4-a-constructive-eb-decomposition-at-the-boundary) expresses the entire channel as a measure-and-prepare operation. This is a statement for every input and every reference system, rather than only for a selected initial state. Later channels remain measure-and-prepare by composition.

At $`\eta=0`$, the capacity-positivity and EB boundaries coincide. At $`\eta>0`$, they separate even though the population transition matrix and every individual matrix-unit self-damping coefficient stay fixed. The generator's coherence-transfer terms determine the separation.

## 4. Scope of the operational conclusions

- The exact capacity-positivity boundary is proved for $`\beta=0`$ and the specified channel family. The [positive-temperature result](thermal_extension.md) proves a strict PPT-entangled example; it does not provide exact finite-temperature capacity thresholds.
- The statement concerns two-way-assisted quantum capacity under independent channel uses. It does not determine the unassisted capacity, the numerical value of the positive capacity, or private communication rates.
- A PPT-entangled channel has residual input-reference entanglement, but this alone does not give a useful memory, an entanglement-distillation protocol, or an operational advantage over an EB channel for a specified application.
- The proposed physical control changes the distinguishability of equal-frequency transition pathways. It preserves the entire classical population generator while changing coherence transfer; it does not preserve the complete Liouvillian spectrum.

The [verification suite](../verification/README.md) checks the local projection, its success probability and normalized state, the rank-two eigenvector, and the positive-rate construction on representative pre-threshold points.
