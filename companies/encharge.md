# EnCharge AI — analog charge-domain in-memory computing

> A Princeton spin-out betting that **charge-domain** analog compute (not noisy current-based analog) can deliver ~20× the performance-per-watt of digital accelerators for on-device AI — including GenAI on laptops.

| | |
|---|---|
| **Founded / HQ** | 2022 · Santa Clara, CA (Princeton spin-out; Naveen Verma) |
| **Architecture** | **Analog charge-domain in-memory computing (IMC)** |
| **Edge flagship** | EN100 |
| **Software stack** | EnCharge software suite |
| **Primary market** | AI PCs, laptops, workstations |
| **Strategic edge** | ~20× performance-per-watt via precise charge-based compute |

## History
Spun out of Princeton in 2022, EnCharge has raised **$144M total**, including a **$100M Series B (Feb 2025, led by Tiger Global)** and an **$18.6M DARPA grant**. Investors include Samsung Ventures, IQT, RTX Ventures, and HH-CTBC (Foxconn/CTBC).

## Architecture
EnCharge's IMC uses **metal-wire switched-capacitor (charge-based)** compute rather than current-based analog. Charge is more robust to process/temperature variation than current, which the company argues solves analog AI's historical precision problem while keeping its efficiency.

## Flagship products (verified)
| Product | AI perf | Power | Memory | Notes |
|---|---|---|---|---|
| **EN100 (M.2)** | 200+ TOPS | 8.25 W | up to 128 GB LPDDR (272 GB/s) | for laptops |
| **EN100 (PCIe)** | ~1 PetaOPS | higher | — | 4 NPUs; workstation |

~30 TOPS/mm² density (vendor figure).

## Software stack
EnCharge software suite for compiling/deploying models to the EN100. Company: [enchargeai.com](https://www.enchargeai.com/).

## Latest news (2025–2026)
- **May 29, 2025:** announced the **EN100**, an industry-first analog in-memory accelerator for on-device AI; vendor cites **up to ~20× better performance per watt**. *(Business Wire.)*
- **Feb 2025:** **$100M** Series B (Tiger Global).

**Caveat:** EN100 performance and the 20× claim are **vendor-sourced** for a new part; await independent benchmarks.
