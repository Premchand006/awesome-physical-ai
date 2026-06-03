# Qualcomm — AI Hub / AI Stack (Hexagon NPU)

> The generalist that scales **horizontally** across billions of consumer devices. Qualcomm doesn't chase niche industrial sockets; it makes on-device AI ubiquitous on phones, PCs, and cars — and is now pushing into the data center.

| | |
|---|---|
| **Founded / HQ** | 1985 · San Diego, CA |
| **Architecture** | Heterogeneous Hexagon NPU (scalar + vector + tensor) |
| **Edge flagship** | Snapdragon (mobile / PC / automotive) |
| **Software stack** | Qualcomm AI Stack / **Qualcomm AI Hub** (QNN, LiteRT, ONNX RT) |
| **Primary market** | Mobile, PC, automotive — now data center |
| **Strategic edge** | Total integration across consumer scale; 150+ optimized models one click away |

## History
Qualcomm built modern mobile (Snapdragon SoCs, modems), then layered AI on top via the **Hexagon** DSP/NPU. The **Qualcomm AI Hub** (2024→) turned that into a developer funnel: pick a model, get it optimized for a target Snapdragon device, deploy.

## Architecture
The **Hexagon NPU** is heterogeneous — scalar, vector, and tensor units (a 12+8+1-style configuration) supporting INT2/4/8/16 and FP8/16. It is a Von Neumann design tuned for transformer and CNN inference at mobile power.

## Flagship products (verified)
| Product | Role | Notes |
|---|---|---|
| **Snapdragon (Hexagon NPU)** | mobile/PC/auto edge inference | INT2–16, FP8/16 |
| **AI200** | data-center inference (2026) | 768 GB LPDDR/card; 160 kW racks |
| **AI250** | data-center inference (2027) | near-memory compute; vendor-claimed >10× effective bandwidth |

## Software stack
**Qualcomm AI Hub** hosts **150+ pre-optimized models** with export to **QNN**, **LiteRT**, or **ONNX Runtime**. Docs: [docs.qualcomm.com](https://docs.qualcomm.com/) · [aihub.qualcomm.com](https://aihub.qualcomm.com/).

## Latest news (2025–2026)
- **Oct 27, 2025:** Qualcomm announced **AI200 (2026)** and **AI250 (2027)** data-center inference accelerators; the stock rose ~20% on the news. Saudi Arabia's **HUMAIN** committed 200 MW of deployments from 2026. *(Qualcomm newsroom; DCD; Tom's Hardware.)*
- Qualcomm agreed to acquire **Alphawave** (~$2.4B) to bolster data-center connectivity IP.

**Caveat:** the AI200/AI250 are data-center parts; Qualcomm's edge story remains Snapdragon + the AI Hub.
