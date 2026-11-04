# From Rivas–Huelga to bath-interference bound entanglement

[Project milestones](MILESTONES.md) · [Scientific entrypoint](../science/README.md) · [Primary references](../references/RELATED_WORK.md)

An energy-population measurement can give the same results for two noisy quantum devices even when their effects on coherence differ. This project makes that comparison exact. The bath's ability to distinguish transition pathways changes, while the population generator stays fixed. The resulting channels lose useful distillable entanglement and all reference–system entanglement at different times.

Rivas–Huelga supplies the open-system framework for understanding how such a bath enters a master equation. This bridge translates that framework into the project's notation, works through one coherence-transfer calculation, and identifies the additional arguments needed to reach the entanglement theorem. The [milestone map](MILESTONES.md) organizes the complete project; the route below is a focused use of the selected anchor.

## Source and edition

The single educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_, first edition, SpringerBriefs in Physics, ©2012**, DOI [10.1007/978-3-642-23354-8](https://doi.org/10.1007/978-3-642-23354-8). Its bibliography key is `rivas2012open`.

The [publisher record](https://link.springer.com/book/10.1007/978-3-642-23354-8) and [printed contents](https://link.springer.com/content/pdf/bfm:978-3-642-23354-8/1) verify the edition and book sections. Springer lists initial electronic and softcover release in October 2011; its citation year and copyright year are 2012. The authors identify [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), revised 9 February 2012, as the corrected preprint version of the published book.

**Book and preprint numbers differ.** The correspondence below is checked against both contents lists. In particular, the book's Chapter 5 is the preprint's Section 6. Book chapters 2, 3, 4 and 5 occupy printed pages 15–17, 19–31, 33–48 and 49–80, respectively. Those are publisher page ranges, not PDF-page numbers for the preprint.

## Reading route

Use the following parts when their associated project question arises. Reading the entire book is not a prerequisite for using the repository.

| Purpose | First-edition book | Author preprint v2 | Continue in this project |
|---|---|---|---|
| Exponentials and repeated evolution | §§1.2–1.3 | §§2.2–2.3 | [Semigroup and time conventions](../science/model.md#conventions-and-scales) |
| Hamiltonian evolution and its removal | Chapter 2 | §3 | [The Hamiltonian part](../science/model.md#the-hamiltonian-part) |
| Maps valid for a system with an untouched reference | §§3.1–3.2, 3.5 | §§4.1–4.2, 4.5 | [Channel definitions](../science/README.md#definitions-and-principal-result) |
| Classical and quantum generators; stationary states | §§4.1–4.4 | §§5.1–5.4 | [Population matching](../science/model.md#the-entire-population-generator) and [primitivity](../science/model.md#primitivity-including-maximal-interference) |
| Frequency decomposition, bath correlations and weak coupling | §§5.2.1–5.2.4 | §§6.2.1–6.2.4 | [The specified bath blocks](../science/model.md#the-davies-generator) |
| Secular approximation and thermal stationarity | §§5.2.6, 5.2.8 | §§6.2.6, 6.2.8 | [Detailed balance](../science/model.md#gns-detailed-balance-with-the-rate-sign-checked) and [detuning](../science/model.md#detuning-and-the-secular-order-of-limits) |

The publisher provides separate chapter records for [Chapter 3](https://link.springer.com/chapter/10.1007/978-3-642-23354-8_3), [Chapter 4](https://link.springer.com/chapter/10.1007/978-3-642-23354-8_4) and [Chapter 5](https://link.springer.com/chapter/10.1007/978-3-642-23354-8_5). The [author preprint](https://arxiv.org/pdf/1104.5242v2) provides the accessible text used to check the frequency convention, coefficient matrices and thermal relation. Section numbers in the left column always refer to the printed book.

## Translate the notation

### States, maps and time

The system state is a positive matrix $`\rho`$ of trace one. In the energy basis, $`\rho_{ii}`$ is the probability of finding level $`i`$ occupied. An off-diagonal element $`\rho_{ij}`$ records phase-sensitive coherence between levels $`i`$ and $`j`$. A channel maps an input state to an output state and remains physically valid when the input is entangled with an untouched reference.

The anchor's system is labelled $`A`$ and its bath $`B`$. Here the evolving system has four levels, and a separate reference is introduced only when studying channel entanglement. The reference is not the thermal bath.

A fixed generator $`\mathcal L`$ determines the channel

```math
\Phi_t=e^{t\mathcal L},\qquad
\frac{d\rho}{dt}=\mathcal L(\rho),\qquad
\Phi_{t+s}=\Phi_t\circ\Phi_s.
```

The last equality means that evolving for two successive intervals is equivalent to evolving for their combined duration. This semigroup identity is different from the communication assumption of independent channel uses: a many-use capacity protocol requires independently implemented copies of the same channel.

Project variables are dimensionless:

```math
H_{\mathrm{phys}}=E_0H,\qquad
H=\operatorname{diag}(4,2,-4,-2),\qquad
\beta=\beta_{\mathrm{phys}}E_0,\qquad
t=\kappa t_{\mathrm{phys}}.
```

Here $`E_0`$ fixes the energy unit and $`\kappa`$ the dissipative rate unit. A time quoted in the project becomes a physical duration after division by $`\kappa`$. The two scales are independent. The channel formulas use the interaction picture, with the specified free Hamiltonian evolution removed.

### Positive frequency has the opposite sign

The anchor's decomposition uses lowering-positive eigenoperators. In its preprint §6.2.1,

```math
[H_A,A_k(\omega)]=-\omega A_k(\omega).
```

This project labels a matrix unit by its energy change:

```math
F_{ij}=|i\rangle\langle j|,\qquad
[H,F_{ij}]=(E_i-E_j)F_{ij}.
```

Thus positive project frequency means **raising** energy. For the same operator, the source and project frequency labels have opposite signs after expressing energies in the same units. For example, $`F_{01}`$ takes level 1 of energy 2 to level 0 of energy 4. Its project frequency is $`+2`$; it belongs to the source's frequency-$`-2`$ sector. The notation $`E_{ij}`$ in [Exact thresholds](../science/exact_thresholds.md) denotes the same matrix unit as $`F_{ij}`$ here.

For a positive project gap $`\omega`$, the scalar thermal factors are

```math
\gamma_{\uparrow}=e^{-\beta\omega/2},\qquad
\gamma_{\downarrow}=e^{+\beta\omega/2},\qquad
\frac{\gamma_{\uparrow}}{\gamma_{\downarrow}}=e^{-\beta\omega}.
```

Excitation is suppressed relative to relaxation at positive inverse temperature. This is the sign-translated KMS pairing from the anchor's thermal discussion, not a reversed detailed-balance condition.

### Bath matrices and the Hamiltonian correction

The project's block convention is

```math
\mathcal K[C;\mathbf F](\rho)
=\sum_{a,b}C_{ab}
\left(F_a\rho F_b^\dagger
-\frac12\{F_b^\dagger F_a,\rho\}\right).
```

The positive matrix $`C`$ contains both individual transition rates and correlations between pathways. In the source's coefficient formula, the first and second operator indices are ordered oppositely. The project uses real symmetric blocks, so that transpose does not change their numerical entries; the frequency-sign change still matters.

The source also separates dissipative coefficients from the Lamb-shift Hamiltonian. The project specifies the latter independently. A diagonal Hamiltonian correction can commute with $`H`$ while failing to commute with a coherence-transfer block. Such a correction cannot automatically be removed as a harmless output unitary; the exact formulas use [the stated Hamiltonian assumptions](../science/model.md#the-hamiltonian-part).

## A worked coherence-transfer example

This example uses the actual generator at $`\beta=0`$. It shows what populations miss before introducing entanglement with a reference.

The two decays $`0\to3`$ and $`1\to2`$ each release energy 6. Their jump operators are $`F_{30}`$ and $`F_{21}`$. If the bath cannot completely distinguish these alternatives, coherence between levels 0 and 1 can become coherence between levels 3 and 2. Their bath block is

```math
C_6(\eta)=2\begin{pmatrix}1&\eta\\\eta&1\end{pmatrix},
\qquad 0\leq\eta\leq1.
```

Its eigenvalues are $`2(1+\eta)`$ and $`2(1-\eta)`$, so all displayed choices give a positive coefficient matrix. The diagonal entries stay at 2; the shared-path terms change with $`\eta`$.

The matrix-unit multiplication rule is $`F_{ij}F_{k\ell}=\delta_{jk}F_{i\ell}`$, where $`\delta_{jk}`$ is one for equal indices and zero otherwise. One cross term therefore acts as

```math
2\eta F_{30}F_{01}F_{12}=2\eta F_{32}.
```

It transfers a coherence. On a diagonal input $`F_{kk}`$, the same cross map vanishes for every $`k`$. The cross anticommutator products also vanish because these transitions have different sources and different targets. Consequently this term changes no population rate. The reverse processes supply the reverse coherence transfer.

Choose the valid initial state

```math
\rho(0)=\frac{I_4}{4}+\frac18(F_{01}+F_{10}).
```

Its eigenvalues are $`3/8,1/8,1/4,1/4`$, so it is positive and normalized. All four populations are $`1/4`$ and remain so: this is the stationary population distribution at $`\beta=0`$, and coherences do not feed into populations in this model.

Let $`x(t)=\rho_{01}(t)`$ and $`y(t)=\rho_{32}(t)`$. The full generator, including the other fixed jumps, gives

```math
\frac{d}{dt}\begin{pmatrix}x\\y\end{pmatrix}
=\begin{pmatrix}-10&2\eta\\2\eta&-10\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix},
\qquad
x(0)=\frac18,\quad y(0)=0.
```

Adding and subtracting the two equations gives decay rates $`10-2\eta`$ and $`10+2\eta`$ for $`x+y`$ and $`x-y`$. The resulting solution is

```math
x(t)=\frac18e^{-10t}\cosh(2\eta t),\qquad
y(t)=\frac18e^{-10t}\sinh(2\eta t).
```

At $`\eta=0`$ no coherence reaches levels 3 and 2. For every $`\eta>0`$ and $`t>0`$, $`y(t)>0`$, even though every population is still $`1/4`$. A measurement of the Hermitian observable $`X_{23}=F_{23}+F_{32}`$ has expectation

```math
\langle X_{23}\rangle_t
=2\operatorname{Re}y(t)
=\frac14e^{-10t}\sinh(2\eta t).
```

This expression uses the interaction picture; experimentally the corresponding quadrature is aligned with, or corrected for, the known free Hamiltonian phase. Population measurements cannot distinguish these evolutions, while this coherence measurement can.

Two distinctions matter. The jumps in this calculation have energy gap 6, whereas the coherences they connect both have frequency 2. Jump frequency and coherence frequency describe different objects. Also, the fixed diagonal damping coefficient 10 does not fix the full decay of $`x(t)`$: transfer back from $`y(t)`$ changes it. The same changed eigenmodes enter the project's multipliers $`u`$ and $`v`$.

This is a mechanism example, not a proof of bound entanglement. It involves one system and no reference. The channel-level conclusion requires the further steps below.

## From the generator to the entanglement theorem

The selected source route explains the dynamical framework. The repository supplies the following proof obligations for its particular generator. Primary research citations credit their established ingredients; they do not add further educational anchors.

1. **Prove the full matched thermal model.** [Model](../science/model.md) specifies all frequency blocks, proves that every population trajectory is independent of interference, checks GNS detailed balance, and proves uniqueness of the faithful stationary state. Thermal stationarity alone is not substituted for quantum detailed balance.

2. **Turn a channel into a reference–system state.** Keep one half of a maximally entangled pair and evolve the other:

   ```math
   |\Omega_4\rangle=\frac12\sum_{j=0}^{3}|j,j\rangle,
   \qquad J(\Phi)=(\operatorname{id}_4\otimes\Phi)
   (|\Omega_4\rangle\langle\Omega_4|).
   ```

   This normalized Choi state tests a channel with an untouched reference. The Choi criterion for complete positivity and the equivalence between separable Choi states and measure-and-prepare channels are [primary ingredients credited here](../references/RELATED_WORK.md#choi-states-ppt-and-entanglement-breaking-channels).

3. **Distinguish PPT from separability.** Partial transpose transposes only the output indices of $`J`$. Positivity after that operation is necessary for separability, but in dimension $`4\times4`$ it is not sufficient. [Exact thresholds](../science/exact_thresholds.md#2-exact-ppt-criterion) computes the complete partial-transpose spectrum. The [Breuer–Hall positive map](../references/RELATED_WORK.md#the-breuerhall-witness) detects entanglement that survives this PPT test.

4. **Prove both sides of the EB boundary.** A negative witness proves that a channel is not entanglement breaking. The converse needs a separate argument: the project constructs [twenty measure-and-prepare components](../science/exact_thresholds.md#4-a-constructive-eb-decomposition-at-the-boundary) whose convex mixture is the boundary channel. With $`r=e^{-8t}`$, $`u=e^{-(10-2\eta)t}`$ and $`v=e^{-(10+2\eta)t}`$, the two exact conditions at $`\beta=0`$ are

   ```math
   \Phi_{\eta,t}\text{ is PPT}\iff r+2u+2v\leq1,
   \qquad
   \Phi_{\eta,t}\text{ is EB}\iff r+4u\leq1.
   ```

   Their equality times are $`t_P`$ and $`t_E`$. The full-interpolation proof is supplied locally; the [known symplectic geometry of the endpoint](../references/RELATED_WORK.md#static-symplectic-channel-geometry) is credited separately.

5. **Connect the inequalities to communication.** [Operational meaning](../science/operational_meaning.md) projects the pre-PPT Choi state onto a fixed two-qubit subspace, yielding an entangled conditional state. Standard purification and hashing then give a positive two-way assisted rate. Once the channel is PPT, an adaptive protocol using independent calls and local operations with classical communication preserves PPT and cannot produce reliable maximally entangled pairs. The [primary distillation and binding-channel results](../references/RELATED_WORK.md#distillability-and-two-way-assisted-quantum-communication) supply the established ingredients. The proof does not presume that every higher-dimensional NPT state is distillable.

6. **Continue to positive temperature with a controlled bound.** [Thermal extension](../science/thermal_extension.md) starts from strict PPT and witness margins, bounds the channel change, and certifies a point at $`\beta=10^{-4}`$ by rational inequalities. This establishes persistence; it does not supply exact finite-temperature thresholds.

Together these steps show why an unchanged population generator need not fix the lifetime of channel entanglement. For every $`\eta>0`$ at $`\beta=0`$, $`t_P\lt t_E`$: throughout $`[t_P,t_E)`$ the channel has zero two-way assisted quantum capacity but an entangled Choi state. The [weak-interference law](../science/exact_thresholds.md#5-threshold-ordering-and-weak-interference-behavior) determines how that interval opens.

## Physical scope

The bridge uses the same assumptions as the scientific pages:

- **Exact repeated gaps.** The four energy levels are distinct, but some transitions share a Bohr frequency. Their cross terms survive secularization because their frequencies agree. Splitting those gaps before taking the fully secular limit is a different model-building operation.
- **Specified equilibrium generators.** The KMS factors define a valid thermal family. Varying $`\beta`$ is not claimed to change only the temperature of one fixed microscopic bath with unchanged couplings and spectral density. A platform-specific bath implementation is not provided.
- **Fixed Hamiltonian treatment.** Additional Lamb shifts require the commutation, compensation or perturbation conditions stated in the model. Commuting with the bare Hamiltonian alone is insufficient.
- **Precisely matched observables.** Population dynamics and matrix-unit self-damping are fixed. Full coherence eigenmodes are not. At infinite temperature the dissipative spectral gap is also fixed, but the full Liouvillian spectrum changes.
- **Stationary equilibrium, possibly transient relaxation.** Detailed balance gives zero stationary currents. It does not forbid transient heat flow from a nonequilibrium initial state. The uniform-population worked example is a special $`\beta=0`$ preparation.
- **Stated communication resources.** The capacity statement starts with no shared entanglement and permits independent uses, arbitrary local processing and free two-way classical communication. It determines the sign of that capacity for this family, not its positive numerical value or the unassisted or private capacity.
- **Separate temperature claims.** Exact boundaries and arbitrary-weak-interference opening are proved at $`\beta=0`$. The positive-temperature certificate proves a strict example and nearby admissible generators; it is not a uniform finite-temperature phase diagram.

The [common milestone map](MILESTONES.md) joins these foundations and project-specific steps into a single scientific story. Detailed proofs remain in the linked scientific pages, and the [verification suite](../verification/README.md) checks their finite-dimensional implementation.
