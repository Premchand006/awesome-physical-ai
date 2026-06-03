# Ambarella — CVflow (edge-vision SoC)

> The video-plus-AI specialist. Ambarella combines high-quality video processing with on-chip AI (CVflow), powering security cameras, cars, and robots — and is reportedly exploring a sale.

| | |
|---|---|
| **Founded / HQ** | 2004 · Santa Clara, CA (NASDAQ: AMBA; Fermi Wang) |
| **Architecture** | **CVflow** NPU integrated in a vision SoC |
| **Edge flagship** | N1 / CV5 / CV7 series (N1-655) |
| **Software stack** | CVflow toolkit (**Cooper** dev platform) |
| **Primary market** | Security cameras, automotive, AMRs |
| **Strategic edge** | Tight video + AI integration at very low power |

## History
A long-time video-SoC company (IPO 2012), Ambarella pivoted to edge AI with **CVflow**. It has shipped **30M+ cumulative edge-AI SoCs (March 2025)**, and in 2025 was reported to be exploring strategic options including a sale.

## Architecture
**CVflow** is a vision-optimized NPU embedded alongside Ambarella's image pipeline, so a single SoC handles multi-stream video decode *and* AI inference. **CVflow 3.0** supports generative models from 0.5–34B parameters.

## Flagship products (verified)
| Product | Capability | Power | Notes |
|---|---|---|---|
| **N1-655** | 12× simultaneous 1080p30 decode + multimodal VLM + CNN | <20 W | runs Phi / Gemma / LLaVA-OneVision / Llama |
| **CV5 / CV7** | edge vision SoCs | low | security/automotive |

## Software stack
CVflow toolchain and the **Cooper** developer platform. Company/docs: [ambarella.com](https://www.ambarella.com/).

## Latest news (2025–2026)
- **Jan 7, 2025 (CES):** **N1-655** — on-chip decode of 12 simultaneous 1080p30 streams while running multimodal VLMs + CNNs at **<20 W** (10–100× lower power than cloud).
- **Jun 24, 2025:** Bloomberg reported Ambarella is **working with bankers to explore a potential sale**; shares jumped ~21% (market value ~$2.6B).
- **Q1 FY2026:** revenue **$85.9M (+57.6% YoY)**; edge AI ~75% of revenue.

**Caveat:** the sale exploration is reported by Bloomberg sources; no transaction is confirmed.
