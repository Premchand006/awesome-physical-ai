# DeepX — DXNN SDK (heterogeneous edge NPU)

> A fast-rising Korean NPU startup chasing "GPU-level accuracy at a fraction of the power" for robots, cameras, and AI PCs.

| | |
|---|---|
| **Founded / HQ** | 2018 · South Korea (fabless; Lokwon Kim) |
| **Architecture** | Heterogeneous NPU |
| **Edge flagship** | DX-M1 |
| **Software stack** | **DXNN** SDK |
| **Primary market** | Robotics, IP cameras, AI PCs, edge servers |
| **Strategic edge** | High TOPS-per-watt with "intelligent quantization" preserving accuracy |

## History
Founded in 2018, DeepX moved from prototypes to **mass production around April 2026** and is planning a **2026 IPO** at a reported ~KRW 1T (~$700M) valuation. It featured prominently at **CES 2026** (booth #8945) alongside NVIDIA, Samsung, and Qualcomm.

## Architecture
A heterogeneous NPU paired with **IQ8 "intelligent quantization"**, which DeepX claims recovers near-FP32 accuracy at INT8 — addressing the usual accuracy hit of edge quantization.

## Flagship products (verified)
| Product | AI perf | Power | Form factor | Notes |
|---|---|---|---|---|
| **DX-V1** | sub-1 W vision | <1 W | embedded | single-camera |
| **DX-V3** | multi-camera | 1–3 W | embedded | |
| **DX-M1** | 25 TOPS | 3–5 W | M.2 2280 | IQ8 quantization |
| **DX-H1** | server-class | higher | card | data-center edge |

Vendor Model Zoo cites 3,523 FPS MobileNetV2, 1,186 FPS ResNet50, 366 FPS YOLOv8L. **DX-M2** is in development on 2 nm. The Radxa **AICore DX-M1** module is listed at ~$187.

## Software stack
**DXNN** SDK and Model Zoo. GitHub: [github.com/DEEPX-AI](https://github.com/DEEPX-AI).

## Latest news (2025–2026)
- **~Apr 2026:** mass production began.
- **Apr 14, 2026:** joint development with **Hyundai Motor Group** on generative-AI robots.
- **CES 2026:** partner Sixfab's ALPON X5 gateway (DX-M1) won a CES Best of Innovation award.

**Caveat:** FPS and accuracy figures are vendor-sourced; independent benchmarks are still emerging.
