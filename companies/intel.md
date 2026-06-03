# Intel — OpenVINO (heterogeneous CPU / NPU / GPU)

> The "use the silicon you already own" play. OpenVINO runs accelerated inference across Intel **CPU, integrated GPU, NPU (Core Ultra), and Arc** GPUs, and is increasingly capable for on-device generative AI.

| | |
|---|---|
| **Founded / HQ** | 1968 · Santa Clara, CA |
| **Architecture** | Heterogeneous CPU + NPU + iGPU/dGPU |
| **Edge flagship** | Core Ultra (NPU) + Arc / Arc Pro GPUs |
| **Software stack** | OpenVINO (+ OpenVINO GenAI, NNCF, OVC) |
| **Primary market** | x86 edge servers, AI PCs, embedded |
| **Strategic edge** | Zero new hardware; mature tooling and notebooks; broad device coverage |

## History
Intel entered edge AI through software (OpenVINO, first released 2018) and a string of acquisitions (Movidius VPUs, Habana/Gaudi for the data center). With **Core Ultra** (2024→) it brought a dedicated **NPU** to mainstream x86, making "AI PC" inference a first-class OpenVINO target.

## Architecture
OpenVINO abstracts a **heterogeneous** target: the same model can run on CPU (via the oneDNN/MLAS-style kernels), the iGPU, the NPU, or an Arc GPU, with an `AUTO` device that distributes work. This is a Von Neumann substrate, but the NPU adds a fixed-function matrix engine for efficiency.

## Flagship products (verified)
| Product | Role | Notes |
|---|---|---|
| **Core Ultra (NPU)** | on-device AI PC inference | INT8/FP16; `torch.compile` NPU path |
| **Arc / Arc Pro GPUs** | edge inference / workstation | incl. Arc Pro B-series |
| **Gaudi** | data-center training/inference | separate from the edge line |

## Software stack (the "CUDA equivalent" for Intel)
**OpenVINO** (latest **2025.4**, 2026.0 in transition). **OpenVINO GenAI** is the LLM/VLM path; **NNCF** handles INT8/INT4 compression; **OVC** converts models. Repo: [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) · notebooks: [openvino_notebooks](https://github.com/openvinotoolkit/openvino_notebooks).

> ⚠️ **Deprecations (flag these):** the legacy **Model Optimizer**, the **`openvino-dev`** package, and the **Open Model Zoo** are removed; NNCF `create_compressed_model()` is deprecated → use `nncf.quantize()`. See [../renames-and-deprecations.md](../renames-and-deprecations.md).

## Latest news (2025–2026)
- **2025:** OpenVINO 2025.x added a GGUF reader (run llama.cpp models), Mixture-of-Experts support (Qwen3-30B, GPT-OSS-20B), NPU `torch.compile`, and Windows ML gold support.
- Ongoing strategy debate around Intel's foundry and AI-accelerator roadmap (Gaudi vs the broader market).

**Caveat:** OpenVINO's strength is breadth and zero added hardware cost; for the heaviest workloads a dedicated GPU/NPU card still wins on raw throughput.
