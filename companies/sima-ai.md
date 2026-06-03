# SiMa.ai — Palette (software-centric heterogeneous MLSoC)

> The "software-first" edge-AI company. SiMa.ai's pitch is that you can port legacy C/C++ code and run it **alongside** an AI network on a single SoC, with a one-click toolchain — ideal for messy real-world robotics and industrial pipelines.

| | |
|---|---|
| **Founded / HQ** | 2018 · San Jose, CA (Krishna Rangasayee) |
| **Architecture** | Heterogeneous **MLSoC** (MLA + Arm + ISP on one chip) |
| **Edge flagship** | MLSoC **Modalix** (M50 / M100 / M200) |
| **Software stack** | **Palette** SDK + **Edgematic** (no-code) on "SiMa.ai ONE" |
| **Primary market** | Robotics, industrial automation, aerospace/defense, smart vision, healthcare |
| **Strategic edge** | Whole-application acceleration; legacy code + AI network on one SoC |

## History
Founded in 2018, SiMa.ai shipped its first 50-TOPS MLSoC for computer vision, then expanded to multimodal generative AI with **Modalix**. It has raised **$355M total**, including an **$85M round on Aug 1, 2025** (led by Maverick Capital, with StepStone joining).

## Architecture
The **MLSoC** integrates a Machine Learning Accelerator (MLA), Arm application cores, and an image-signal processor on one die. The selling point is *heterogeneous* execution — classical CV/control code (C/C++) runs next to the neural network without leaving the chip — which suits pipelines that aren't pure deep learning.

## Flagship products (verified)
| Product | AI perf | Precision | Power | Notes |
|---|---|---|---|---|
| **MLSoC (Gen 1)** | 50 TOPS | INT8 | low | vision focus |
| **Modalix M50/M100/M200** | 50 TOPS (M50) | BF16 + INT8/INT16 | <10 W | multimodal/GenAI; now shipping |

A **system-on-module** (with Enclustra) was announced March 10, 2025.

## Software stack
**Palette** (full SDK) plus **Edgematic**, a no-code/low-code builder, on the unified **SiMa.ai ONE** platform; emphasizes "push-button" porting of existing pipelines. GitHub: [github.com/sima-ai](https://github.com/sima-ai).

## Latest news (2025–2026)
- **Aug 1, 2025:** **$85M** raise (Maverick Capital; StepStone), total **$355M**.
- **Mar 10, 2025:** Modalix SoM with Enclustra.

**Caveat:** the "one-click legacy porting" and heterogeneous-pipeline advantages are vendor positioning; independent multi-stream benchmarks are limited — validate on your workload.
