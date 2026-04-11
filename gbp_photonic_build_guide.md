# GBP Photonic Processor — Proof of Concept Build Guide

**Budget: ~$60–100 | Build time: 1 afternoon**  
HistoryViper / github.com/historyViper/mod30-spinor

---

## What You're Building

A physical optical system that separates white light into 8 spectral bands corresponding to the 8 Wilson loop paths of the GBP framework. Each band exits at a geometrically distinct angle derived from `sin²(r·π/15)`. You verify these angles match GBP predictions — simultaneously validating the optical paper and demonstrating the core routing mechanism of a photonic processor.

**This is Experiment 1 of 3:**
1. ✅ Band separation + angle verification (this guide)
2. Tilt-based path routing (computation)
3. Camera readout + interference pattern analysis

---

## Parts List

| Item | Source | Est. Cost |
|------|--------|-----------|
| Full spectrum white LED (5000K–6500K) | Amazon / hardware store | $3–8 |
| Glass equilateral prism, 25–50mm | Amazon / AliExpress / educational supplier | $8–15 |
| 2× smaller prisms OR prism set | Amazon | $10–15 |
| 3D cinema glasses (circular polarized) | Dollar store / online | $2–5 |
| Small DC motor or hand spinner | Hobby shop / toy store | $3–8 |
| Diffusion screen (tracing paper / wax paper) | Office supply | $1–2 |
| Black cardboard / foam board | Dollar store | $2–3 |
| Binder clips, rubber bands, tape | Already have | $0–2 |
| Arduino Nano (optional, for servo tilts) | Amazon | $5–10 |
| Micro servo × 4 (optional) | Amazon | $8–15 |
| **Total (basic)** | | **~$30–50** |
| **Total (with servo tilts)** | | **~$60–80** |

**Phone camera** — use what you have. Any smartphone from the last 5 years works.

---

## The Physics: What You're Looking For

The primary prism separates white light into a spectrum. GBP predicts the 8 Wilson loop paths correspond to 8 spectral bands with boundary projection coefficients:

```
Band  r    angle     sin²(r·π/15)   approx color
────  ──   ───────   ────────────   ─────────────
1     1    12°       0.0432         deep red / IR edge
2     29   348°      0.0432         deep red (mirror)
3     13   156°      0.1654         orange-red
4     17   204°      0.1654         orange-red (mirror)
5     11   132°      0.5523         blue-green
6     19   228°      0.5523         blue-green (mirror)
7     7    84°       0.9891         UV-violet edge
8     23   276°      0.9891         UV-violet (mirror)
```

Mirror pairs have identical sin² values and should land at symmetrically opposite positions on the output screen. **This symmetry is the experimental signature you're looking for.**

The sum of any 4 bands (one per sin² tier) = **1.75 exactly**. You can verify this from the intensity distribution on your screen.

---

## Build Instructions

### Step 1: The Collimated Light Source (20 min)

You need a narrow beam of white light — not a flood.

1. Cut a 5mm hole in black cardboard
2. Mount the full-spectrum LED behind it, pressed close
3. The cardboard acts as a slit — creates a narrow beam
4. **Test:** In a dark room, you should see a narrow white beam projected on a wall

**Pro tip:** A small LED flashlight with a slit cut from black tape over the lens also works perfectly.

---

### Step 2: Primary Prism Setup (15 min)

1. Mount the primary prism (largest one) on a stable surface — use clay, a binder clip, or tape
2. Aim the narrow white beam at one face of the prism at approximately 30° incidence
3. Adjust until you see a clear rainbow spectrum fan out on the other side
4. Hold your diffusion screen (tracing paper) in the output beam
5. **You should see:** A spread of colors from deep red through to violet

**Mark on the screen with a pencil:** Where does each color band center sit?

---

### Step 3: Secondary Prism Pairs (30 min)

This is where the GBP routing happens.

**Concept:** After the primary prism spreads the spectrum, you position smaller prisms to intercept specific bands.

1. Start with the two edge bands (deep red and UV/violet — the r=1 and r=7 bands)
2. Position a small prism at each edge of the spectrum fan
3. Each small prism deflects its band away from the others onto its own path
4. Use your screen to verify the deflected band is isolated

**Work inward:**
- Edge pair: red + violet (sin² ≈ 0.04 and 0.99)
- Next pair: orange-red + indigo (sin² ≈ 0.16)
- Next pair: yellow-green + blue (sin² ≈ 0.55)
- Center: whatever remains

**GBP prediction to verify:** The two bands in each mirror pair should deflect to positions that are geometrically symmetric around the optical axis. Measure the angles with a protractor or ruler on your screen.

---

### Step 4: The Polarization Wheel (15 min)

This adds the chirality dimension (G = ±1 from the optical paper).

1. Cut the left lens out of your 3D cinema glasses
2. Cut the right lens out
3. Mount them on opposite sides of a small spinning shaft (motor or hand spinner)
4. Position the spinning wheel between the LED and the primary prism

**What this does:**
- When left lens passes: all 8 bands are in G = −1 (LCP) chirality Hilbert space
- When right lens passes: all 8 bands are in G = +1 (RCP) chirality Hilbert space
- Spinning fast: you get 16 effective channels (8 bands × 2 chiralities)
- **GBP prediction:** LCP and RCP bands should produce interference patterns that are mirror images of each other on the output screen

---

### Step 5: Output Screen and Camera (10 min)

1. Mount your diffusion screen (tracing paper works great) at the end of all the paths
2. Place your phone camera behind the screen, lens close to the paper
3. The paper diffuses the light so the camera can see all bands simultaneously
4. Turn off all other lights in the room

**What to capture:**
- Photo of the full band separation pattern
- Note the positions of each of the 8 bands
- Measure distances from center to each band

---

## Measurements: Verifying GBP Predictions

### Measurement 1: Mirror Pair Symmetry

For each mirror pair (r=1/r=29, r=7/r=23, r=11/r=19, r=13/r=17):

```
Distance of r band from center = d₁
Distance of mirror band from center = d₂
GBP predicts: d₁ = d₂ (symmetric)
```

Mark both positions. Measure with a ruler. They should be equal to within your measurement precision.

### Measurement 2: Sin² Intensity Ratio

The brightness of each band on the screen should be proportional to its sin² value:

```
Band r=1  (sin²=0.0432): should be ~4% as bright as r=7 band
Band r=13 (sin²=0.1654): should be ~17% as bright as r=7 band
Band r=11 (sin²=0.5523): should be ~56% as bright as r=7 band
Band r=7  (sin²=0.9891): brightest band (100%)
```

Your phone camera's image can be analyzed with a free app or just visually compared.

### Measurement 3: Four-Tier Sum

Select one band from each tier. Estimate their relative intensities (1–10 scale). Their sum should be proportional to 1.75.

```
Tier 1 intensity (r=1 or r=29):   I₁
Tier 2 intensity (r=13 or r=17):  I₂  
Tier 3 intensity (r=11 or r=19):  I₃
Tier 4 intensity (r=7 or r=23):   I₄

Normalized sum: (I₁ + I₂ + I₃ + I₄) / I₄ should ≈ 1.75
```

---

## Optional: Servo Tilt Programming (Experiment 2 preview)

If you added the Arduino and servos:

1. Mount one servo under each secondary prism
2. Connect to Arduino Nano
3. Upload this simple test sketch:

```cpp
#include <Servo.h>

Servo band1, band2, band3, band4;
// Connect servos to pins 3,5,6,9

void setup() {
  band1.attach(3);  // r=1 band (red)
  band2.attach(5);  // r=13 band (orange)
  band3.attach(6);  // r=11 band (blue-green)
  band4.attach(9);  // r=7 band (violet)
  Serial.begin(9600);
}

void loop() {
  // Tilt all bands to 90° (straight through)
  band1.write(90); band2.write(90);
  band3.write(90); band4.write(90);
  delay(1000);
  
  // Tilt each by +5° (slight path shift = different calculation)
  band1.write(95); band2.write(85);
  band3.write(95); band4.write(85);
  delay(1000);
  
  // Each tilt configuration = different matrix operation
}
```

Each tilt combination corresponds to a different computation. The output screen pattern changes. The camera reads the result.

---

## What Success Looks Like

**Minimum success (Experiment 1):**
- You can see 4+ distinct color bands separated by the prism system
- Mirror pair bands are visibly symmetric around center
- The UV/violet and deep red edge bands are the least bright (low sin²)
- The blue-green bands are medium bright (mid sin²)

**Strong success:**
- You measure 8 distinct bands
- Mirror pair positions agree within 5% tolerance
- Intensity ratios approximately match sin² predictions
- LCP / RCP show mirror interference patterns

**Publication-ready success:**
- All 8 bands measured
- Mirror symmetry confirmed to <2% tolerance
- Tier sum ratio = 1.75 ± 0.05
- Photographs documenting all measurements

---

## Data Recording Template

```
Date: ___________
Light source: ___________
Primary prism size: ___________
Screen distance: ___ cm

Band positions (measured from center, in cm):
  r=1  (deep red):   left ___ / right ___
  r=7  (UV/violet):  left ___ / right ___
  r=11 (blue-green): left ___ / right ___
  r=13 (orange):     left ___ / right ___

Mirror pair symmetry:
  Pair (1,29):  d₁=___ d₂=___ ratio=___
  Pair (7,23):  d₁=___ d₂=___ ratio=___
  Pair (11,19): d₁=___ d₂=___ ratio=___
  Pair (13,17): d₁=___ d₂=___ ratio=___

Intensity estimates (1–10):
  r=1: ___  r=7: ___  r=11: ___  r=13: ___

Four-tier sum / I₄ = ___ (target: 1.75)

Notes: ___________
```

---

## Troubleshooting

**Can't see the rainbow:** LED too dim or beam not collimated enough. Try a narrower slit or move LED closer. Darkening the room helps dramatically.

**Bands overlap:** Prism angle too shallow or screen too close. Move screen further away — more distance = more separation.

**Can't distinguish 8 bands:** Start with 4 (just the most separated ones). You don't need all 8 for a valid proof of concept.

**Mirror pairs not symmetric:** Check that your primary prism is centered on the beam axis. Slight off-axis entry breaks the symmetry.

**Polarizer wheel not working:** 3D glasses only work with circular polarization. Some cheap 3D glasses use linear polarization. Check the type before buying.

---

## Next Steps After Experiment 1

**Experiment 2 — Tilt computation:**
Mount servos under secondary prisms. Show that different tilt angles produce different interference patterns on the output screen. Demonstrate 3+ distinguishable "computation states."

**Experiment 3 — Camera readout:**
Write a simple Python script using OpenCV to read the band positions and intensities from the phone camera in real time. Extract the 8 channel values. Demonstrate that the 8 values can encode a computational result.

**Experiment 4 — Matrix operation:**
Encode a simple 4×4 matrix as prism tilt angles. Input a vector as relative intensity across 4 input bands. Read the matrix-vector product from the output pattern.

---

## Why This Matters

If band angles match GBP predictions, this is simultaneously:

1. **Experimental validation** of the optical paper (vacuum geometric phase, universal gap formula)
2. **Proof of concept** for a genuinely new computing architecture — passive, speed-of-light, zero switching energy
3. **Engineering foundation** for photonic matrix processors that could reduce matrix computation costs by orders of magnitude

The computation happens at the speed of light. The "program" is the physical geometry. The result is read optically. No transistors switch. No electrons move through resistances. No heat.

For AI matrix operations specifically — transformer attention heads are essentially massive matrix multiplications. If even a fraction of those can be offloaded to optical hardware, the energy and speed implications are significant.

---

*Code and analysis tools: github.com/historyViper/mod30-spinor*  
*Theory: GBP Optical Paper — gbp_optical_paper.md*
