# Renames & Deprecations (2024–2026)

The edge / Physical-AI space renamed, deprecated, and discontinued a lot recently. This page is the cheat-sheet so you don't act on stale information. Verify against the linked source before relying on any single line.

## Discontinued / abandoned
- **Google Coral / Edge TPU — effectively abandoned** (community consensus, not an official Google EOL). No updates 2021–2025; the Gasket PCIe driver won't build on Linux ≥ 6.4; the `google/gasket-driver` repo was archived April 2026. Use **Hailo** instead.
- **Raspberry Pi AI Kit — out of production.** Replaced by the **AI HAT+** (Hailo-8/8L) and the **AI HAT+ 2** (Hailo-10H, 40 TOPS INT4, 8 GB, GenAI on Pi 5; launched Jan 15, 2026 at $130).

## Renamed
- **TensorFlow Lite → LiteRT** (Google, Sept 4, 2024); `.tflite` format unchanged; `tf.lite` decoupled into a standalone LiteRT repo (TF 2.20, Aug 2025).
- **Groq → "NVIDIA Groq"** — NVIDIA licensed Groq's LPU architecture and acqui-hired its team (Dec 2025); product rebranded **Groq 3 LPX**. *(Framing is contested and under U.S. Senate antitrust review — see [companies/datacenter-context.md](companies/datacenter-context.md).)*

## Deprecated within an active product
- **OpenVINO:** the legacy **Model Optimizer**, the **`openvino-dev`** package, and the **Open Model Zoo** are removed; NNCF `create_compressed_model()` is deprecated → use `nncf.quantize()`.
- **ONNX Runtime:** the **ArmNN Execution Provider** was removed in 1.26 (use the CPU EP with KleidiAI, or QNN for Qualcomm).

## Corporate status changes
- **Blaize** is now **public** (NASDAQ: **BZAI**, Jan 14 2025) — no longer a private startup.
- **Ambarella** is reportedly **exploring a sale** (Bloomberg, June 2025) — unconfirmed.
- **Mythic** revived with a **$125M** round (Dec 2025) after a near-collapse in 2022.

## ROS 2 release status
- Current release **Kilted Kaiju** (May 23, 2025) is **non-LTS** (EOL Nov 2026).
- **Lyrical Luth** is scheduled as the next **LTS** (~May 2026, 5-year support); ship status as of mid-2026 is ambiguous.
- Most recent shipped **LTS** is **Jazzy Jalisco** (May 2024, EOL 2029). Pick an LTS for production robots.

## Quick "if you read X, know Y"
| If a source says… | Today it's… |
|---|---|
| "TensorFlow Lite" | **LiteRT** (`.tflite` unchanged) |
| "buy a Coral / Edge TPU" | **abandoned** — use Hailo |
| "Raspberry Pi AI Kit" | **AI HAT+** or **AI HAT+ 2** |
| "Groq (independent)" | **NVIDIA Groq** (licensed + acqui-hired) |
| "Blaize, the startup" | **public company** (NASDAQ: BZAI) |
| "OpenVINO Model Optimizer" | **OVC** + `optimum-intel` |

*Spot something stale? [Open a PR](CONTRIBUTING.md) — keeping this current is one of the most valuable contributions here.*
