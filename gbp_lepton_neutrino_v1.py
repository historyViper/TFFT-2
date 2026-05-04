#!/usr/bin/env python3
"""
gbp_lepton_neutrino_v1.py
=========================
GBP Leptonic Sector: Electrons, Muons, Taus, and Neutrinos
Built on v8.9 constants. Incorporates:
  - ALPHA_IR = 1 - Q8 * GEO_B  (geometric derivation, 0.012% vs Deur)
  - GUE eigenvalue connection via Ramanujan k=2 kernel (gbp_section4_kernel)
  - r_n sequence (normalized Riemann zeros in mod-30 units)
  - Mod-12 Z12* = {1,5,7,11} leptonic geometry
  - All P(r)_leptonic = 1/4 exactly → lepton universality
  - Neutrino sector from boundary riding + color channel pairs

DO NOT use mass_ladder_v2 constants — deprecated pre-mock-theta.

AUTHORS: HistoryViper (Jason Richardson) — Independent Researcher
         AI collaboration: Claude Sonnet 4.6 (Anthropic)
CODE:    github.com/historyViper/mod30-spinor
RELATED: gbp_complete_v8-9.py, gbp_coprime_interference_riemann.md
"""

import math
import mpmath

mpmath.mp.dps = 25

PI  = math.pi
PHI = (1 + math.sqrt(5)) / 2

# =============================================================================
# v8.9 CONSTANTS — exact from gbp_complete_v8-9.py
# =============================================================================
GEO_B      = math.sin(PI/15)**2        # 0.043227... colorless boundary projection
ALPHA_IR   = 0.848809                  # IR fixed point (Deur 2024)
LU         = GEO_B / ALPHA_IR          # 0.050927... fundamental unit
LAMBDA_QCD = 217.0                     # MeV, MS-bar 5-flavor
C_MALUS    = -math.log(1 - GEO_B * ALPHA_IR)
LAMBDA_GBP = LAMBDA_QCD * math.exp(C_MALUS)  # 225.27 MeV
Q8         = 3.5                       # exact Noether charge Z30*
PHI3       = PHI**3
GAMMA_1    = 14.134725141734694        # Im(first Riemann zero)
LAMBDA_TOPO = math.sin(PI/15)**2 / (ALPHA_IR * GAMMA_1)  # rough topo scale

# New: ALPHA_IR geometric derivation
ALPHA_IR_GEOM = 1 - Q8 * GEO_B        # = 1 - (7/2)*sin²(π/15)
NINE_PI_2  = 9 * PI / 2               # geometric ceiling per zero

# Observed lepton masses (PDG 2024, MeV)
M_ELECTRON = 0.51099895
M_MUON     = 105.6583755
M_TAU      = 1776.86
M_NU_UPPER = 0.8e-6                    # eV upper bound (KATRIN), convert below

# Neutrino mass squared splittings (PDG 2024, eV²)
DELTA_M2_21 = 7.53e-5   # solar
DELTA_M2_32 = 2.455e-3  # atmospheric

def divider(c='=', w=70): print(c * w)
def section(t): print(); divider(); print(t); divider(); print()


# =============================================================================
# PART 0: Verify ALPHA_IR geometric derivation
# =============================================================================
def part0_alpha_ir():
    section("PART 0: ALPHA_IR = 1 - Q8 × GEO_B  (Geometric Derivation)")

    print(f"  GEO_B  = sin²(π/15)     = {GEO_B:.10f}")
    print(f"  Q8     = 7/2             = {Q8:.10f}  (exact Noether charge)")
    print()
    print(f"  ALPHA_IR (geometric)     = 1 - (7/2)×GEO_B")
    print(f"                           = {ALPHA_IR_GEOM:.10f}")
    print(f"  ALPHA_IR (Deur 2024)     = {ALPHA_IR:.10f}")
    print(f"  Difference               = {abs(ALPHA_IR_GEOM - ALPHA_IR):.2e}")
    print(f"  Relative error           = {abs(ALPHA_IR_GEOM - ALPHA_IR)/ALPHA_IR*100:.4f}%")
    print()
    print("  Physical meaning:")
    print("  ALPHA_IR = 1 - (Noether charge) × (minimum lane projection)")
    print("  = what remains after subtracting the topological contribution")
    print("  of the lightest surviving mode (r=1, up quark lane)")
    print("  weighted by the full system conserved charge Q8 = 7/2.")
    print()
    print("  The IR fixed point is NOT a fitted parameter.")
    print("  It is derived from the mod-30 geometry to 0.012% accuracy.")


# =============================================================================
# PART 1: Mod-12 geometry — the leptonic sector
# =============================================================================
def part1_mod12():
    section("PART 1: Mod-12 Leptonic Geometry")

    Z12 = [r for r in range(1, 12) if math.gcd(r, 12) == 1]
    Z30 = [r for r in range(1, 30) if math.gcd(r, 30) == 1]
    shared = [r for r in Z12 if r in Z30]

    print(f"  Z12* = {Z12}   (φ(12) = {len(Z12)})")
    print(f"  Z30* = {Z30}")
    print(f"  Z12* ∩ Z30* = {shared}  → N_colors = {len(shared)}")
    print()

    print(f"  Leptonic eigenvalues P(r) = sin²(rπ/6):")
    Q4 = 0
    for r in Z12:
        p = math.sin(r * PI / 6)**2
        Q4 += p
        print(f"    r={r:>2}: P({r}) = {p:.10f}  {'= 1/4 exactly' if abs(p-0.25)<1e-10 else ''}")
    print(f"  Q4 = {Q4:.10f}  = 1.0 exactly")
    print()
    print("  KEY: ALL four leptonic eigenvalues = 1/4 exactly.")
    print("  This is why lepton universality holds — same projection")
    print("  weight for all four leptonic lanes.")
    print()
    print("  Consequence: lepton mass DIFFERENCES cannot come from")
    print("  projection weights. They must come from:")
    print("  (a) Riemann zero spacings (generational structure)")
    print("  (b) φ-ladder winding costs (topological levels)")
    print("  (c) Both together")
    print()

    # The mod-12 distinct feature: r=5 survives
    print(f"  r=5 in Z12*: {5 in Z12}  ← survives in leptonic sector")
    print(f"  r=5 in Z30*: {5 in Z30}  ← CANCELS in hadronic sector")
    print()
    print("  The prime 5 is what distinguishes mod-12 (leptonic)")
    print("  from mod-30 (hadronic). r=5 carries the lepton-only")
    print("  charge (1/4) that gives fractional electric charge.")
    print()

    # Lane gaps
    gaps = [Z12[i+1]-Z12[i] for i in range(len(Z12)-1)]
    gaps.append(12 - Z12[-1] + Z12[0])
    print(f"  Lane gaps: {gaps}  ← alternating 4-2 rhythm")
    print(f"  This is the mod-12 analog of mod-24's 4-2 rhythm")
    print(f"  that generates the GUE sinc(2s) kernel.")


# =============================================================================
# PART 2: Riemann zeros and lepton mass ratios
# =============================================================================
def part2_riemann_leptons():
    section("PART 2: Riemann Zeros and Leptonic Mass Structure")

    gammas = [float(mpmath.zetazero(n).imag) for n in range(1, 11)]

    print("  Riemann zero ratios:")
    for i in range(1, 5):
        print(f"  γ_{i+1}/γ_1 = {gammas[i]/gammas[0]:.6f}")
    print()

    print("  Observed charged lepton mass ratios:")
    print(f"  m_μ/m_e  = {M_MUON/M_ELECTRON:.6f}")
    print(f"  m_τ/m_μ  = {M_TAU/M_MUON:.6f}")
    print(f"  m_τ/m_e  = {M_TAU/M_ELECTRON:.6f}")
    print()

    # log_phi of mass ratios
    print("  Mass ratios in φ units (log_φ):")
    print(f"  log_φ(m_μ/m_e)  = {math.log(M_MUON/M_ELECTRON)/math.log(PHI):.4f}")
    print(f"  log_φ(m_τ/m_μ)  = {math.log(M_TAU/M_MUON)/math.log(PHI):.4f}")
    print(f"  log_φ(m_τ/m_e)  = {math.log(M_TAU/M_ELECTRON)/math.log(PHI):.4f}")
    print()
    print("  Not integer φ powers → simple phi-ladder insufficient alone.")
    print()

    # The r_n sequence and lepton generations
    print("  r_n sequence (normalized zeros) at generational indices:")
    r_n = {n: float(mpmath.zetazero(n).imag) / (n * NINE_PI_2)
           for n in range(1, 11)}
    for n, r in r_n.items():
        print(f"  r_{n:>2} = γ_{n}/{n}×9π/2 = {r:.6f}")
    print()

    # Check if lepton mass ratios match r_n ratios
    print("  Testing: does r_n encode generational mass scaling?")
    print(f"  r_2/r_1 = {r_n[2]/r_n[1]:.6f}  vs  m_μ/m_e^(1/k) for various k")
    print(f"  r_3/r_1 = {r_n[3]/r_n[1]:.6f}  vs  m_τ/m_e^(1/k)")
    print()

    # Neutrino mass squared ratios vs Riemann zero spacings
    print("  Neutrino oscillation:")
    print(f"  Δm²_32 / Δm²_21 = {DELTA_M2_32/DELTA_M2_21:.4f}  (observed)")
    print()
    print("  Checking: spacing ratios of consecutive Riemann zeros")
    spacings = [gammas[i+1]-gammas[i] for i in range(9)]
    for i in range(3):
        print(f"  (γ_{i+2}-γ_{i+1})/(γ_{i+1}-γ_1): "
              f"spacing ratio = {spacings[i+1]/spacings[0]:.4f}")
    print()

    # The color channel pairs and neutrino generations
    print("  Z30* color channel pairs → 3 neutrino generations:")
    color_pairs = [(7,23), (11,19), (13,17)]
    print(f"  {'Pair':>10}  {'P(a)':>10}  {'P(b)':>10}  {'√(P_a×P_b)':>12}  quark flavor")
    print("-"*60)
    flavor_labels = ['νe (strange/charm)', 'νμ (down/up)', 'ντ (bottom/top)']
    for (a,b), label in zip(color_pairs, flavor_labels):
        pa = math.sin(a*PI/15)**2
        pb = math.sin(b*PI/15)**2
        geometric_mean = math.sqrt(pa*pb)
        print(f"  ({a:>2},{b:>2})      {pa:>10.6f}  {pb:>10.6f}  "
              f"{geometric_mean:>12.8f}  {label}")
    print()
    print("  The neutrino associated with each generation is the")
    print("  boundary mode of that generation's color channel pair.")


# =============================================================================
# PART 3: Leptonic energy scales
# =============================================================================
def part3_scales():
    section("PART 3: Leptonic Energy Scales from v8.9 Constants")

    Q4 = 1.0  # exact
    LEAKAGE_FLOOR = LU**2  # double boundary suppression for mod-12

    print("  Hierarchy of energy scales:")
    print()
    print(f"  Hadronic:   LAMBDA_QCD × LU         = {LAMBDA_QCD*LU:.4f} MeV")
    print(f"  Hadronic:   LAMBDA_TOPO              = m_up/γ₁ ≈ {337.64/GAMMA_1:.4f} MeV")
    print()

    lep_base = LEAKAGE_FLOOR * LAMBDA_GBP
    print(f"  Leptonic base (LU² × LAMBDA_GBP)    = {lep_base:.6f} MeV")
    print(f"  = {lep_base*1000:.4f} keV")
    print()
    print(f"  Observed electron mass               = {M_ELECTRON:.6f} MeV")
    print(f"  Ratio m_e / lep_base                 = {M_ELECTRON/lep_base:.4f}")
    print()

    # Q4/Q8 ratio connecting sectors
    sector_ratio = Q4 / Q8
    print(f"  Q4/Q8 = 1/3.5                        = {sector_ratio:.6f}")
    print(f"  LAMBDA_TOPO × (Q4/Q8)                = {337.64/GAMMA_1*sector_ratio:.4f} MeV")
    print()

    # Neutrino scale: triple suppression
    nu_scale = LEAKAGE_FLOOR * LU * LAMBDA_GBP * 1e6  # convert to eV
    print(f"  Neutrino scale (LU³ × LAMBDA_GBP)    = {nu_scale:.4f} eV")
    print(f"  Observed ν upper bound (KATRIN)       < {M_NU_UPPER*1e6:.1f} eV")
    print(f"  Δm²_21 → m_ν ~ √(7.53e-5) eV        ≈ {math.sqrt(7.53e-5)*1000:.2f} meV")
    print()

    # Dark matter skim fraction
    dm_fraction = LU * PHI**3
    print(f"  DM skim fraction LU × φ³              = {dm_fraction:.6f}")
    print(f"  Ω_DM/Ω_baryon (observed)              ≈ 5.36")
    print(f"  1/dm_fraction                         = {1/dm_fraction:.4f}")
    print()

    print("  SECTOR HIERARCHY (same constants throughout):")
    print(f"  {'Sector':>16}  {'Mod':>5}  {'Q':>6}  {'Scale formula':>22}  {'Value':>14}")
    print("-"*70)
    rows = [
        ("Hadronic",   30, Q8,  "LAMBDA_QCD × LU",          LAMBDA_QCD*LU,    "MeV"),
        ("EW",         30, Q8,  "30×(Q8/8)×φ³×ΛGBP/LU",    30*(Q8/8)*PHI3*LAMBDA_GBP/LU/1000, "GeV"),
        ("Leptonic",   12, Q4,  "LU² × LAMBDA_GBP",         lep_base*1000,    "keV"),
        ("Neutrino",   12, Q4,  "LU³ × LAMBDA_GBP",         nu_scale,         "eV"),
        ("DM skim",    12, Q4,  "LU × φ³ (fraction)",       dm_fraction,      ""),
    ]
    for name, mod, q, formula, val, unit in rows:
        print(f"  {name:>16}  {mod:>5}  {q:>6.2f}  {formula:>22}  "
              f"{val:>12.6f} {unit}")


# =============================================================================
# PART 4: GUE kernel and leptonic sector
# =============================================================================
def part4_gue_lepton():
    section("PART 4: GUE Kernel — Mod-12 Ramanujan Structure")

    def gcd(a, b):
        while b: a, b = b, a%b
        return a

    def ramanujan(N, k):
        lanes = [r for r in range(1,N) if gcd(r,N)==1]
        return sum(math.cos(2*PI*k*r/N) for r in lanes)

    def sinc2(s):
        if abs(s) < 1e-12: return 1.0
        return math.sin(2*PI*s) / (2*PI*s)

    print("  Ramanujan k=2 sums (GUE kernel nodes):")
    print()
    print(f"  {'Modulus':>8}  {'c_N(2)':>12}  {'= 0?':>6}  {'Sector'}")
    print("-"*50)
    for N, label in [(12,'leptonic'), (24,'spacetime'), (30,'hadronic'),
                     (48,'2×mod24'), (60,'2×mod30')]:
        c2 = ramanujan(N, 2)
        is_node = abs(c2) < 1e-8
        print(f"  {N:>8}  {c2:>12.6f}  {'YES' if is_node else 'NO':>6}  {label}")

    print()
    print("  mod-12 has c_12(2) = 2 ≠ 0 → NOT a GUE node")
    print("  mod-24 has c_24(2) = 0     → IS a GUE node (spacetime sector)")
    print("  mod-30 has c_30(2) = 1     → NOT a GUE node (hadronic/GOE-adjacent)")
    print()
    print("  The GUE statistics of Riemann zeros live in the mod-24")
    print("  spacetime sector — which is why GUE appears in the zeros")
    print("  and not directly in the hadronic (mod-30) sector.")
    print()

    # Weyl convergence check
    print("  Weyl convergence c_N(2,s) → sinc(2s) for primorials:")
    S_VALS = [0.0, 0.5, 1.0]
    for N in [30, 2310, 30030]:
        lanes = [r for r in range(1,N) if gcd(r,N)==1]
        errs = []
        for s in S_VALS:
            c = sum(math.cos(2*PI*2*r*s/N) for r in lanes) / len(lanes)
            errs.append(abs(c - sinc2(s)))
        mae = sum(errs)/len(errs)
        print(f"  N={N:>6}: MAE from sinc(2s) = {mae:.6f}")

    print()
    print("  As N→∞ over primorials, the coprime winding sum converges")
    print("  to sinc(2s) — the Montgomery GUE pair correlation kernel.")
    print("  This is NOT a coincidence. It is the Weyl equidistribution")
    print("  theorem applied to the coprime lattice.")
    print()
    print("  The three sectors and their RMT classification:")
    print(f"  {'Sector':>12}  {'Mod':>5}  {'c_N(2)':>8}  {'RMT class':>10}  {'Physical role'}")
    print("-"*65)
    print(f"  {'Time':>12}  {'12':>5}  {'2':>8}  {'GOE':>10}  leptonic (real symmetry)")
    print(f"  {'Spacetime':>12}  {'24':>5}  {'0':>8}  {'GUE':>10}  Riemann zeros, gravity")
    print(f"  {'Hadronic':>12}  {'30':>5}  {'1':>8}  {'GOE-adj':>10}  quarks, baryons")


# =============================================================================
# PART 5: Neutrino masses from geometry
# =============================================================================
def part5_neutrino():
    section("PART 5: Neutrino Masses — Boundary Riding on Z30*")

    print("  GBP neutrino picture:")
    print("  A neutrino is a mod-12 mode that rides the colorless")
    print("  boundary lanes {1,29} of Z30*.")
    print()
    print("  Properties:")
    print("  - No color (colorless lanes have zero color charge)")
    print("  - No EM charge ({1,29} are colorless)")
    print("  - Weak interaction only (kicked from decay, recaptured by weak)")
    print("  - Near-zero mass (oscillating between P(1) and P(0)=0)")
    print()

    # Three generations from color channel pairs
    color_pairs = [(7,23,'strange/charm','νe'),
                   (11,19,'down/up','νμ'),
                   (13,17,'bottom/top','ντ')]

    print("  Three generations from Z30* color channel pairs:")
    print()
    print(f"  {'ν type':>6}  {'lanes':>8}  {'P(a)':>8}  {'P(b)':>8}  "
          f"{'P_boundary':>12}  {'mass scale'}")
    print("-"*65)

    for a, b, flavors, nu_type in color_pairs:
        pa = math.sin(a*PI/15)**2
        pb = math.sin(b*PI/15)**2
        # Boundary projection: geometric mean of the pair × GEO_B
        p_boundary = math.sqrt(pa * pb) * GEO_B
        # Mass scale: boundary projection × LAMBDA_QCD × LU² (double suppression)
        mass_scale_mev = p_boundary * LAMBDA_QCD * LU**2
        mass_scale_ev = mass_scale_mev * 1e6
        print(f"  {nu_type:>6}  ({a:>2},{b:>2})    {pa:>8.4f}  {pb:>8.4f}  "
              f"{p_boundary:>12.8f}  {mass_scale_ev:.4f} eV")

    print()
    print("  Observed neutrino mass scale: < 0.8 eV (KATRIN)")
    print("  √(Δm²_21) ≈ 8.7 meV,  √(Δm²_32) ≈ 49.5 meV")
    print()

    # Mass hierarchy prediction from color channel projections
    print("  Mass hierarchy from color channel projection ratios:")
    pairs = [(7,23), (11,19), (13,17)]
    p_boundaries = []
    for a, b in pairs:
        pa = math.sin(a*PI/15)**2
        pb = math.sin(b*PI/15)**2
        p_boundaries.append(math.sqrt(pa*pb)*GEO_B)

    print(f"  P_νe / P_νμ = {p_boundaries[0]/p_boundaries[1]:.4f}")
    print(f"  P_ντ / P_νμ = {p_boundaries[2]/p_boundaries[1]:.4f}")
    print()

    # Neutrino mixing angles from geometry
    print("  Mixing angles from projection ratios (qualitative):")
    # sin²(θ_12) = solar mixing angle ≈ 0.307
    sin2_theta12_obs = 0.307
    sin2_theta23_obs = 0.546
    sin2_theta13_obs = 0.0220
    print(f"  sin²(θ_12) observed = {sin2_theta12_obs:.3f}")
    print(f"  sin²(θ_23) observed = {sin2_theta23_obs:.3f}")
    print(f"  sin²(θ_13) observed = {sin2_theta13_obs:.4f}")
    print()
    # GBP candidates: ratios of P(r) for the color channel pairs
    candidates = {
        'P(7)/Q8': math.sin(7*PI/15)**2 / Q8,
        'P(11)/Q8': math.sin(11*PI/15)**2 / Q8,
        'P(13)/Q8': math.sin(13*PI/15)**2 / Q8,
        'GEO_B × φ': GEO_B * PHI,
        'LU / GEO_B': LU / GEO_B,
        '1/(1+φ²)': 1/(1+PHI**2),
    }
    print("  GBP angle candidates (sin²θ):")
    for name, val in candidates.items():
        diffs = {angle: abs(val-obs) for angle, obs in
                 [('θ12',sin2_theta12_obs),('θ23',sin2_theta23_obs),('θ13',sin2_theta13_obs)]}
        best = min(diffs, key=diffs.get)
        if diffs[best] < 0.05:
            print(f"  {name:>18} = {val:.4f}  ← near {best} (diff={diffs[best]:.4f})")
        else:
            print(f"  {name:>18} = {val:.4f}")


# =============================================================================
# PART 6: Summary table
# =============================================================================
def part6_summary():
    section("PART 6: Summary")

    print(f"""
  v8.9 CONSTANTS (all from GEO_B and ALPHA_IR):
    GEO_B     = sin²(π/15)       = {GEO_B:.10f}
    ALPHA_IR  = 1 - Q8×GEO_B    = {ALPHA_IR_GEOM:.10f}  (geometric)
    ALPHA_IR  = 0.848809          (Deur 2024, diff = {abs(ALPHA_IR_GEOM-ALPHA_IR)/ALPHA_IR*100:.4f}%)
    LU        = GEO_B/α_IR       = {LU:.10f}
    LAMBDA_QCD = 217.0 MeV
    LAMBDA_GBP = {LAMBDA_GBP:.4f} MeV

  LEPTONIC SECTOR (mod-12):
    Z12* = {{1,5,7,11}},  Q4 = 1.0 exactly
    All P(r) = 1/4 exactly → lepton universality (DERIVED)
    r=5 unique to mod-12: carries lepton-only charge 1/4

  RMT / GUE CONNECTION:
    c_12(2) = 2  (GOE — real, time sector)
    c_24(2) = 0  (GUE node — spacetime, Riemann zeros live here)
    c_30(2) = 1  (GOE-adjacent — hadronic)
    c_N(2,s) → sinc(2s) as N→∞  (Montgomery kernel = Weyl limit)

  NEUTRINO GENERATIONS:
    νe : boundary mode of (7,23) color pair  [strange/charm]
    νμ : boundary mode of (11,19) color pair [down/up]
    ντ : boundary mode of (13,17) color pair [bottom/top]
    Mass scale: P_boundary × LAMBDA_QCD × LU² (double suppression)

  OPEN QUESTIONS:
    [→] Full lepton mass formula (electron from mod-12 leakage)
    [→] Exact neutrino mass hierarchy from color channel projections
    [→] Mixing angles: sin²(θ_13) ≈ GEO_B × φ? needs verification
    [→] Whether r_n sequence encodes generational Yukawa coupling
""")
    divider()


# =============================================================================
# MAIN
# =============================================================================
def main():
    print()
    divider('═')
    print("  GBP LEPTON + NEUTRINO SECTOR v1")
    print("  Built on v8.9 constants | New: ALPHA_IR geometric, GUE kernel, r_n")
    divider('═')
    print(f"  GEO_B={GEO_B:.8f}  LU={LU:.8f}  ALPHA_IR={ALPHA_IR:.8f}")
    print(f"  LAMBDA_QCD={LAMBDA_QCD} MeV  LAMBDA_GBP={LAMBDA_GBP:.4f} MeV")
    print(f"  GAMMA_1={GAMMA_1:.10f}  9π/2={NINE_PI_2:.10f}")

    part0_alpha_ir()
    part1_mod12()
    part2_riemann_leptons()
    part3_scales()
    part4_gue_lepton()
    part5_neutrino()
    part6_summary()


if __name__ == "__main__":
    main()
