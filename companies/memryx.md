# MemryX — MemryX SDK (at-memory dataflow)

> The developer's favorite. MemryX pairs an at-memory dataflow accelerator with a genuinely **open-source SDK** and a sub-ten-minute setup — the easiest discrete NPU to actually get running.

| | |
|---|---|
| **Founded / HQ** | spun out of the University of Michigan · USA |
| **Architecture** | At-memory **dataflow** |
| **Edge flagship** | MX3 (M.2 module) |
| **Software stack** | **MemryX SDK** (open-source runtime + compiler + simulator) |
| **Primary market** | Developer / edge vision |
| **Strategic edge** | Easiest onboarding; open-source stack; bit-accurate simulator |

## History
MemryX commercialized University of Michigan research into an at-memory dataflow accelerator, prioritizing developer experience over peak TOPS. Independent reviewers consistently highlight how quickly it runs out of the box.

## Architecture
The **MX3** stores weights on-chip next to the compute (at-memory dataflow), streaming activations between stages. With no external DRAM, it is extremely efficient for small/medium CNNs but **memory-limited for large transformers** (~10.5M 8-bit params/chip).

## Flagship products (verified)
| Product | AI perf | Precision | Memory | Power | Price |
|---|---|---|---|---|---|
| **MX3 (single chip)** | 6 TOPS | 4/8/16-bit + BF16 | on-chip (10.5M params) | low | — |
| **MX3 M.2 module (4 chips)** | 24 TOPS | same | ~42M params total | 6–8 W | ~$149 |
| **MX3 (max interconnect)** | up to 96 TOPS (16 chips) | same | — | — | — |

## Software stack
**MemryX SDK 2.2** — open-source C++/Python runtime, kernel driver, and a **bit-accurate simulator**. Site: [memryx.com](https://memryx.com/) · GitHub: [github.com/memryx](https://github.com/memryx).

## Latest news (2025–2026)
- SDK 2.x with the open runtime and simulator; growing hobbyist adoption.

> **Independent note:** Phoronix and reviewer Anton Maltsev praise the **<10-minute setup** and **truly open-source SDK** (its standout edge), while noting it is **slower than Hailo/Axelera** and constrained on large models. This is one of the few accelerators with genuinely independent hands-on coverage.
