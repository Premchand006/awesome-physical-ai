# Mythic — Mythic ACE (analog compute-in-memory)

> The analog-AI pioneer. Mythic performs neural-network math in the **analog domain inside flash memory cells**, storing all weights on-chip — a radically different bet on efficiency, recently revitalized with $125M in fresh funding.

| | |
|---|---|
| **Founded / HQ** | 2012 · Austin, TX (Dave Fick) |
| **Architecture** | **Analog compute-in-memory** (embedded flash) |
| **Edge flagship** | M1076 Analog Matrix Processor (AMP) |
| **Software stack** | **Mythic ACE** + graph compiler |
| **Primary market** | Edge vision, defense |
| **Strategic edge** | Analog efficiency; all weights stored on-chip (no external memory) |

## History
Founded in 2012, Mythic nearly collapsed in 2022, was rescued by a **$13M round (March 2023)**, and then staged a major comeback with an **oversubscribed $125M round led by DCVC (Dec 17, 2025)**. Customers include **Lockheed Martin**.

## Architecture
**Analog compute-in-memory** runs matrix multiplication directly in **embedded-flash** cells, using analog current summation. Because weights live permanently on-chip, there's no weight-streaming traffic — the route to its efficiency claims. The trade-off historically has been analog precision/calibration.

## Flagship products (verified)
| Product | AI perf | Power | Memory | Notes |
|---|---|---|---|---|
| **M1076 AMP** | 25 TOPS | 3 W | up to 80M weights on-chip | 76 tiles; 40 nm flash |
| **M.2 / PCIe (up to 16 chips)** | up to 400 TOPS | ~75 W | — | scale-out card |

## Software stack
**Mythic ACE** with a graph compiler. Company: [mythic.ai](https://mythic.ai/).

## Latest news (2025–2026)
- **Dec 17, 2025:** **$125M** round led by **DCVC**; Mythic claims a next-gen architecture **~100× more energy-efficient than top GPUs/ASICs** — quantified as **120 TOPS/W** and **17 femtojoules per multiply-accumulate** (≈1,000× less than today's GPUs). *(Mythic press release.)*

**Caveat:** the 120 TOPS/W and 17 fJ/MAC figures are **vendor claims for a next-gen part**, not yet independently benchmarked.
