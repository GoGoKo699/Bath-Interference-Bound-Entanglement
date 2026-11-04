# The 30-milestone understanding map

This project asks how a thermal bath can erase the ability to communicate quantum information before its channel becomes equivalent to measuring an input and preparing an output. Its controlled variable is interference between equal-frequency transition pathways. The population dynamics stay fixed, while coherence transfer changes the lifetime of entanglement between the system and an untouched reference.

The map contains **exactly 30 project-defined milestones** in two phases:

| Phase | Milestones | Scientific purpose |
|---|---|---|
| Background/preliminaries | M01–M14: 14 milestones | Build the state, channel, thermal-generator, and entanglement languages into one framework for comparing noise processes. |
| Narrative/innovation | M15–M30: 16 milestones | Follow the specified bath mechanism through its exact proofs, operational consequences, thermal persistence, and final interpretation. |

The allocation follows the project's connection between two subjects: equilibrium open-system dynamics and the entanglement properties of a channel with a reference. The background phase needs both languages, including the distinction between stationarity and detailed balance and the distinction between PPT and entanglement breaking. The narrative phase gives more space to how these ingredients combine into the new result. Within each phase, individual objects and local arguments lead to an integrated account; M14 and M30 are the respective synthesis points. Specialist calculations remain in the linked scientific pages.

## The selected anchor and the source convention

The single educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_ (2012)**, [Springer DOI 10.1007/978-3-642-23354-8](https://doi.org/10.1007/978-3-642-23354-8). The abbreviation **RH** below refers to this book. Section numbers always mean the **printed 2012 book**, whose numbering differs from the accompanying preprint. The [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md#source-and-edition) records the edition and the [reading route](RIVAS_HUELGA_BRIDGE.md#reading-route) translates the section numbers.

RH supplies the open-systems framework and assumes some quantum-mechanical background. The map therefore makes the elementary state and channel targets explicit. Its source pointers distinguish supporting textbook context from the repository's own derivations. In particular, the Choi/PPT comparisons, Breuer–Hall witness, constructive EB decomposition, two-way-capacity proof, and quantitative thermal certificate are supplied by the project and its attributed research ingredients. The [related-work account](../references/RELATED_WORK.md) retains those primary research sources without adding another educational anchor.

Each milestone records a central question, an understanding target, earlier-ID dependencies and its role in the story, a conceptual connection, and both anchor and canonical project pointers. Phase membership is given by the containing phase heading. These targets describe the science of the project and are independent of any reader's assessment history.

## Background/preliminaries — M01–M14

### M01 — A system, a state, and an untouched reference

**Central question.** Whose state changes when a noisy channel acts on only one part of a larger system?

**Understanding target.** Interpret a density operator as a positive, unit-trace matrix encoding the probabilities of quantum observations. Distinguish the noisy four-level system from an untouched reference and identify the bipartition across which entanglement is discussed. Correlations between these two parties are different from correlations between two internal qubits used to label the four levels.

**Dependencies and story role.** Earlier IDs: none. Establishes the objects and the system–reference perspective from which the entire project is described.

**Conceptual connection.** A local noise process can change correlations with another system even when its own populations look ordinary; this makes a reference necessary for the later channel comparison.

**Sources.** **Anchor:** [RH §3.1, dynamical-map setting](RIVAS_HUELGA_BRIDGE.md#reading-route), as context rather than a complete elementary state course. **Project:** [Definitions and principal result](../science/README.md#definitions-and-principal-result) and the preparation at the start of [the local projection](../science/operational_meaning.md#1-a-local-projection-before-ppt-onset).

### M02 — Why a physical channel must tolerate a reference

**Central question.** Why is positivity on the system alone insufficient to describe physical noise?

**Understanding target.** Explain trace preservation as preservation of total probability and complete positivity as positivity when the channel acts beside an arbitrary untouched reference. Distinguish the channel, which maps input states to output states, from a particular state produced by one chosen input.

**Dependencies and story role.** Earlier IDs: M01. Turns the system–reference setting into the physical requirements on a noise map.

**Conceptual connection.** Complete positivity links reduced dynamics to the same reference-system viewpoint later used by the Choi construction and entanglement tests.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route). **Project:** [Scientific definitions](../science/README.md#definitions-and-principal-result) and [the Davies generator](../science/model.md#the-davies-generator).

### M03 — Measurement and preparation as a complete channel description

**Central question.** What does it mean for all of a channel's output to be reproducible by a measurement result and a prepared state?

**Understanding target.** Describe a measure-and-prepare channel as a measurement with classical outcomes followed by outcome-dependent state preparation. Understand why it destroys entanglement with every reference, and why checking a single separable output is insufficient to establish this property for a channel.

**Dependencies and story role.** Earlier IDs: M01, M02. Introduces the later endpoint of the project before discussing a time-dependent route to it.

**Conceptual connection.** An operational realization supplies more than a negative entanglement test: it can prove the channel is entanglement breaking for every input.

**Sources.** **Anchor:** [RH §3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) supports the completely positive map framework; the EB characterization and constructions come from the project. **Project:** [Definitions](../science/README.md#definitions-and-principal-result) and [two explicit measure-and-prepare channels](../science/exact_thresholds.md#41-two-explicit-measure-and-prepare-channels).

### M04 — A generator determines a continuous noise process

**Central question.** How does a time-independent generator specify a channel at every duration?

**Understanding target.** Interpret the semigroup relation as composition of successive durations of the same noise and the exponential of a generator as its continuous-time channel. Identify the Hamiltonian and dissipative parts of a Lindblad generator, and distinguish a decay rate from a channel multiplier at a specified time.

**Dependencies and story role.** Earlier IDs: M02. Moves from individual channels to the dynamical family whose entanglement properties change with duration.

**Conceptual connection.** The semigroup structure supplies both the exact solution method and the reason an EB channel remains EB at later times.

**Sources.** **Anchor:** [RH §§1.2–1.3, §3.5, and §4.2](RIVAS_HUELGA_BRIDGE.md#reading-route). **Project:** [Conventions and scales](../science/model.md#conventions-and-scales), [the generator](../science/model.md#the-davies-generator), and the composition argument in [the EB sufficiency proof](../science/exact_thresholds.md#44-nonnegative-weights).

### M05 — Energy levels and transition frequencies are different data

**Central question.** How can distinct energy levels still support transitions of the same frequency?

**Understanding target.** Read a transition operator as moving amplitude from one energy eigenstate to another and its Bohr frequency as the energy difference. Distinguish level degeneracy from repeated gaps. Understand why working in an interaction picture can remove a specified commuting Hamiltonian evolution without removing the dissipative effect.

**Dependencies and story role.** Earlier IDs: M01, M04. Introduces the frequency organization that makes the bath mechanism possible.

**Conceptual connection.** The bath can correlate two different transitions while remaining within one exactly resolved frequency sector.

**Sources.** **Anchor:** [RH Chapter 2 and §5.2.1](RIVAS_HUELGA_BRIDGE.md#reading-route), for Hamiltonian evolution and interaction decomposition. **Project:** [Conventions](../science/model.md#conventions-and-scales), [the Hamiltonian part](../science/model.md#the-hamiltonian-part), and [repeated gaps](../science/model.md#bath-interpretation-and-the-role-of-repeated-gaps).

### M06 — Bath correlations are coefficients of a physical generator

**Central question.** How can correlations between jump pathways be changed without making the dynamics unphysical?

**Understanding target.** Interpret a positive Kossakowski matrix as a valid combination of Lindblad jumps. Distinguish diagonal coefficients that set individual pathway strengths from off-diagonal coefficients that combine transition amplitudes. Relate a Gram matrix of environment records to whether the bath retains information about which pathway occurred.

**Dependencies and story role.** Earlier IDs: M02, M04, M05. Connects the abstract generator to a local physical control on the environment.

**Conceptual connection.** Complete positivity constrains the allowed interference parameter, while overlap of bath records gives that parameter a physical meaning.

**Sources.** **Anchor:** [RH §§4.2–4.3 and §§5.2.2–5.2.4](RIVAS_HUELGA_BRIDGE.md#reading-route). **Project:** [The coefficient blocks](../science/model.md#the-davies-generator) and [their bath-record interpretation](../science/model.md#bath-interpretation-and-the-role-of-repeated-gaps).

### M07 — Populations, coherence self-damping, and coherence modes

**Central question.** Which aspects of a density matrix are fixed by population rates, and which are not?

**Understanding target.** Distinguish energy-basis populations from off-diagonal coherences. Separate the coefficient of a coherence in its own differential equation from transfer to other coherences and from the decay rates of the resulting eigenmodes. Understand why equal population histories or equal self-damping do not establish equal channels.

**Dependencies and story role.** Earlier IDs: M01, M04, M05, M06. Identifies the dynamical quantities whose equality gives the project a controlled comparison.

**Conceptual connection.** Classical relaxation data describe only one sector of a quantum generator; off-diagonal bath correlations can act in another sector.

**Sources.** **Anchor:** [RH §§4.1–4.2](RIVAS_HUELGA_BRIDGE.md#reading-route), for classical and quantum generator descriptions. **Project:** [What is held fixed](../science/model.md#what-is-held-fixed) and [the worked coherence-transfer example](RIVAS_HUELGA_BRIDGE.md#a-worked-coherence-transfer-example).

### M08 — Thermal rates and a Gibbs stationary state

**Central question.** What makes a pair of upward and downward transition rates compatible with a thermal bath?

**Understanding target.** Relate the Gibbs weights to the ratio of reverse transition rates through the KMS condition. Track the chosen sign of a Bohr frequency so that energy-raising and energy-lowering processes receive the correct weights. Distinguish a specified family of KMS-compatible rates from changing the temperature of one fixed microscopic reservoir.

**Dependencies and story role.** Earlier IDs: M05, M06, M07. Adds the equilibrium constraint to the admissible bath-correlation model.

**Conceptual connection.** Thermal stationarity restricts rate ratios but does not by itself remove correlations between equal-frequency pathways.

**Sources.** **Anchor:** [RH §§5.2.4 and 5.2.8](RIVAS_HUELGA_BRIDGE.md#reading-route). **Project:** [The thermal generator](../science/model.md#the-davies-generator), [the rate-sign calculation](../science/model.md#gns-detailed-balance-with-the-rate-sign-checked), and [population detailed balance](../science/model.md#the-entire-population-generator).

### M09 — Quantum detailed balance is stronger than stationarity

**Central question.** Why does finding a Gibbs fixed point not finish the equilibrium proof for a quantum generator?

**Understanding target.** Distinguish stationarity of one state, classical detailed balance of populations, and GNS self-adjointness of the Heisenberg dissipator. Understand the Gibbs-weighted inner product and how a frequency jump and its adjoint become partners in that inner product. Separate the symmetric dissipator from the Hamiltonian part.

**Dependencies and story role.** Earlier IDs: M04, M05, M08. Establishes the precise equilibrium condition used by the project.

**Conceptual connection.** A condition on the complete operator dynamics is needed before attributing the later effect to an equilibrium bath rather than merely to equilibrium-looking populations.

**Sources.** **Anchor:** [RH §4.4 and §5.2.8](RIVAS_HUELGA_BRIDGE.md#reading-route) give steady-state and thermal context; the full GNS convention and proof are supplied locally. **Project:** [GNS detailed balance](../science/model.md#gns-detailed-balance-with-the-rate-sign-checked) and the attributed [equilibrium-generator framework](../references/RELATED_WORK.md#equilibrium-generators).

### M10 — Unique relaxation and its slowest decay rate

**Central question.** What must be checked before interpreting a stationary state as the unique long-time destination?

**Understanding target.** Understand primitivity as convergence to a unique full-rank, or faithful, stationary state and recognize how a commuting observable or dark subspace could obstruct it. Interpret the dissipative spectral gap as the smallest nonzero decay rate, while distinguishing that one number from the complete spectrum and from an entanglement lifetime.

**Dependencies and story role.** Earlier IDs: M04, M07, M09. Completes the background description of equilibration without identifying it with entanglement loss.

**Conceptual connection.** Establishing ordinary thermal relaxation excludes hidden stationary quantum sectors as the explanation of the bound-entangled interval.

**Sources.** **Anchor:** [RH §1.3 and §4.4](RIVAS_HUELGA_BRIDGE.md#reading-route). **Project:** [Primitivity](../science/model.md#primitivity-including-maximal-interference) and [the infinite-temperature spectrum](../science/model.md#infinite-temperature-spectrum).

### M11 — A Choi state represents a channel-level entanglement question

**Central question.** How can one bipartite operator determine whether a channel is PPT or entanglement breaking?

**Understanding target.** Explain the normalized Choi construction by sending half of a maximally entangled state through the channel. Distinguish positivity of the Choi state, positivity after output partial transpose, and separability. Understand the corresponding channel statements, including the requirement that EB destroy entanglement for every input and reference.

**Dependencies and story role.** Earlier IDs: M01, M02, M03. Introduces the bridge from generator dynamics to the global property of the noisy channel.

**Conceptual connection.** The reference used to define complete positivity also provides a finite representation in which the two entanglement thresholds can be compared.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) supply dynamical-map and complete-positivity context; the Choi/PPT/EB comparison used here is supplied by the project. **Project:** [Scientific definitions](../science/README.md#definitions-and-principal-result), [the Choi construction](../science/exact_thresholds.md#2-exact-ppt-criterion), and [the attributed equivalences](../references/RELATED_WORK.md#choi-states-ppt-and-entanglement-breaking-channels).

### M12 — Entanglement beyond the PPT criterion

**Central question.** How can a state have positive partial transpose and still be entangled?

**Understanding target.** Recognize PPT as a necessary condition for separability whose sufficiency depends on dimension. Understand why a positive map applied to one side preserves positivity for separable states, and why a negative result supplies an entanglement certificate even when partial transpose is positive. Keep the absence of a detected violation separate from a proof of separability.

**Dependencies and story role.** Earlier IDs: M02, M03, M11. Supplies the logical distinction that permits two different entanglement boundaries.

**Conceptual connection.** Necessity can come from a witness, whereas sufficiency needs a separate argument such as an explicit separable realization.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) support positivity versus complete positivity; they are not the source of this project's bound-entanglement proof. **Project:** [The positive-map argument](../science/exact_thresholds.md#3-an-entanglement-witness-up-to-the-eb-boundary) and [witness attribution](../references/RELATED_WORK.md#the-breuerhall-witness).

### M13 — Distillable entanglement and two-way quantum communication

**Central question.** What distinguishes surviving entanglement from entanglement that can support a reliable quantum communication rate?

**Understanding target.** Describe distillation as local processing with classical communication that converts many noisy shared pairs into nearly ideal entangled pairs. Specify independent channel uses, initially unentangled laboratories, and unlimited two-way classical communication. Distinguish positive two-way-assisted quantum capacity from an entangled output, an unassisted capacity claim, or a claim about private communication.

**Dependencies and story role.** Earlier IDs: M01, M02, M03, M11, M12. Introduces the operational question associated with the earlier threshold.

**Conceptual connection.** A channel can fail to distribute distillable entanglement while still failing to admit a measure-and-prepare description.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) supply the channel framework only; the communication and distillation arguments are repository-supplied. **Project:** [Operational definitions](../science/operational_meaning.md), [scope of the capacity claims](../science/operational_meaning.md#4-scope-of-the-operational-conclusions), and [their primary attribution](../references/RELATED_WORK.md#distillability-and-two-way-assisted-quantum-communication).

### M14 — The complete framework for a controlled noise comparison

**Central question.** What must be specified to compare two equilibrium noise processes and interpret different entanglement lifetimes?

**Understanding target.** Assemble the system–reference split, admissible generator, thermal condition, matched observables, time and energy scales, and channel-level entanglement criteria into one comparison. Identify the distinct proof obligations: validity of the dynamics, equality of the advertised relaxation data, separate PPT and EB boundaries, and an operational interpretation under stated communication resources.

**Dependencies and story role.** Earlier IDs: M03, M04, M07, M08, M09, M10, M11, M12, M13. Integrates the background phase into the precise problem that the narrative will resolve.

**Conceptual connection.** Open-system equilibration and channel entanglement become parts of one question rather than independent descriptions of noise.

**Sources.** **Anchor:** [RH §§3.1–3.2, §§4.1–4.4, and §§5.2.1–5.2.4, 5.2.8](RIVAS_HUELGA_BRIDGE.md#reading-route), selected for the dynamical framework. **Project:** [Scientific overview](../science/README.md), [physical interpretation](../science/interpretation.md), and [the bridge from generator to entanglement](RIVAS_HUELGA_BRIDGE.md#from-the-generator-to-the-entanglement-theorem).

## Narrative/innovation — M15–M30

### M15 — The concrete four-level thermal family

**Central question.** Which Hamiltonian and bath-correlation blocks realize the proposed control within a valid Davies generator?

**Understanding target.** Identify the distinct levels of $`H=\operatorname{diag}(4,2,-4,-2)`$, the repeated gaps at 2 and 6, and the two coefficient blocks with off-diagonal entries of opposite sign proportional to $`\eta`$. Explain why their eigenvalues keep the generator completely positive for $`0\le\eta\le1`$. Track the separate energy scale, dissipative rate, dimensionless time, and dimensionless inverse temperature.

**Dependencies and story role.** Earlier IDs: M04, M05, M06, M08, M14. Begins the narrative with the actual local ingredients rather than an abstract assertion that suitable noise exists.

**Conceptual connection.** The controlled interference parameter belongs to an explicit positive, frequency-resolved thermal generator.

**Sources.** **Anchor:** [RH §§4.2–4.3 and §§5.2.1–5.2.4](RIVAS_HUELGA_BRIDGE.md#reading-route). **Project:** [Conventions and scales](../science/model.md#conventions-and-scales), [the Davies generator](../science/model.md#the-davies-generator), and [notation translation](RIVAS_HUELGA_BRIDGE.md#translate-the-notation).

### M16 — Change coherence transfer while holding relaxation data fixed

**Central question.** Why do the interference terms change the quantum dynamics without changing any population history or coherence self-damping coefficient?

**Understanding target.** Follow how cross terms between disjoint equal-frequency transitions map one off-diagonal matrix unit to another, while their cross anticommutator products vanish. Explain why setting $`\eta=0`$ resolves the pathways and why increasing its magnitude changes their bath-record overlap. Keep the specified relative signs and full coherence-mode changes visible in the matched comparison.

**Dependencies and story role.** Earlier IDs: M06, M07, M15. Establishes the causal control that the later entanglement separation will be attributed to.

**Conceptual connection.** Fixed individual transition strengths can coexist with changed interference because the environment's pathway records carry additional information.

**Sources.** **Anchor:** [RH §§5.2.1–5.2.4](RIVAS_HUELGA_BRIDGE.md#reading-route), for frequency decomposition and correlation coefficients. **Project:** [What is held fixed](../science/model.md#what-is-held-fixed), [bath interpretation](../science/model.md#bath-interpretation-and-the-role-of-repeated-gaps), and [the worked transfer example](RIVAS_HUELGA_BRIDGE.md#a-worked-coherence-transfer-example).

### M17 — Equilibrium and unique relaxation survive interference

**Central question.** Does the controlled interference introduce a hidden departure from equilibrium or a protected stationary sector?

**Understanding target.** Follow the pairing of raising and lowering jumps in the Heisenberg GNS inner product and see why it proves quantum detailed balance, not only Gibbs stationarity. Explain how the two diagonal jumps and the connected transition graph force fixed observables to be scalar, including at maximal interference. Separate absence of stationary currents from possible transient heat flow.

**Dependencies and story role.** Earlier IDs: M08, M09, M10, M15, M16. Verifies the full equilibrium premise of the controlled family before its entanglement consequences are used.

**Conceptual connection.** The bound-entangled stage need not be attributed to driving, circulation of stationary populations, or a nonrelaxing subsystem.

**Sources.** **Anchor:** [RH §4.4 and §5.2.8](RIVAS_HUELGA_BRIDGE.md#reading-route) supply equilibrium context; the GNS and commutant arguments are explicit project proofs. **Project:** [Detailed balance](../science/model.md#gns-detailed-balance-with-the-rate-sign-checked), [primitivity](../science/model.md#primitivity-including-maximal-interference), and [stationary population currents](../science/model.md#the-entire-population-generator).

### M18 — Solve the infinite-temperature dynamics in Pauli sectors

**Central question.** How do the population and coherence blocks lead to an exact channel solution?

**Understanding target.** Connect the two-by-two coherence-transfer blocks to the multipliers $`u`$ and $`v`$, and the remaining sectors to $`r`$ and $`b`$. Understand the Pauli multiplicities $`1,4,4,6`$ and why the complete dissipative gap remains 8 even though several eigenmode rates change. Interpret exponential multipliers as the channel's action on a basis of operators.

**Dependencies and story role.** Earlier IDs: M04, M07, M10, M15, M16, M17. Converts the explicit generator into the finite set of quantities used by both entanglement proofs.

**Conceptual connection.** Diagonalizing the dynamics makes a global property of the channel accessible while showing why population measurements and one relaxation gap cannot settle it.

**Sources.** **Anchor:** [RH §§1.2–1.3 and §4.2](RIVAS_HUELGA_BRIDGE.md#reading-route). **Project:** [Solving the generator](../science/exact_thresholds.md#1-solving-the-generator) and [the infinite-temperature spectrum](../science/model.md#infinite-temperature-spectrum).

### M19 — The first exact boundary from partial transpose

**Central question.** Which eigenvalue determines when the complete channel becomes PPT?

**Understanding target.** Translate the Pauli multipliers into the normalized Choi state and its output partial transpose. Follow why the commuting Pauli products make its spectrum explicit and why ordering the candidate eigenvalues reduces positivity to $`r+2u+2v\le1`$. Interpret the equality time $`t_P`$ as a channel-level boundary.

**Dependencies and story role.** Earlier IDs: M11, M12, M18. Establishes the first global threshold from the solved local dynamics.

**Conceptual connection.** A complete spectral positivity calculation has different force from testing entanglement decay for a selected initial state.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) provide map context only; the Choi and partial-transpose proof is supplied locally. **Project:** [Exact PPT criterion](../science/exact_thresholds.md#2-exact-ppt-criterion) and [the attributed channel/state equivalences](../references/RELATED_WORK.md#choi-states-ppt-and-entanglement-breaking-channels).

### M20 — Certify entanglement beyond the PPT boundary

**Central question.** What still detects entanglement after partial transpose has become positive?

**Understanding target.** Understand the positivity of the Breuer–Hall map from the orthogonality induced by its skew-symmetric unitary. Follow the fixed maximally entangled witness vector to the expectation $`(1-r-4u)/8`$. Recognize that negativity proves non-EB behavior, while a nonnegative value alone does not prove EB.

**Dependencies and story role.** Earlier IDs: M11, M12, M18, M19. Supplies the necessary condition for the later EB threshold and exposes the intermediate entanglement.

**Conceptual connection.** The positive-map argument goes beyond PPT without replacing the separate sufficiency task.

**Sources.** **Anchor:** [RH §3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) supplies the complete-positivity distinction only; the witness is not attributed to the anchor. **Project:** [The witness calculation](../science/exact_thresholds.md#3-an-entanglement-witness-up-to-the-eb-boundary) and [Breuer–Hall attribution](../references/RELATED_WORK.md#the-breuerhall-witness).

### M21 — Elementary EB channels with known Pauli action

**Central question.** Which explicit measurements and preparations can be assembled to prove an EB boundary?

**Understanding target.** Distinguish the singleton Pauli channel, which measures two eigenspaces and prepares a normalized mixed state inside the selected eigenspace, from pinching alone. Explain why complete dephasing in a joint eigenbasis of a maximal commuting Pauli triple is also EB. Identify exactly which Pauli coefficients each elementary channel retains.

**Dependencies and story role.** Earlier IDs: M03, M18, M20. Constructs the local operational pieces needed for a sufficiency proof of EB.

**Conceptual connection.** Matching simple measure-and-prepare maps on an operator basis turns an abstract separability question into a constructive channel identity.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) provide channel context; these elementary EB constructions are supplied by the repository. **Project:** [Two explicit measure-and-prepare channels](../science/exact_thresholds.md#41-two-explicit-measure-and-prepare-channels).

### M22 — Assemble all twenty components into the exact EB proof

**Central question.** Why does the witness boundary actually admit a complete measure-and-prepare realization?

**Understanding target.** Follow how five mutually anticommuting Pauli operators organize the fifteen commuting triples, and how their incidence counts reproduce every channel multiplier. Understand the roles of nonnegative weights, total weight one at $`r+4u=1`$, and equality on a full operator basis. Combine this boundary construction with semigroup composition and the earlier witness to obtain an exact EB time $`t_E`$.

**Dependencies and story role.** Earlier IDs: M03, M04, M18, M20, M21. Combines elementary pieces into the second global threshold and closes the necessity–sufficiency gap.

**Conceptual connection.** A separable decomposition proves the whole channel is EB, including inputs and reference systems that were not individually tested.

**Sources.** **Anchor:** [RH §§1.3 and 3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) support composition and channel structure only. **Project:** [All twenty components](../science/exact_thresholds.md#42-all-twenty-components), [coefficient matching](../science/exact_thresholds.md#43-why-the-mixture-reproduces-the-channel), and [nonnegative weights and later times](../science/exact_thresholds.md#44-nonnegative-weights).

### M23 — Interpret the separation and its weak-interference law

**Central question.** How does a small unresolved component open a finite interval between the two boundaries?

**Understanding target.** Use the two exact criteria to understand why their roots coincide at $`\eta=0`$ and separate for every $`\eta>0`$ at infinite temperature. Distinguish the linear opening of $`t_E-t_P`$ from the quadratic shift of $`t_P`$ near zero interference. Interpret the explicit maximal-interference endpoints and the inclusion of the PPT boundary but exclusion of the EB boundary in the bound-entangled interval.

**Dependencies and story role.** Earlier IDs: M16, M18, M19, M20, M22. Integrates both spectral and constructive proofs into a single dynamical picture.

**Conceptual connection.** The dependence on bath cross-correlations isolates a mechanism that population relaxation and the common spectral gap do not reveal.

**Sources.** **Anchor:** [RH §§1.2–1.3](RIVAS_HUELGA_BRIDGE.md#reading-route) give semigroup context; the threshold ordering and expansion are project results. **Project:** [Threshold ordering and weak-interference behavior](../science/exact_thresholds.md#5-threshold-ordering-and-weak-interference-behavior) and [two losses of functionality](../science/interpretation.md#two-losses-of-quantum-functionality).

### M24 — Extract an entangled two-qubit state before PPT onset

**Central question.** Why is the entire pre-PPT region provably distillable rather than merely NPT?

**Understanding target.** Follow the fixed local projection onto energy levels 0 and 1 on both reference and output. Interpret its nonvanishing success probability and the rank-two negative partial-transpose vector. Understand why this produces an entangled two-qubit state for every fixed $`t\lt t_P`$ without invoking a general claim that all higher-dimensional NPT states are distillable.

**Dependencies and story role.** Earlier IDs: M11, M12, M13, M18, M19, M23. Supplies a concrete local operation connecting the first spectral boundary to usable entanglement.

**Conceptual connection.** An explicit low-dimensional filter supplies the operational content that a negative eigenvalue alone would not guarantee in general dimensions.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) supply map context only; the filtering and distillability argument is local to the project. **Project:** [The local projection](../science/operational_meaning.md#1-a-local-projection-before-ppt-onset) and [distillability attribution](../references/RELATED_WORK.md#distillability-and-two-way-assisted-quantum-communication).

### M25 — Account for a strictly positive communication rate

**Central question.** How does successful filtering become a positive asymptotic rate rather than a rare favorable event?

**Understanding target.** Connect the conditional Bell fidelity above one half to isotropic twirling, a finite number of recurrence rounds with retwirling, and a positive hashing yield. Track discarded projections, recurrence success probabilities, and consumption of two pairs per round. Explain how distilled entanglement and free classical communication provide a positive two-way quantum communication rate for each fixed pre-threshold channel.

**Dependencies and story role.** Earlier IDs: M03, M13, M24. Converts the local entanglement certificate into a rate statement with its resource and success accounting visible.

**Conceptual connection.** Postselection can support a capacity lower bound only when its probability and subsequent pair consumption are included; the proof does not compute the optimal capacity.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) support the channel description only. **Project:** [The explicit positive-rate route](../science/operational_meaning.md#an-explicit-positive-rate-route) and [the inherited recurrence and hashing ingredients](../references/RELATED_WORK.md#distillability-and-two-way-assisted-quantum-communication).

### M26 — Prove zero capacity even with adaptive channel use

**Central question.** Why can unlimited local processing and two-way classical communication not bypass the PPT boundary?

**Understanding target.** Follow preservation of PPT when a subsystem moves from sender to receiver through a PPT channel, including conditioning on measurement outcomes and adaptive later inputs. Understand the overlap bound between a PPT state and a maximally entangled target. Combine this upper bound with M25 to identify the exact positivity boundary of two-way-assisted capacity, while distinguishing its sign from its numerical value.

**Dependencies and story role.** Earlier IDs: M02, M11, M13, M19, M25. Completes the operational proof and gives the earlier exact threshold its communication meaning.

**Conceptual connection.** A property of one channel use becomes a converse for arbitrary independent uses only after the state shared across the evolving laboratory cut is tracked.

**Sources.** **Anchor:** [RH §§3.1–3.2](RIVAS_HUELGA_BRIDGE.md#reading-route) supply complete-positivity context; the adaptive capacity converse is repository-supplied. **Project:** [Adaptive PPT preservation](../science/operational_meaning.md#2-zero-capacity-after-ppt-onset-including-adaptive-protocols), [the later EB threshold](../science/operational_meaning.md#3-entanglement-breaking-at-the-later-threshold), and [operational scope](../science/operational_meaning.md#4-scope-of-the-operational-conclusions).

### M27 — Carry a strict certificate to positive inverse temperature

**Central question.** What survives when the stationary state is no longer maximally mixed?

**Understanding target.** Explain why a strict positive PPT margin and a strictly negative fixed witness expectation can survive a bounded generator perturbation. Follow the role of Duhamel's formula, channel contraction, and the separate partial-transpose and witness norm estimates in the explicit $`\beta=10^{-4}`$ certificate. Distinguish this existence-and-neighborhood result from exact thermal onset curves or a claim that arbitrarily weak interference works at a fixed positive inverse temperature.

**Dependencies and story role.** Earlier IDs: M04, M08, M09, M17, M19, M20, M23. Extends the physical significance beyond the exactly solved infinite-temperature point while preserving the theorem's quantifiers.

**Conceptual connection.** Strict inequalities make the channel classification robust; they do not transport the entire exact phase diagram to a different temperature.

**Sources.** **Anchor:** [RH §§1.2–1.3 and §5.2.8](RIVAS_HUELGA_BRIDGE.md#reading-route) give dynamical and thermal context; the diamond-norm certificate is supplied by the repository. **Project:** [The strict reference point](../science/thermal_extension.md#a-strict-reference-point), [generator-to-channel and witness bounds](../science/thermal_extension.md#passing-from-generators-to-channels-and-witnesses), [the rational certificate](../science/thermal_extension.md#an-entirely-explicit-positive-inverse-temperature), and [thermal scope](../science/thermal_extension.md#scope-of-the-thermal-result).

### M28 — Identify which physical perturbations preserve the comparison

**Central question.** Which changes are small perturbations of this model, and which rebuild a different effective dynamics?

**Understanding target.** Distinguish changing admissible rates at fixed repeated gaps from splitting the gaps and taking a new fully secular weak-coupling limit. Explain the order-of-limits issue and why an arbitrary diagonal Lamb shift is not automatically a harmless output unitary. Preserve the distinction between the specified KMS-compatible mathematical family and an unchanged microscopic bath or a platform-specific implementation.

**Dependencies and story role.** Earlier IDs: M05, M06, M08, M15, M16, M17, M27. Places the exact and thermal results within their physical domain of validity.

**Conceptual connection.** The control parameter describes equal-frequency pathway information; it does not license keeping arbitrary nonsecular terms or asserting robustness under a singular change in the generator construction.

**Sources.** **Anchor:** [RH §§5.2.3, 5.2.6, and 5.2.8](RIVAS_HUELGA_BRIDGE.md#reading-route), for the weak-coupling limit, secular scope, and thermal state. **Project:** [Hamiltonian scope](../science/model.md#the-hamiltonian-part), [detuning and secular order](../science/model.md#detuning-and-the-secular-order-of-limits), [admissible neighborhoods](../science/thermal_extension.md#open-neighborhoods-in-time-and-admissible-rates), and [physical scope](RIVAS_HUELGA_BRIDGE.md#physical-scope).

### M29 — Identify the contribution and the evidence supporting it

**Central question.** Which conclusion remains after the known ingredients and the limits of verification are made explicit?

**Understanding target.** Distinguish the inherited static symplectic endpoint and existing noise-induced bound-entanglement phenomena from the matched Davies interpolation and its exact boundaries. Understand why the related resolved-transition theorem has a different jump hypothesis. Separate primary-source attribution, general analytical proofs, and finite numerical checks that expose sign, normalization, or multiplicity errors without proving the whole parameter range.

**Dependencies and story role.** Earlier IDs: M14, M17, M22, M23, M26, M27, M28. Evaluates the assembled result as a scientific contribution with explicit provenance and scope.

**Conceptual connection.** The meaningful advance is the relation between a physical bath control and rigorously different channel lifetimes, rather than rediscovery of a known entangled state or accumulation of numerical examples.

**Sources.** **Anchor:** [RH §§4.2–4.4 and §§5.2.1–5.2.4](RIVAS_HUELGA_BRIDGE.md#reading-route) identify the inherited open-systems framework, not a novelty claim. **Project:** [Related work and attribution](../references/RELATED_WORK.md), [why detailed balance does not identify the boundaries](../science/interpretation.md#why-detailed-balance-does-not-force-the-boundaries-to-agree), and [limits of the verification checks](../verification/README.md#limits-of-these-checks).

### M30 — Integrate mechanism, exact boundaries, and operational meaning

**Central question.** What does the complete project establish about how equilibrium noise removes quantum functionality?

**Understanding target.** Give a connected account from bath pathway indistinguishability to coherence transfer, the exact PPT and EB thresholds, and the three duration regimes of the channel. Explain why identical population dynamics, identical bare coherence self-damping, detailed balance, and a common infinite-temperature spectral gap coexist with a bound-entangled interval. Include the constructive proof of the later boundary, the matching operational bounds at the earlier one, and the separately scoped positive-temperature persistence.

**Dependencies and story role.** Earlier IDs: M14, M16, M17, M18, M22, M23, M26, M27, M28, M29. Integrates the narrative into the project's full physical and mathematical conclusion.

**Conceptual connection.** Thermal relaxation, loss of distillable entanglement, and a measure-and-prepare description are distinct properties whose relation depends on how the bath combines equal-frequency transition pathways.

**Sources.** **Anchor:** [The RH reading route and bridge](RIVAS_HUELGA_BRIDGE.md#reading-route) supply the open-systems foundation; the synthesis uses the project's complete argument. **Project:** [Scientific overview](../science/README.md), [exact thresholds](../science/exact_thresholds.md), [operational meaning](../science/operational_meaning.md), [thermal persistence](../science/thermal_extension.md), and [interpretation and scope](../science/interpretation.md).
