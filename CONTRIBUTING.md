# Contributing to awesome-physical-ai

Thanks for helping maintain an accurate, vendor-neutral map of the Physical-AI landscape. This guide explains **what we accept** and **the quality bar**.

## What this repo is
A curated reference: **company/product profiles**, **architecture explainers**, **comparison tables**, **VLA/world-model coverage**, **applications**, and a **curated awesome list**. It is opinionated, current, and honest about what is verified versus vendor-claimed.

## Great contributions
- 🆕 **Add or correct a company/product spec** (with an official source and date).
- 📊 **Improve a comparison table** (alignment, a missing part, a corrected number).
- 📰 **Add verified 2025–2026 news** (funding, launches, acquisitions) — primary source + date required.
- 🔁 **Flag a rename/deprecation/status change.**
- 📚 **Add a high-signal resource** to the awesome list.

## Quality bar (non-negotiable)
1. **Cite a primary source with a date.** Vendor newsroom, official docs, SEC/press, or a named reputable outlet. No unsourced specs.
2. **Label vendor claims.** Any TOPS/efficiency figure from a vendor is marked vendor-claimed; only flag a number as independent if a named third party measured it.
3. **State precision for TOPS** (INT4/INT8/FP4) — they are not comparable.
4. **Be vendor-neutral.** Note trade-offs, not just strengths.
5. **Specific links, no trailing slash**; awesome-list items use `- [Name](url) - Capitalized description.`

## Submit
1. Fork, branch (`add/<short-name>`), keep the PR focused.
2. Run checks locally if you can:
   ```bash
   npx awesome-lint awesome-resources/README.md
   lychee --offline . || lychee .
   ```
3. Use a [Conventional Commits](https://www.conventionalcommits.org/) message, e.g. `docs: update Hailo-10H pricing`.
4. Open a PR; CI runs `awesome-lint` and a link checker.

## License of contributions
Prose/tables: **CC BY 4.0**; any code: **MIT**. By contributing you agree to these terms. See [LICENSE](LICENSE) and the [Code of Conduct](CODE_OF_CONDUCT.md).
