# VLA Models & World Foundation Models

The silicon in [companies](../companies/README.md) is the body; these models are the brain. Two model families define the current frontier of Physical AI: **Vision-Language-Action (VLA)** models, which turn perception + instructions into robot actions, and **World Foundation Models (WFMs)**, which simulate physical reality to train and validate those policies.

## Vision-Language-Action (VLA) models
A VLA takes camera images and a natural-language instruction and outputs **robot actions** — it fuses a vision-language model's understanding with a control policy's dexterity. Conceptually: *perceive → reason → act*, often combining a VLM (semantics) with a diffusion or transformer **policy** (precise, continuous motion). A solid primer is LearnOpenCV's [Vision Language Action Models (VLA) & Policies for Robots](https://learnopencv.com/vision-language-action-models-lerobot-policy/).

### Notable VLA & policy models (verified, current)
| Model | Org / year | Params | Open? | Note |
|---|---|---|---|---|
| **RT-2** | Google DeepMind, 2023 | large | ❌ | established the VLA paradigm |
| **OpenVLA** | Stanford/collab, 2024 | 7B | ✅ | trained on 970k Open-X demos; beats RT-2-X (55B) by 16.5% with 7× fewer params (per the paper) |
| **π0 / π0.5** | Physical Intelligence, 2024–25 | — | partial | flow-based; widely cited as SOTA |
| **Octo** | open, 2024 | small | ✅ | generalist manipulation transformer |
| **Diffusion Policy** | 2023 | small | ✅ | diffusion over action sequences |
| **ACT** | 2023 | ~80M | ✅ | Action Chunking Transformer |
| **SmolVLA** | Hugging Face, 2025 | 450M | ✅ | 82–90% on LIBERO; 15–30 Hz on one RTX 4090 |
| **Isaac GR00T N1 / N1.5** | NVIDIA, 2025 | 2.2B | ✅ | humanoid foundation policy; Eagle VLM backbone |

### Single-system vs dual-system designs
- **Single model** (RT-2, OpenVLA, π0): one network maps pixels+text → actions.
- **Dual system** (Figure Helix, GR00T N1): a slow "System-2" VLM for reasoning plus a fast "System-1" diffusion transformer for high-rate control — mirroring human fast/slow cognition.

### LeRobot — the open robot-learning hub
**[LeRobot](https://github.com/huggingface/lerobot)** (Hugging Face) is the de-facto open library for robot learning, with implementations of **ACT, Diffusion Policy, VQ-BeT, π0/π0.5/π0Fast, SmolVLA, GR00T N1.5**, plus datasets and pretrained checkpoints. It is the fastest on-ramp to running a real policy.

## World Foundation Models (WFMs) — NVIDIA Cosmos
A **world model** learns the dynamics of physical reality so it can **predict** future states and **generate synthetic training data** — covering rare or dangerous situations a robot can't safely encounter for real.

**NVIDIA Cosmos** ([nvidia.com/en-us/ai/cosmos](https://www.nvidia.com/en-us/ai/cosmos/); platform paper [arXiv 2501.03575](https://arxiv.org/abs/2501.03575), Jan 7 2025) has three families:
- **Predict** — generate future world states / video from text, image, or video.
- **Transfer** — turn structured inputs (segmentation, depth) into photoreal synthetic data (Sim2Real / Real2Real).
- **Reason** — vision-language reasoning over physical scenes.

Latest: **Cosmos-Predict 2.5** ([arXiv 2511.00062](https://arxiv.org/abs/2511.00062)) unifies Text2World / Image2World / Video2World on a flow-based architecture (2B & 14B scales, trained on ~200M curated clips); **Cosmos-Transfer 2.5** is ~3.5× smaller than Transfer1 at higher fidelity. Released under the NVIDIA Open Model License ([github.com/nvidia-cosmos](https://github.com/nvidia-cosmos)).

## How it fits the three-computer workflow
WFMs power the **simulate** stage (synthetic data + validation); VLAs are the **policies** trained there and then deployed on edge silicon for the **deploy** stage. See [concepts](../concepts/README.md) and [applications](../applications/README.md).

> **Note:** the VLA field moves monthly; treat the table as a mid-2026 snapshot and verify the latest checkpoints in LeRobot before building.
