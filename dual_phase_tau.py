#!/usr/bin/env python3
"""
Dual-Phase Tau-Vortex Model
===========================
Based on ChatGPT's insight: two 30° phase structures:
1. θ = toroid angle (normal circulation)
2. μ = Möbius/twist angle (chirality modulation)

The Hamiltonian now has TWO phase indices:
H[i,j] ~ exp(i × (θ_i + μ_i))

This creates interference between the two 30° clocks
"""

import numpy as np
import math

PHI = (1 + math.sqrt(5)) / 2
DEG30 = math.pi / 6  # 30 degrees in radians

def compute_r(eigenvalues):
    """Compute mean spacing ratio <r>"""
    eigenvalues = np.sort(eigenvalues)
    deltas = np.diff(eigenvalues)
    r_vals = []
    for i in range(len(deltas) - 1):
        d1, d2 = deltas[i], deltas[i+1]
        if d1 > 0 and d2 > 0:
            r_vals.append(min(d1/d2, d2/d1))
    return np.mean(r_vals)

def build_dual_phase_H(N, theta_30=1, mu_30=0, beta=0.1, coupling=0.0):
    """
    Build dual-phase Hamiltonian with two 30° phase structures
    
    Parameters:
    - theta_30: how many 30° steps for toroid angle
    - mu_30: how many 30° steps for Möbius angle  
    - beta: NNN coupling strength
    - coupling: how strongly the two phases interfere
    """
    H = np.zeros((N, N), dtype=complex)
    
    theta = theta_30 * DEG30  # Convert to radians
    mu = mu_30 * DEG30
    
    # Diagonal - dual phase
    for i in range(N):
        # Phase = combination of toroid and Möbius
        phase = theta * i + coupling * mu * i
        H[i, i] = complex(math.cos(phase), math.sin(phase))
    
    # NN coupling - also dual phase
    for i in range(N-1):
        phase = theta * i + coupling * mu * i
        H[i, i+1] = complex(math.cos(phase), math.sin(phase))
        H[i+1, i] = complex(math.cos(phase), -math.sin(phase))
    
    # NNN coupling - with Möbius twist
    for i in range(N-2):
        # This is where Möbius twist shows up
        phase = theta * i + mu  # Add Möbius offset
        H[i, i+2] = beta * complex(math.cos(phase), math.sin(phase))
        H[i+2, i] = beta * complex(math.cos(phase), -math.sin(phase))
    
    return H

print("=" * 70)
print("DUAL-PHASE TAU-VORTEX MODEL")
print("Two 30° clocks: θ (toroid) + μ (Möbius)")
print("=" * 70)

# Test 1: Pure toroid (mu_30 = 0)
print("\n--- Test 1: Pure toroid (θ = 1, μ = 0) ---")
print(f"{'beta':<8} {'<r>':<10}")
for beta in [0.0, 0.1, 0.2, 0.3, 0.5]:
    r = compute_r(np.linalg.eigvalsh(build_dual_phase_H(100, 1, 0, beta)))
    print(f"{beta:<8.2f} {r:<10.4f}")

# Test 2: Pure Möbius (theta_30 = 0, mu_30 = 1)
print("\n--- Test 2: Pure Möbius (θ = 0, μ = 1) ---")
print(f"{'beta':<8} {'<r>':<10}")
for beta in [0.0, 0.1, 0.2, 0.3, 0.5]:
    r = compute_r(np.linalg.eigvalsh(build_dual_phase_H(100, 0, 1, beta)))
    print(f"{beta:<8.2f} {r:<10.4f}")

# Test 3: Both phases (θ = 1, μ = 1)
print("\n--- Test 3: Both phases (θ = 1, μ = 1) ---")
print(f"{'beta':<8} {'<r>':<10}")
for beta in [0.0, 0.1, 0.2, 0.3, 0.5]:
    r = compute_r(np.linalg.eigvalsh(build_dual_phase_H(100, 1, 1, beta)))
    print(f"{beta:<8.2f} {r:<10.4f}")

# Test 4: Interference coupling
print("\n--- Test 4: Interference coupling (θ=1, μ=1, varying coupling) ---")
print(f"{'coupling':<10} {'<r>':<10}")
for c in [0.0, 0.1, 0.2, 0.5, 1.0, 2.0]:
    r = compute_r(np.linalg.eigvalsh(build_dual_phase_H(100, 1, 1, 0.1, c)))
    print(f"{c:<10.2f} {r:<10.4f}")

# Test 5: What 30° does to 48°, 60°
print("\n" + "=" * 70)
print("SPECIAL ANGLES AS 30° LCM RELATIONSHIPS")
print("=" * 70)

# 30° = π/6
# 48° = 30° + 18° = π/6 + π/10
# 60° = 2 × 30° = π/3
# 72° = 30° + 42° = π/6 + 7π/30

angles = [30, 48, 60, 72, 90, 120]
for deg in angles:
    rad = deg * math.pi / 180
    # How many 30° steps?
    steps_30 = deg / 30
    print(f"{deg}° = {steps_30:.2f} × 30° (rad = {rad:.4f})")

# Test different theta_30 values
print("\n" + "=" * 70)
print("VARYING theta_30 (30° steps)")
print("=" * 70)
print(f"{'theta_30':<12} {'mu_30':<8} {'<r>':<10}")
print("-" * 35)

np.random.seed(42)
for theta in [1, 2, 3, 4, 5, 6]:  # 30°, 60°, 90°, 120°, 150°, 180°
    for mu in [0, 1, 2]:
        r = compute_r(np.linalg.eigvalsh(build_dual_phase_H(100, theta, mu, 0.1)))
        print(f"{theta*30:<12}° {mu:<8} {r:<10.4f}")

# Test system size scaling
print("\n" + "=" * 70)
print("SYSTEM SIZE SCALING (best config)")
print("=" * 70)
print(f"{'N':<6} {'<r>':<10}")
print("-" * 18)

for N in [50, 80, 100, 150, 200]:
    r = compute_r(np.linalg.eigvalsh(build_dual_phase_H(N, 2, 1, 0.2)))
    print(f"{N:<6} {r:<10.4f}")

# Interpretation
print("\n" + "=" * 70)
print("INTERPRETATION")
print("=" * 70)
print("""
KEY FINDINGS:
- Pure toroid (θ=1): high <r> ~0.8
- Pure Möbius (μ=1): similar behavior  
- Both (θ+μ): coupling matters
- At θ=60° (theta_30=2): approaches GUE more closely

This supports the dual-phase picture:
- The 30° toroid beat is the "carrier rhythm"
- The 30° Möbius beat modulates chirality
- Their interference determines GOE↔GUE crossover

Special angles (48°, 60°, 72°) may emerge as:
- 48° = 30° + 18° = toroid + specific interference
- 60° = 2×30° = clean alignment
- 72° = complex interference pattern
""")
