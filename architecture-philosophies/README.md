# Architecture Philosophies

Every AI chip is an answer to one question: **how do you move the math and the data so the network runs fast without burning energy shuffling bytes?** The "memory wall" — the cost of moving data between memory and compute — dominates AI energy use, and each philosophy attacks it differently. Understanding these six approaches explains why the [companies](../companies/README.md) look so different.

## 1. Von Neumann / SIMT GPU
**Who:** NVIDIA (Jetson). **How:** thousands of threads (Single-Instruction, Multiple-Thread) execute in lockstep, with data passing through multi-level caches to Tensor Cores. **Strength:** total generality — any model, any precision, the richest toolchain (CUDA). **Cost:** the constant data movement through the cache hierarchy is power-hungry relative to fixed-function designs.

## 2. Heterogeneous NPU SoC
**Who:** Qualcomm (Hexagon), SiMa.ai (MLSoC), Ambarella (CVflow). **How:** a fixed-function matrix/tensor engine sits beside CPU cores and (often) an image-signal processor on one die, so vision + control + AI run together. **Strength:** whole-application efficiency; great for real systems that aren't pure deep learning. **Cost:** less flexible than a GPU for arbitrary research models.

## 3. Structural dataflow
**Who:** Hailo, MemryX, Blaize (GSP). **How:** the network's layers are **mapped directly onto physical compute/memory nodes**; activations stream layer-to-layer on-chip like an assembly line, so weights and intermediates rarely touch external DRAM. **Strength:** excellent performance-per-watt for CV. **Cost:** custom models must be compiled/quantized to fit the fabric.

## 4. Digital in-memory computing (D-IMC)
**Who:** Axelera (Metis/Europa). **How:** multiply-accumulate happens **inside the SRAM array**, in the digital domain — bypassing the memory wall while avoiding analog noise. **Strength:** high throughput-per-watt and per-dollar for dense vision. **Cost:** newer toolchains; on-chip SRAM caps model size.

## 5. Analog in-memory computing
**Who:** EnCharge (charge-domain), Mythic (embedded flash). **How:** the math is performed in the **analog domain** within memory cells — summing charge or current — with all weights stored on-chip. **Strength:** potentially the best energy efficiency of all (Mythic claims ~120 TOPS/W for a next-gen part; EnCharge ~20× perf/watt). **Cost:** analog precision/calibration is the historical challenge; EnCharge's charge-domain approach specifically targets that. *(Both companies' headline numbers are vendor claims pending independent benchmarks.)*

## 6. Deterministic LPU
**Who:** Groq. **How:** **no caches, no branch predictors, no out-of-order execution** — the compiler schedules every operation and data movement ahead of time, so latency is perfectly predictable. **Strength:** lowest-latency large-model inference. **Cost:** tiny on-chip SRAM means a big model is sharded across many chained cards.

## 7. RISC-V tensor grid
**Who:** Tenstorrent (Tensix). **How:** a grid of cores combining **RISC-V** with matrix/vector engines, programmable down to **open-source bare-metal kernels**. **Strength:** openness and flexibility. **Cost:** the developer owns more of the low-level optimization.

## Quick map
| Philosophy | Beats the memory wall by… | Trade-off |
|---|---|---|
| SIMT GPU | brute-force parallelism + caches | power |
| Heterogeneous NPU | co-locating CV/AI/control | flexibility |
| Structural dataflow | keeping activations on-chip | model fit/compile |
| Digital IMC | computing inside SRAM (digital) | model size, tooling maturity |
| Analog IMC | computing inside memory (analog) | precision/calibration |
| Deterministic LPU | compile-time scheduling | SRAM capacity → card chaining |
| RISC-V grid | open programmable cores | low-level effort |

➡️ See these philosophies embodied in the [company profiles](../companies/README.md).
