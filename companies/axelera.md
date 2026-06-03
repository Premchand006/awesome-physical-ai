# Axelera AI — Voyager SDK (Digital In-Memory Computing)

> The cost-to-performance challenger for multi-stream vision. Axelera computes matrix math **inside the memory array** (digital in-memory computing), sidestepping the "memory wall" to deliver high throughput per dollar on dense camera workloads.

| | |
|---|---|
| **Founded / HQ** | 2021 · Eindhoven, NL (imec spin-off; Fabrizio Del Maffeo) |
| **Architecture** | **Digital In-Memory Computing (D-IMC)** |
| **Edge flagship** | Metis AIPU (M.2 / PCIe); Europa AIPU (2026) |
| **Software stack** | **Voyager SDK** (Apache TVM + GStreamer, YAML pipelines) |
| **Primary market** | Multi-stream vision, heavy enterprise edge |
| **Strategic edge** | Industry-leading cost-to-performance for many concurrent video streams |

## History
Spun out of imec in 2021, Axelera raised **>$200M** (investors include Samsung) and won a **€61.6M EuroHPC "DARE" grant** for its Titania datacenter chiplet. It is one of Europe's most prominent AI-silicon startups.

## Architecture
**Digital In-Memory Computing** performs multiply-accumulate operations within SRAM cells, drastically cutting the data movement that dominates GPU energy use. Unlike analog IMC (EnCharge, Mythic), Axelera's approach is fully *digital*, avoiding analog noise while still beating the memory wall.

## Flagship products (verified)
| Product | AI perf | Precision | On-chip mem | Notes |
|---|---|---|---|---|
| **Metis AIPU** | up to 214 TOPS (1-chip) / 856 TOPS (4-chip) | INT8 (~15 TOPS/W) | — | M.2 / PCIe |
| **Europa AIPU** | 629 TOPS | INT8 | 128 MB L2 SRAM | 8 cores + 16 RISC-V vector cores; ships H1 2026 |

## Software stack
**Voyager SDK** — declarative **YAML** pipelines built on **Apache TVM** (compiler) and **GStreamer** (media), with a 50+ model Model Zoo. Repo: [github.com/axelera-ai-hub/voyager-sdk](https://github.com/axelera-ai-hub/voyager-sdk) · software: [axelera.ai/ai-software](https://axelera.ai/ai-software).

## Latest news (2025–2026)
- **Oct 21, 2025:** announced the **Europa AIPU** (629 TOPS, 128 MB SRAM, ships H1 2026). *(Business Wire.)*
- 2025: **€61.6M EuroHPC DARE** grant for the Titania datacenter chiplet.

> **Benchmark/claim audit:** Axelera's "industry-leading multi-stream vision" rests on vendor demos (e.g., 24 concurrent YOLOv5 streams on one Metis PCIe card; "16.4 fps/$" on ResNet-50). **HotTech** rankings are vendor-promoted, and **Astute Group** is Axelera's distributor — neither is a neutral benchmark. Treat the cost-to-performance claim as plausible but vendor-sourced.
