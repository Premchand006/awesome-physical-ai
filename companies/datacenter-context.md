# Datacenter Context — Groq & Tenstorrent

These two aren't edge-device companies, but they define the *other* end of the Physical-AI compute spectrum (training and large-model inference) and illustrate two more architecture philosophies. We include them for context in the [landscape comparison](README.md).

## Groq — deterministic LPU
| | |
|---|---|
| **Founded / HQ** | 2016 · Mountain View, CA (Jonathan Ross, creator of Google's first TPU) |
| **Architecture** | **Deterministic Language Processing Unit (LPU)** |
| **Software** | GroqCompiler / GroqWare |
| **Edge** | Lowest-latency LLM token generation |

Groq's LPU has **no branch predictors, caches, or out-of-order logic** — the **GroqCompiler plans every byte's movement at compile time**, before the chip runs. The original chip carries ~230 MB of on-chip SRAM at ~80 TB/s and **no HBM**, so a large model must be **sharded across hundreds of chained cards**. The payoff is extreme, predictable streaming throughput (vendor figures >1,600 tokens/s on some models; an independent benchmark of ~241 tokens/s on Llama-2-70B).

**Latest news (contested framing):** NVIDIA announced a **~$20B deal (Dec 24, 2025)** widely described as a **non-exclusive license to Groq's LPU architecture plus an acqui-hire** of Jonathan Ross and most engineers; the product was rebranded **"NVIDIA Groq 3 LPX"** for the Vera Rubin platform. U.S. Senators opened an antitrust inquiry (~March 2026) over the "reverse acqui-hire" structure. *Some outlets call it an acquisition; others dispute that — do not assert "NVIDIA acquired Groq" without the qualifier.*

## Tenstorrent — RISC-V Tensix grid
| | |
|---|---|
| **Founded / HQ** | 2016 · Toronto, Canada (led by Jim Keller) |
| **Architecture** | **Tensix core grid (RISC-V + matrix/vector engines)** |
| **Software** | **TT-Metalium** (low-level) / TT-Buda (high-level) |
| **Edge** | Fully open-source, bare-metal kernel programming |

Each **Tensix** core combines RISC-V cores with matrix/vector engines and a hardware packer/unpacker for format conversion. Unlike Groq's fixed deterministic pipeline, Tenstorrent exposes a **programmable, general grid** — and its **bare-metal kernels are fully open source**, positioning it as the open alternative for developers who want low-level control without NVIDIA's licensing model.

## Why they matter for Physical AI
Robots are trained in the cloud before they're deployed at the edge. Groq (fast inference) and Tenstorrent (open training/inference) represent the "train and serve large models" tier that feeds the foundation models and VLA policies which ultimately run on edge silicon like Jetson, Hailo, or SiMa.ai. See [../vla-and-world-models/README.md](../vla-and-world-models/README.md).
