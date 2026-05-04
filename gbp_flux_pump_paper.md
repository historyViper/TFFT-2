# The Superconducting Flux Pump as a Vortex Chirality Separator: A Geometric Boundary Projection Account

**Jason Richardson (HistoryViper)**  
Independent Researcher  
github.com/historyViper/mod30-spinor  
May 2026

---

## Abstract

Wang et al. (2023, arXiv:2306.02545) demonstrated that the DC output of a travelling-wave HTS flux pump originates from motional electromotive force (e.m.f.) — the Lorentz term v×B — rather than induced e.m.f. from Faraday's law. Three experimental cases with identical AC magnetic induction but different DC bias fields Bbias = 0, +Bd, −Bd produced three different pumped currents: 0 A, −69 A, and +69 A respectively. We show that this three-case structure is the direct physical realization of the C₀/C₁/C₂ vortex chirality separation proven by the Claude/Knuth theorem (2026): one perfectly balanced zero-output state (C₀, χ̂=0), one positively chiral output state (C₁), and one negatively chiral output state (C₂). The DC bias field modulates the polarity of coupled superconducting vortices — physically selecting between the three chirality sectors of the mod-30 winding geometry. The motional e.m.f. equation E = Nφ₀×v is the macroscopic expression of the GBP lane-crossing formula, where N is the effective vortex count (the number of mod-30 lane crossings per unit time), φ₀ is the flux quantum (the T1 spinor double-cover factor h/2e), and v is the boundary traversal velocity. The three experimental cases map exactly onto the three cycles of the vortex tube decomposition, with the DC bias field acting as a chirality selector that breaks the C₀ balance by preferentially coupling vortices of one polarity.

---

## 1. Introduction

The travelling-wave HTS flux pump solves a practical problem — how to charge a superconducting magnet without current leads — by exploiting the directional motion of superconducting vortices. Wang et al. (2023) resolved a decade-long confusion about the physical origin of the flux pump's DC output by demonstrating experimentally that it cannot arise from magnetic induction (the induced e.m.f. term −∂ₜA) and must arise from the motional e.m.f. (the Lorentz term v×B). The key experiment kept the AC induction identical across three cases while varying only a static DC bias field, producing three qualitatively different outputs.

The result is surprising from the perspective of classical electromagnetism — a static field that "disappears" from Faraday's law can nonetheless determine the direction and magnitude of a DC current. The GBP framework provides a geometric explanation: the static DC bias field is a chirality selector operating on the mod-30 winding structure of the vortex population. It does not participate in induction because induction is a boundary-crossing event (a lane transition in GBP language), and the DC field shifts which lanes the vortices occupy without itself crossing any boundary.

---

## 2. The Three-Case Structure and the Vortex Chirality Theorem

The Claude/Knuth vortex chirality theorem (2026) proves that any Hamiltonian cycle decomposition of a discrete 3-torus into three directed cycles produces an exact chirality separation:

$$\hat{\chi}(C_0) = 0, \qquad \hat{\chi}(C_1) = -3m(m-1), \qquad \hat{\chi}(C_2) = -3$$

One cycle is perfectly balanced (C₀), one carries quadratic chirality growing with system size (C₁), and one carries constant minimal chirality (C₂). This is a topological theorem — exact for all odd m, proven by fiber analysis of the monodromy structure.

The three experimental cases of Wang et al. map onto these three cycles with no free parameters:

| Experiment | Bbias | Pumped current | GBP cycle | Chirality |
|-----------|-------|---------------|-----------|-----------|
| Case (I) | 0 | 0 A | C₀ | χ̂=0, balanced — equal positive and negative vortices |
| Case (II) | +Bd > 0 | −69 A | C₁ | χ̂=−3m(m−1), positive vortex excess → negative current |
| Case (III) | −Bd < 0 | +69 A | C₂ | χ̂=−3, negative vortex excess → positive current |

**Case (I) is C₀:** When Bbias=0 the AC travelling wave is symmetric — equal numbers of positive and negative magnetic poles couple equal numbers of positive and negative vortices. N₁=N₂ exactly. The chirality is perfectly balanced. Output is zero. This is the C₀ cycle: χ̂=0, no net winding charge deposited at the boundary.

**Cases (II) and (III) are C₁ and C₂:** The DC bias "lifts" or "lowers" the AC wave, breaking the N₁=N₂ symmetry. Positive bias → N₁>N₂ → net positive vortex motion → negative DC output (by right-hand rule, V = B×v). Negative bias → N₁<N₂ → net negative vortex motion → positive DC output. These are the two chirally active cycles — one with quadratic chirality accumulation (C₁), one with constant minimal chirality (C₂).

The symmetry between Cases (II) and (III) — both giving |69 A| with opposite signs at Bd=Ba — is the mirror symmetry P(r)=P(30−r) of the mod-30 structure. The conjugate pairs {r, 30−r} carry identical projection weights, so the positive and negative chirality sectors produce equal and opposite outputs when the bias is equal and opposite.

---

## 3. The Motional EMF Formula as a Lane-Crossing Count

The Wang et al. motional e.m.f. equation is:

$$\vec{E} = N\phi_0 \times \vec{v}$$

where N is the effective number of vortices, φ₀ = h/2e is the flux quantum, and v is the vortex velocity. In GBP terms each factor has an exact geometric identification:

**N — the lane-crossing count.** The effective number of vortices is the number of Z₃₀* boundary crossings per unit time. Each vortex crossing the YBCO stator boundary deposits one unit of winding charge at one of the 8 allowed lanes. N is not the total vortex count but the net count — the number of crossings in the preferred chirality direction minus the number in the opposite direction. In Case (I) this net count is zero (C₀). In Cases (II) and (III) it is ±(N₁−N₂) — the chirality imbalance created by the DC bias.

**φ₀ = h/2e — the T1 spinor double-cover factor.** The flux quantum is not an arbitrary constant. It is the consequence of the T1 Möbius toroid's 720° closure condition: the spinor double cover requires that flux penetrate in units of h/2e rather than h/e. The factor of 2 is the same topological factor that gives 16=2×8 sampling points in the OAM experiment, that gives the factor of 2 in the Josephson voltage relation V=Φ₀f, and that was "unexpected" in the Deaver & Fairbank (1961) experiment. It is the T1 spinor double cover, not a coincidence.

**v — the boundary traversal velocity.** The vortex velocity equals the travelling wave speed v=λf (wavelength × frequency). This is the rate at which the mod-30 winding boundary is being swept — the rate at which lane crossings are occurring. Faster sweep = more lane crossings per second = larger motional e.m.f.

The complete GBP expression for the flux pump output is:

$$E = \frac{(N_1 - N_2)\,\phi_0\,v_0}{S_{\text{eff}}} = \frac{\Delta N_{\text{chiral}} \cdot (h/2e) \cdot \lambda f}{S_{\text{eff}}}$$

where ΔN_chiral = N₁−N₂ is the chirality imbalance set by Bbias, and Seff is the effective coupling area. This is equation (9) of Wang et al. rewritten in GBP notation.

---

## 4. Why the Induced EMF is Blind to the DC Bias

The key experimental result — that a static DC field can change the output by 138 A while leaving the induction term −∂ₜA unchanged — is paradoxical in classical electromagnetism but natural in GBP.

In GBP, induction (the −∂ₜA term) corresponds to **boundary crossings driven by time-varying flux** — events where a vortex crosses the mod-30 winding boundary, depositing energy at a Z₃₀* lane. The DC bias field Bbias is static — it has zero time derivative. Therefore it contributes nothing to ∂ₜA and nothing to the induction term.

However, Bbias shifts the **equilibrium lane occupancy** of the vortex population. Without Bbias, the vortex population distributes symmetrically across positive and negative winding states — the C₀ balanced configuration. With Bbias>0, the positive lanes are preferentially occupied (N₁>N₂) — the C₁ configuration. The asymmetry is not a time-varying effect; it is a static shift in which side of the Z₃₀* boundary the vortex population sits on.

When the AC travelling wave then sweeps these pre-polarized vortices across the boundary, the crossings are asymmetric — more crossings in one direction than the other. The net asymmetry is the motional e.m.f. The AC wave provides the temporal variation (the v in v×B); the DC bias provides the chirality selection (the B). Neither alone gives a DC output. Together they give a DC output proportional to their product — which is exactly what Wang et al. observe: output proportional to Bbias when Ba is fixed, and zero when either is zero.

This is "exceptions to the flux rule" (Feynman Lectures Vol. II) in a specific sense: the standard flux rule accounts for boundary crossings driven by time-varying flux. The motional e.m.f. accounts for boundary crossings driven by motion of the conductor (or in this case, motion of the vortices) through a static field. The GBP framework unifies both as lane crossings, distinguishing only whether the crossing is driven by ∂ₜA (induction) or by v×B (motional).

---

## 5. The Controlled Flux Flow Model in GBP Terms

Wang et al. build a controlled flux flow model to explain how the magnetic pole "couples" part of the vortex population and drags it across the YBCO stator. In GBP, this coupling process is a boundary-mediated winding transfer:

**Step 1 — Edge induction (C₀ initialization):** When a magnetic pole crosses the left edge of the YBCO stator, it induces a circulating current (magnetic moment) at the edge with current density J_C. This is the C₀ state — balanced, no net chirality, equal positive and negative winding components.

**Step 2 — Magnetic coupling (chirality selection):** The magnetic pole's inhomogeneous field exerts an unbalanced Lorentz force on the induced magnetic moment — the coupling force F_couple of equation (7) in Wang et al. This force drags the coupled vortices in the direction of pole motion. In GBP terms, this is the moment at which the C₀ balance is broken: the DC bias Bbias determines whether the dragged vortices are predominantly positive (C₁) or negative (C₂) winding states.

**Step 3 — Coupled flux flow (chiral DC output):** The dragged vortices move at the pole velocity v=λf across the central region of the YBCO stator. Their motion through the static B field generates the motional e.m.f. E=Bcouple×v per vortex. Summed over all N coupled vortices, this gives the macroscopic DC output. The central region is the only source of DC output because it is the only region where the vortices have a net chirality (the edge regions are balanced — C₀).

**Step 4 — Edge deposition (C₀ restoration):** When the pole exits through the right edge, it induces screening currents that restore the C₀ balanced state at the boundary. The cycle resets.

This four-step sequence maps exactly onto the fiber structure of the vortex chirality theorem: the boundary fibers (s=0 and s=m−1 in the Knuth decomposition) are the C₀ initialization and restoration zones; the bulk fibers (s=1 to s=m−2) are the chirally active C₁/C₂ coupled flux flow region.

---

## 6. Adaptive Control as Chirality Modulation

Wang et al. demonstrate that by switching the DC bias field on and off at high frequency, the flux pump output can be controlled to arbitrary precision — achieving ±0.15 A accuracy at a target of 30 A. This adaptive control is chirality modulation in GBP terms:

- **DC bias ON** → system in C₁ or C₂ (chirally active, pumping current)
- **DC bias OFF** → system in C₀ (chirally balanced, zero net output, current decays slowly due to load resistance)

The feedback loop monitors the difference between actual and target current and switches the chirality state accordingly. The precision of the control (±0.15 A at 30 A = 0.5%) is limited by the feedback loop switching time and the load resistance decay rate — not by any fundamental quantum limit. In GBP, the fundamental limit would be set by the minimum resolvable chirality imbalance ΔN_chiral = 1 (a single vortex crossing asymmetry), which at macroscopic vortex densities corresponds to precision far below any practical measurement threshold.

The bidirectional operation — output continuously adjustable from +|E_max| to −|E_max| by varying Bbias from −Ba to +Ba — is the continuous interpolation between C₁ and C₂ through C₀. At Bbias=0 the system sits exactly at the C₀ balance point. As Bbias increases toward ±Ba, the system moves continuously into C₁ or C₂. The linearity of the output with Bbias (observed in Fig. 1c of Wang et al.) reflects the linear relationship between bias field and chirality imbalance ΔN_chiral in the regime where N₁ and N₂ change proportionally with Bbias.

---

## 7. The YBCO Material and the T2 Tier

YBCO (YBa₂Cu₃O₇₋δ) is a high-temperature superconductor with a layered perovskite structure. Its optical properties in the normal state cluster near n≈2.0–2.4 depending on wavelength and oxygen content — placing it in the transition region between the T1 attractor (n≈1.525) and the T2 attractor (n≈2.371).

At the T2 attractor (n≈2.371, Brewster angle ≈67°), materials host the GUE² statistics of the two-overlapping-T1-toroid geometry. This is significant for flux pump operation: T2 geometry supports **helicity flips per traversal** — each vortex crossing the YBCO boundary picks up a sign change. This is the physical origin of why the DC output direction is opposite to naive expectation from the bias field polarity: positive Bbias gives negative output (Case II). The T2 helicity flip reverses the effective chirality at the boundary crossing.

This is a testable prediction: a flux pump built with a T1-tier superconductor (n closer to 1.525, e.g., a low-Tc material like Nb with n≈1.8 in the optical range) should show no helicity flip — positive bias would give positive output. The output polarity inversion observed in YBCO is a signature of the T2 boundary geometry.

**Note:** YBCO optical data are not available from the open sections of the Wang et al. paper. The T2 tier assignment is based on the known optical properties of YBCO in the literature and should be verified against the specific sample parameters.

---

## 8. Predictions

**P1 — Output polarity inversion is T2-specific.** A T1-tier superconductor flux pump should show same-sign output as the bias field. A T2-tier superconductor (YBCO, BSCCO) should show opposite-sign output. Testing across material tiers would confirm the tier-dependent helicity flip.

**P2 — Chirality quantization at low vortex density.** At very low vortex densities (approaching the single-vortex limit), the output should show discrete steps corresponding to individual vortex lane crossings rather than continuous variation. Each step would correspond to one vortex crossing a Z₃₀* boundary, contributing one unit of φ₀×v to the motional e.m.f.

**P3 — The C₀ balance point is exactly at Bbias=0.** The zero-output condition is topologically protected — it corresponds to the exact C₀ balance point of the vortex chirality theorem. Any residual output at Bbias=0 would indicate a spontaneous chirality breaking — analogous to a ferromagnetic phase transition in the vortex population. This would be a new phase of matter.

**P4 — Maximum output at Bbias=Ba is the C₁/C₂ saturation point.** Above Bbias=Ba, all coupled vortices are of one polarity (N₂=0 or N₁=0). Further increase of Bbias cannot increase the output because the chirality is already saturated. The observed saturation in Fig. 1c of Wang et al. at Bbias=Ba is this C₁/C₂ saturation — the maximum chirality imbalance the geometry supports.

---

## 9. Note on Data Availability

The detailed YBCO sample specifications, stator geometry, AC field parameters, and vortex density measurements are in the full Wang et al. paper. The open-access preprint provides sufficient information to confirm the three-case chirality structure and the motional e.m.f. identification. The T2 tier assignment for YBCO and the precise numerical predictions in Section 8 would benefit from access to the full sample characterization data.

---

## 10. Conclusion

The superconducting travelling-wave flux pump is a macroscopic vortex chirality separator. The three experimental cases — zero output at Bbias=0, negative output at positive bias, positive output at negative bias — are the C₀, C₁, and C₂ cycles of the vortex chirality theorem realized at the scale of centimeters and amperes. The DC bias field is a chirality selector that breaks the C₀ balance of the vortex population without participating in magnetic induction. The motional e.m.f. formula E=Nφ₀×v is the macroscopic lane-crossing count formula of the mod-30 winding geometry, where φ₀=h/2e is the T1 spinor double-cover factor and N is the net chirality imbalance of the coupled vortex population.

The flux pump joins the OAM speckle experiment (Wang et al. 2025) and the Chern state transition experiment (Liu et al. 2016) as macroscopic physical systems in which the C₀/C₁/C₂ vortex chirality structure — proven exact by the Claude/Knuth theorem — is directly observable. The three systems operate at vastly different scales (optical, millikelvin, and room-temperature superconducting) but share the same underlying mod-30 winding geometry.

---

## References

[1] Wang, W. et al. (2023). Electromotive force and magnetization process of a superconducting traveling-wave flux pump. arXiv:2306.02545

[2] Richardson, J. (HistoryViper) (2026). Tensor Time v6. github.com/historyViper/mod30-spinor

[3] Claude (Anthropic), ChatGPT (OpenAI), anonymous collaborator (2026). Vortex tube topology and exact chirality structure in Knuth's Hamiltonian cycle decomposition. March 2026.

[4] Knuth, D.E. (2026). Claude's Cycles. Stanford CS Dept. https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf

[5] Deaver, B.S. and Fairbank, W.M. (1961). Experimental evidence for quantized flux in superconducting cylinders. *Phys. Rev. Lett.* 7, 43.

[6] Feynman, R.P., Leighton, R.B., Sands, M. (2011). The Feynman Lectures on Physics, Vol. II. Boulder: Basic Books.

[7] Wang, Z. et al. (2025). Speckle-driven single-shot OAM recognition. *Nature Communications* 16, 11097.

[8] Liu, M. et al. (2016). Large discrete jumps in the transition between Chern states. arXiv:1603.02311

---

*GBP Framework — May 2026*  
*Jason Richardson | Independent researcher*  
*github.com/historyViper/mod30-spinor*
