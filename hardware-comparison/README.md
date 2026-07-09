# Hardware Comparison

Side-by-side flagship specs across the landscape. **Read this with the caveats up front:** every TOPS number is a **peak vendor figure at the stated precision**, and INT4/INT8/FP4 are not directly comparable. Independent third-party benchmarks are rare in this space and are flagged explicitly.

## Edge accelerators — flagship parts
| Company | Flagship | AI perf (vendor) | Precision | On-chip / module memory | Power | Form factor |
|---|---|---|---|---|---|---|
| [Hailo](../companies/hailo.md) | Hailo-10H | 40 / 20 TOPS | INT4 / INT8 | 4–8 GB on-module | ~2.5 W | M.2 |
| [Hailo](../companies/hailo.md) | Hailo-8 | 26 TOPS | INT8 | on-chip (no DRAM) | ~2.5 W | M.2 / module |
| [SiMa.ai](../companies/sima-ai.md) | Modalix M-series | 50 TOPS | BF16 + INT8/16 | on-chip | <10 W | SoM / SoC |
| [Axelera](../companies/axelera.md) | Metis | up to 214 / 856 TOPS | INT8 | — | card-level | M.2 / PCIe |
| [Axelera](../companies/axelera.md) | Europa — samples H1 2026, *not shipping* | 629 TOPS (vendor claim) | INT8 | 128 MB L2 SRAM | card | PCIe |
| [Blaize](../companies/blaize.md) | GSP El Cano | 16 TOPS | INT8 | — | 7 W | module |
| [DeepX](../companies/deepx.md) | DX-M1 | 25 TOPS | INT8 | — | 3–5 W | M.2 2280 |
| [MemryX](../companies/memryx.md) | MX3 (4-chip M.2) | 24 TOPS | 4/8/16-bit + BF16 | on-chip (~42M params) | 6–8 W | M.2 |
| [Mythic](../companies/mythic.md) | M1076 AMP | 25 TOPS | analog | up to 80M weights on-chip | 3 W | M.2 / PCIe |
| [EnCharge](../companies/encharge.md) | EN100 (M.2) | 200+ TOPS | analog (charge) | 32 GB LPDDR | 8.25 W | M.2 |
| [EnCharge](../companies/encharge.md) | EN100 (PCIe) | ~1 PetaOPS | analog (charge) | 128 GB LPDDR | ~40 W | PCIe (4 NPUs) |
| [Ambarella](../companies/ambarella.md) | N1-655 | 12× 1080p30 + VLM | mixed | — | <20 W | SoC |
| [Qualcomm](../companies/qualcomm.md) | Snapdragon (Hexagon) | varies | INT2–16, FP8/16 | system | mobile | SoC |

## Edge platforms (host + accelerator)
| Platform | AI perf (vendor) | Precision | Memory | Power | Price |
|---|---|---|---|---|---|
| [NVIDIA](../companies/nvidia.md) Jetson AGX Thor | up to 2,070 TFLOPS | FP4 | 128 GB | 40–130 W | $3,499 dev kit |
| [NVIDIA](../companies/nvidia.md) Jetson Orin Nano Super | 67 TOPS | INT8 | 8 GB | 7–25 W | $249 |
| Raspberry Pi 5 + AI HAT+ 2 (Hailo-10H) | 40 TOPS | INT4 | 8 GB on HAT | ~2.5 W (NPU) | ~$130 + Pi |

## Datacenter context
| Company | Part | Notes |
|---|---|---|
| [Groq](../companies/datacenter-context.md) | LPU | ~230 MB SRAM/chip, no HBM; >1,600 tok/s vendor / ~241 tok/s independent (Llama-2-70B) |
| [Tenstorrent](../companies/datacenter-context.md) | Tensix grid | open-source bare-metal kernels |
| [Qualcomm](../companies/qualcomm.md) | AI200 (2026) / AI250 (2027) | 768 GB LPDDR/card; 160 kW racks |

## All tracked parts (auto-generated)

The curated tables above are the human-readable view. The table below is generated from
[`data/hardware.yaml`](../data/hardware.yaml) by [`scripts/generate_tables.py`](../scripts/generate_tables.py)
— the single machine-readable source of truth that also feeds the [interactive picker](../docs/picker/).
Edit the YAML, not this block.

<!-- HW-TABLE:START -->
<!-- AUTO-GENERATED from data/hardware.yaml by scripts/generate_tables.py — do not edit by hand -->

| Part | Vendor | AI perf (peak) | Power | Memory | GenAI | Price | Status | Src |
|---|---|---|---|---|---|---|---|---|
| NVIDIA Jetson AGX Thor (Dev Kit) | NVIDIA | 2070 TFLOPS (FP4) | 40–130 W | 128 GB LPDDR5X | ✅ | $3499 | available | © |
| NVIDIA Jetson Orin Nano Super (Dev Kit) | NVIDIA | 67 TOPS (INT8-sparse) | 7–25 W | 8 GB LPDDR5, 102 GB/s | ✅ | $249 | available | © |
| Raspberry Pi 5 + AI HAT+ 2 (Hailo-10H) | Raspberry Pi | 40 TOPS (INT4) | 2–3 W | 8 GB LPDDR4X on HAT + Pi RAM | ✅ | $130 | available | 🔬 |
| Hailo-10H (discrete M.2) | Hailo | 40 TOPS (INT4) | 2–3 W | 4-8 GB on-module LPDDR4X | ✅ | — | available | 🔬 |
| Hailo-8 (discrete M.2) | Hailo | 26 TOPS (INT8) | 2–3 W | on-chip (no external DRAM) | ❌ | $110 | available | 🔬 |
| SiMa.ai Modalix (MLSoC) | SiMa.ai | 50 TOPS (BF16+INT8/16) | 5–10 W | 8-32 GB LPDDR5 on module | ✅ | $349 | available | © |
| Axelera Metis (M.2 / PCIe) | Axelera | 214 TOPS (INT8) | 8–40 W | on-card | ❌ | — | available | 🔬 |
| Axelera Europa (PCIe) | Axelera | 629 TOPS (INT8) | 45 W | 128 MB on-chip L2 SRAM | ✅ | — | samples | © |
| Blaize GSP (El Cano) | Blaize | 16 TOPS (INT8) | 7 W | on-module | ❌ | — | available | © |
| DeepX DX-M1 | DeepX | 25 TOPS (INT8) | 3–5 W | 4 GB LPDDR5 | ❌ | — | available | 🔬 |
| MemryX MX3 (4-chip M.2) | MemryX | 24 TOPS (4/8/16-bit+BF16) | 6–8 W | on-chip (~42M params, no external DRAM) | ❌ | $149 | available | 🔬 |
| Mythic M1076 AMP (analog) | Mythic | 25 TOPS (analog) | 3 W | up to 80M weights on-chip | ❌ | — | available | © |
| EnCharge EN100 (M.2) | EnCharge | 200 TOPS (analog-charge) | 8–9 W | 32 GB LPDDR (272 GB/s) | ✅ | — | samples | © |
| EnCharge EN100 (PCIe, 4 NPUs) | EnCharge | 1 PetaOPS (analog-charge) | 40 W | 128 GB LPDDR | ✅ | — | samples | © |
| Ambarella N1-655 (CVflow SoC) | Ambarella | 12 streams (VLM-mixed) | 15–20 W | system | ✅ | — | available | © |

> **Src:** 🔬 = independent third-party benchmark · © = vendor claim. **AI perf** is a peak figure at the stated precision; INT4/INT8/FP4 are not comparable. `status: samples` = announced/sampling, not generally shipping.
<!-- HW-TABLE:END -->

## How to read efficiency claims
- **TOPS/W** is the honest comparator for edge parts, but it's still a peak figure. Hailo-10H ≈ 16 TOPS/W; Blaize ≈ >10 TOPS/W; Axelera Metis ≈ 15 TOPS/W; Mythic claims 120 TOPS/W (next-gen, unverified).
- **Independent datapoints today:** MemryX (Phoronix / Anton Maltsev hands-on), Hailo-10H (CNX Software), Groq (~241 tok/s Llama-2-70B). Everything else is vendor-sourced.
- **Memory caps model size.** Parts with no external DRAM (Hailo-8, MemryX, Mythic) are superb for CV but limited for large LLMs; parts with on-module LPDDR (Hailo-10H, EnCharge, Jetson) can host generative models.

➡️ Full per-company detail: [companies](../companies/README.md). The models these run: [vla-and-world-models](../vla-and-world-models/README.md).
