# Hailo — Hailo AI Software Suite (structural dataflow NPU)

> The efficiency king of edge vision. Hailo maps each network layer to physical nodes on the chip so data flows like an assembly line, eliminating the memory-bottleneck traffic of a GPU — and it powers the Raspberry Pi AI HAT+.

| | |
|---|---|
| **Founded / HQ** | 2017 · Tel Aviv, Israel (Orr Danon, Avi Baum) |
| **Architecture** | Hardwired **structural dataflow** NPU |
| **Edge flagship** | Hailo-10H (GenAI-capable) |
| **Software stack** | Hailo AI Software Suite (HailoRT, TAPPAS, Dataflow Compiler, Model Zoo) |
| **Primary market** | Smart cameras, automotive, retail, smart cities |
| **Strategic edge** | Best performance-per-watt for CV; mature ecosystem; 10,000+ monthly developers |

## History
Founded in 2017, Hailo became the most widely adopted independent edge-AI accelerator, in part by powering Raspberry Pi's AI accessories. It has raised **more than $340M** to date; the **April 2, 2024 $120M Series C extension** lifted its valuation to ~$1.2B.

## Architecture
Hailo's **structural dataflow** design compiles a neural network directly onto the silicon's compute/memory fabric. Because intermediate activations stay on-chip and stream between layers, Hailo avoids the constant DRAM round-trips of a GPU — the source of its class-leading efficiency (Hailo-10H: ~16 TOPS/W). The trade-off: custom (non-Model-Zoo) models must be compiled and quantized through the Dataflow Compiler.

## Flagship products (verified)
| Product | AI perf | Precision | Memory | Power | Notes |
|---|---|---|---|---|---|
| **Hailo-8** | 26 TOPS | INT8 | on-chip (no DRAM) | ~2.5 W | mature CV workhorse |
| **Hailo-8L** | 13 TOPS | INT8 | on-chip | low | entry level |
| **Hailo-10H** | 40 / 20 TOPS | INT4 / INT8 | 4/8 GB on-module | ~2.5 W typ | GenAI; GA Jul 22, 2025; AEC-Q100 G2 |

The **Hailo-10H** powers the **Raspberry Pi AI HAT+ 2** ($130, Jan 15, 2026).

## Software stack
**Hailo AI Software Suite** — HailoRT (runtime), TAPPAS (GStreamer pipelines), Hailo Dataflow Compiler, Hailo Model Zoo; integrates TF/PyTorch/ONNX/Keras on x86/ARM hosts. Suite: [hailo.ai/products/hailo-software/hailo-ai-software-suite](https://hailo.ai/products/hailo-software/hailo-ai-software-suite/) · GitHub: [github.com/hailo-ai](https://github.com/hailo-ai).

## Latest news (2025–2026)
- **Jul 22, 2025:** general availability of the **Hailo-10H** with on-device generative AI. *(Hailo newsroom.)*
- **Jan 15, 2026:** Raspberry Pi **AI HAT+ 2** (Hailo-10H) launched.
- Integrations with HP (M.2 AI Accelerator card) and Fujitsu.

> **Independent note:** CNX Software's hands-on with the AI HAT+ 2 found the Raspberry Pi 5 CPU sometimes *matched* the Hailo-10H on raw LLM token generation; the accelerator's real win is **offloading** (total system power ~7.2–7.6 W with Hailo vs ~10.2–10.6 W CPU-only). Vendor figures cite first-token <1 s and ~10 tokens/s on 2B-param LLMs.
