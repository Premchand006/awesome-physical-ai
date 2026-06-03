# NVIDIA — CUDA + Jetson (SIMT GPU)

> The full-stack incumbent. NVIDIA frames Physical AI as a **"three-computer" problem** — train in the cloud (DGX), simulate and generate synthetic data (Omniverse + Cosmos), and deploy on the robot (Jetson) — and owns silicon and software at every stage.

| | |
|---|---|
| **Founded / HQ** | 1993 · Santa Clara, CA |
| **Architecture** | Von Neumann / SIMT GPU + Tensor Cores |
| **Edge flagship** | Jetson AGX Thor (Jetson T5000 module) |
| **Software stack** | CUDA, JetPack 6/7, TensorRT, DeepStream, Isaac ROS, Holoscan, Cosmos |
| **Primary market** | Cloud data centers **and** robotics/edge |
| **Strategic edge** | End-to-end software moat (CUDA + 2.2M+ developers); unrivaled training-to-deployment continuity |

## History
NVIDIA created the consumer GPU category in the 1990s, then turned the GPU into the substrate of modern AI with **CUDA (2006)**. Its Jetson embedded line (2014→) brought that same stack to robots and cameras. By 2025 the company had pivoted hard into **Physical AI and robotics** as its next growth vector; CEO Jensen Huang used his **CES 2025 keynote (Jan 6, 2025)** to argue that "the ChatGPT moment for general robotics is just around the corner."

## Architecture
Jetson uses the same **SIMT (Single-Instruction, Multiple-Thread) GPU** cores and **Tensor Cores** as NVIDIA's data-center parts, scaled down in power. Work is dispatched across thousands of threads, with data moving through cache hierarchies to the compute units — a highly evolved Von Neumann design. The advantage is generality (any model, any precision) and the CUDA toolchain; the cost is higher power than fixed-function NPUs.

## Flagship products (verified)
| Product | AI perf | Precision | Memory | Power | Price |
|---|---|---|---|---|---|
| **Jetson AGX Thor / T5000** | up to 2,070 TFLOPS (sparse) | FP4 | 128 GB LPDDR5X | 40–130 W | $3,499 dev kit (~$2,999 module) |
| **Jetson T4000 (module)** | ~1,200 TFLOPS | FP4 | 64 GB | 40–75 W | ~$1,999 |
| **Jetson Orin Nano Super** | 67 TOPS | INT8 | 8 GB | 7–25 W | $249 |
| **Jetson AGX Orin** | up to 275 TOPS | INT8 | 32/64 GB | 15–60 W | $$$ |

Thor's T5000 pairs a Blackwell GPU (2,560 CUDA cores, 96 fifth-gen Tensor Cores) with a 14-core Arm Neoverse-V3AE CPU; NVIDIA cites **7.5× the AI compute and 3.5× the energy efficiency of AGX Orin**.

## Software stack ("the CUDA equivalent" — it *is* CUDA)
**CUDA** (parallel compute), **TensorRT** (inference optimization), **DeepStream** (GStreamer-based video analytics), **Isaac ROS** (GPU-accelerated ROS 2 via NITROS), **Holoscan** (low-latency sensor AI), and **Cosmos** world foundation models. Docs: [developer.nvidia.com/embedded/jetson-modules](https://developer.nvidia.com/embedded/jetson-modules) · [Jetson AI Lab](https://www.jetson-ai-lab.com/).

## Latest news (2025–2026)
- **Aug 2025:** Jetson AGX Thor reached general availability at **$3,499**; Boston Dynamics' all-electric Atlas runs Thor. *(NVIDIA Newsroom, Aug 2025.)*
- **CES 2026 / GTC 2026:** continued push on humanoid foundation models (Isaac GR00T N-series) and the Vera Rubin platform.
- **Dec 2025:** NVIDIA struck a ~$20B deal to license Groq's LPU architecture and acqui-hire its team (see [datacenter-context.md](datacenter-context.md)) — framing contested and under U.S. Senate antitrust review.

**Caveat:** Thor's 2,070 TFLOPS is an **FP4 sparse** figure; it is not comparable to INT8 TOPS quoted by edge NPUs.
