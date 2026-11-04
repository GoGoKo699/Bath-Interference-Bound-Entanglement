# Related work and attribution

This project studies how interference between equal-frequency transition paths changes the entanglement lifetimes of an equilibrium quantum channel. Its object is the normalized reference–system Choi state of a four-level Davies semigroup. The comparison holds the **entire classical population generator** fixed while changing the off-diagonal entries of two bath correlation matrices. All bibliographic keys below are defined in [references.bib](references.bib). Source versions were checked on 4 November 2026.

## The contribution being distinguished

For the Hamiltonian $`H=\operatorname{diag}(4,2,-4,-2)`$, the interference parameter $`0\leq\eta\leq1`$ changes coherence transfer between transition operators at repeated Bohr frequencies. It preserves every population trajectory and the diagonal attenuation coefficients in the energy-coherence basis. The coherence eigenmode decay rates do change.

At inverse temperature $`\beta=0`$, set

```math
r=e^{-8t},\qquad u=e^{-(10-2\eta)t},\qquad
v=e^{-(10+2\eta)t},\qquad b=e^{-12t}.
```

The exact channel conditions established for this trajectory are

```math
\Phi_t\text{ is PPT}\quad\Longleftrightarrow\quad r+2u+2v\leq1,
\qquad
\Phi_t\text{ is entanglement breaking}\quad\Longleftrightarrow\quad r+4u\leq1.
```

The first condition fixes the exact extinction time of positive two-way assisted quantum capacity, using a Schmidt-rank-two negative-partial-transpose vector before that time. The second uses a constructive convex decomposition into measure-and-prepare channels at the boundary. Thus the interval between the thresholds is a channel-level interval with zero two-way assisted quantum capacity and an entangled Choi state. The width opens linearly in $`\eta`$ from the resolved-transition endpoint, whereas the PPT time changes only quadratically. These exact statements concern $`\beta=0`$; a separate strict-interior certificate establishes persistence at an explicit positive inverse temperature.

The ingredients below are inherited. The specific contribution is their combination with the matched equilibrium generator, the full interference interpolation, and its exact operational boundaries. It is not a claim of the first PPT entangled state, binding-entanglement channel, transient bound-entangled regime, or eventual entanglement-breaking semigroup.

## Static symplectic channel geometry

**Sean Prudhoe, _Entanglement Breaking Structure of Cartan-Covariant Quantum Channels_**, [arXiv:2501.03959v3](https://arxiv.org/abs/2501.03959v3), revised 7 August 2026; first posted 7 January 2025 (`prudhoe2026cartan`). Section 3 analyzes symplectic-covariant channels and their Choi, PPT and separability geometry. The fully interfering endpoint here, $`\eta=1`$, has the corresponding five- and ten-dimensional traceless operator sectors. Its threshold calculation is therefore an application of known static geometry. Prudhoe also analyzes other Cartan covariance groups; the present construction does not claim that every symmetry classification is new or irrelevant.

**Sang-Jun Park, _$k$-Positivity and high-dimensional bound entanglement under symplectic group symmetries_**, [arXiv:2602.09860v3](https://arxiv.org/abs/2602.09860v3), revised 10 March 2026; first posted 10 February 2026 (`park2026symplectic`). Theorem 4.1 gives exact PPT and separability regions in the two-real-parameter symplectic families. The work also develops stronger positive-map and Schmidt-number results. These results are direct antecedents for the endpoint cone and the use of symplectic witnesses.

For $`0\lt \eta\lt 1`$ and $`t>0`$, this project's nonidentity Pauli eigenvalues have multiplicities $`1,4,4,6`$, splitting both of the symplectic sectors. Consequently the two-parameter symplectic classification does not itself prove separability of the interior interpolation. The project supplies that step by an explicit mixture of singleton Pauli measure-and-prepare channels and dephasing channels associated with maximal commuting triples. The novelty claim rests on this full trajectory and its bath realization, rather than on a new interpretation of the known endpoint cone. This comparison does not assert an exhaustive classification of all other covariant channel families.

## Related project: Current-Induced Bound Entanglement

The closely related project [**Current-Induced Bound Entanglement**](https://github.com/GoGoKo699/Current-Induced-Bound-Entanglement/tree/be54aa938a7263b43db79a9afd99a245881b2a32) is compared at the fixed commit `be54aa938a7263b43db79a9afd99a245881b2a32` (`currentinduced2026`). Its relevant sources are the pinned [model](https://github.com/GoGoKo699/Current-Induced-Bound-Entanglement/blob/be54aa938a7263b43db79a9afd99a245881b2a32/science/model.md), [reversible-case proof](https://github.com/GoGoKo699/Current-Induced-Bound-Entanglement/blob/be54aa938a7263b43db79a9afd99a245881b2a32/science/reversible_proof.md), and [limitations](https://github.com/GoGoKo699/Current-Induced-Bound-Entanglement/blob/be54aa938a7263b43db79a9afd99a245881b2a32/science/limitations.md).

Its equality theorem assumes resolved rank-one population jumps

```math
J_{i\leftarrow j}=\sqrt{q_{ij}}\,|i\rangle\langle j|,
```

together with a diagonal Hamiltonian, real Hermitian diagonal noise, and faithful classical detailed balance. In that class, PPT and entanglement-breaking thresholds coincide. Its current-driven construction separates the thresholds by departing from classical detailed balance. The limitations explicitly exclude generic Davies generators with unresolved equal-frequency transitions that transfer coherence between transition operators.

The present family enters precisely that excluded class when $`\eta>0`$. It retains quantum detailed balance while introducing bath correlations within repeated-frequency blocks. The resolved endpoint $`\eta=0`$ is consistent with the earlier equality theorem. There is no contradiction: the hypotheses differ. Here the full classical generator is independent of $`\eta`$, so stationary currents and all population trajectories are identical across the comparison. The mechanism for the gap is coherence transfer caused by bath-path interference, rather than stationary classical irreversibility. The relation to this predecessor is part of the scientific attribution, not merely a bibliographic similarity.

## Noise-induced bound entanglement and eventual channel behavior

| Primary source | Established result relevant here | Distinction of the present trajectory |
|---|---|---|
| Elias Amselem, Muhammad Sadiq and Mohamed Bourennane, [Scientific Reports **3**, 1966 (2013)](https://doi.org/10.1038/srep01966), `amselem2013pauli` | An experimental correlated Pauli-noise construction takes products of Bell states into a multipartite bound-entangled regime. | The four-party separability restrictions differ from bipartite reference(4)–system(4) Choi entanglement. The present claim concerns a detailed-balanced semigroup and its matched transition-resolution control. |
| Gurvir Singh, Saptarshi Roy and Arvind, [Physical Review A **112**, 052424 (2025)](https://doi.org/10.1103/vpq9-691b), [arXiv:2503.12694](https://arxiv.org/abs/2503.12694), `singh2025gaussian` | Four-mode Gaussian state evolution under thermal noise can pass through a transient bound-entangled phase before separability. | Thermal noise producing such an intermediate phase is already known. Here the bounds classify a finite-dimensional channel through its Choi state, with exact thresholds and the complete classical generator matched. |
| Eric P. Hanson, Cambyse Rouzé and Daniel Stilck França, [Annales Henri Poincaré **21**, 1517–1571 (2020)](https://doi.org/10.1007/s00023-020-00906-4), `hanson2020eventual` | General structure and time bounds for eventual entanglement breaking in Markovian dynamics. | Eventual entanglement breaking of this primitive semigroup is inherited; the target is the exact earlier PPT boundary and its separation from the EB boundary. |
| Krzysztof Szczygielski and Dariusz Chruściński, [Journal of Physics A **57**, 495206 (2024)](https://doi.org/10.1088/1751-8121/ad9368), [arXiv:2407.16583v2](https://arxiv.org/abs/2407.16583v2), `szczygielski2024eventual` | Eventual entanglement breaking for broad divisible dynamics, including faithful stationary semigroups; PPT and EB arrival-time comparisons are discussed. | The present calculation supplies a particular exact equality/separation law under bath interference, rather than a new general eventual-EB principle. |

These sources establish that neither equilibrium noise nor loss of distillability is generally equivalent to immediate loss of every form of entanglement. What the present comparison isolates is a change in channel-level entanglement lifetimes that cannot be diagnosed from the classical population generator.

## Foundational results used in the proofs

### Equilibrium generators

The weak-coupling Markovian framework is due to [E. B. Davies, _Markovian master equations_ (1974)](https://doi.org/10.1007/BF01608389), `davies1974markovian`. Quantum detailed balance for non-Hamiltonian semigroups has an early systematic formulation in [Robert Alicki (1976)](https://doi.org/10.1016/0034-4877(76)90046-X), `alicki1976balance`. The positive Kossakowski blocks, frequency decomposition and KMS pairing used here belong to this established framework. This repository specifies a finite-dimensional generator within that framework; it does not claim a new weak-coupling-limit theorem.

### Choi states, PPT and entanglement-breaking channels

[Man-Duen Choi (1975)](https://doi.org/10.1016/0024-3795(75)90075-0), `choi1975completely`, supplies the completely-positive-map criterion in terms of the associated matrix. [Asher Peres (1996)](https://doi.org/10.1103/PhysRevLett.77.1413), `peres1996separability`, supplies the partial-transpose separability test. [Michael Horodecki, Peter W. Shor and Mary Beth Ruskai (2003)](https://doi.org/10.1142/S0129055X03001709), `horodecki2003eb`, establish the equivalent descriptions of entanglement-breaking channels, including separable Choi states and measure-and-prepare representations. The project's explicit separable decomposition is an application of this channel criterion.

### The Breuer–Hall witness

The map used to certify PPT entanglement is the established positive map

```math
\mathcal B(X)=\operatorname{tr}(X)I-X-VX^{\mathsf T}V^\dagger,
\qquad V^{\mathsf T}=-V,
```

up to an immaterial positive normalization. Its attribution is to [Heinz-Peter Breuer, Physical Review Letters **97**, 080501 (2006)](https://doi.org/10.1103/PhysRevLett.97.080501), `breuer2006criterion`, and [William Hall, Journal of Physics A **39**, 14119 (2006)](https://doi.org/10.1088/0305-4470/39/45/020), `hall2006indecomposability`. Neither the map nor the fact that it detects PPT entanglement is new here. Its negative eigenvalue provides necessity of the EB boundary; the constructive measure-and-prepare decomposition provides the separate sufficiency proof.

### Distillability and two-way assisted quantum communication

The proof of positive two-way assisted capacity before the PPT time uses a **specific Schmidt-rank-two negative vector**, yielding an entangled two-qubit projection of the Choi state. It does not assume that every higher-dimensional NPT state is distillable. Distillability of every entangled two-qubit state follows from [Michał, Paweł and Ryszard Horodecki (1997)](https://doi.org/10.1103/PhysRevLett.78.574), `horodecki1997distillation`. Recurrence purification and the connection to reliable quantum communication are established by [Bennett, Brassard, Popescu, Schumacher, Smolin and Wootters (1996)](https://doi.org/10.1103/PhysRevLett.76.722), `bennett1996purification`; the hashing and channel-coding framework is developed by [Bennett, DiVincenzo, Smolin and Wootters (1996)](https://doi.org/10.1103/PhysRevA.54.3824), `bennett1996mixed`.

PPT states cannot be distilled to singlets by LOCC, as shown by [Michał, Paweł and Ryszard Horodecki (1998)](https://doi.org/10.1103/PhysRevLett.80.5239), `horodecki1998bound`. The stronger PPT-preserving-operation framework is developed in [Eric M. Rains (2001)](https://doi.org/10.1109/18.959270), `rains2001semidefinite`. For a channel with PPT Choi state, $`T\circ\Phi`$ is completely positive. Repeated uses of that channel, interleaved with LOCC, preserve PPT across the communicating parties and therefore cannot distill singlets. This establishes the zero-capacity side of the threshold without equating the capacity of an arbitrary channel to the distillable entanglement of its Choi state.

The broader phenomenon of zero quantum communication capability together with the ability to distribute bound entanglement was already formulated by [Paweł, Michał and Ryszard Horodecki, _Binding entanglement channels_, Journal of Modern Optics **47**, 347–354 (2000)](https://doi.org/10.1080/09500340008244047), [arXiv:quant-ph/9904092](https://arxiv.org/abs/quant-ph/9904092), `horodecki2000binding`. The project locates the beginning and end of that behavior along its specified matched equilibrium trajectory; it does not introduce the phenomenon itself.

## Scope of the comparison

The exact arbitrary-weak-interference opening law is proved at $`\beta=0`$. Positive-temperature persistence is certified at a strict interior point; the same weak-interference law at fixed positive temperature is not established. Repeated Bohr frequencies and the chosen signs of bath correlations are part of the model. Splitting those gaps and then applying a fully secular approximation changes which interference terms survive. Detailed balance implies zero stationary currents, not zero transient heat flow for every initial state. The surviving entanglement is between a reference and the evolved system; no entanglement creation from an initially unentangled reference–system state is asserted.

Within these limits, the supported distinction is an exact separation of operational entanglement lifetimes caused by bath-path interference while population dynamics remain identical. The comparisons above bound that claim and identify the established tools on which it depends; they are not an exhaustive priority certification for every form of noisy bound entanglement.
