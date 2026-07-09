# Interactive Hardware &amp; Runtime Picker

A zero-backend, single-page decision tool. Answer four questions (budget, use case,
power envelope, ecosystem) and get a ranked top-3 of edge-AI accelerators, with
caveats (EOL, not-shipping, vendor-claim-only). A second tab maps a target platform
to the runtime you should reach for.

## How it works

- [`index.html`](index.html) is self-contained vanilla JS/CSS — no build step, no dependencies.
- It `fetch()`es [`hardware.json`](hardware.json), which is **generated** from
  [`../../data/hardware.yaml`](../../data/hardware.yaml) by
  [`../../scripts/generate_tables.py`](../../scripts/generate_tables.py).
- Because the picker and the [comparison tables](../../hardware-comparison/README.md) share one
  source of truth, they can never drift apart.

## Run it locally

`fetch()` needs HTTP (opening the file directly is blocked by the browser), so serve the folder:

```bash
# from the repo root
python scripts/generate_tables.py     # (re)build hardware.json
cd docs/picker
python -m http.server 8000            # then open http://localhost:8000
```

## Publish with GitHub Pages

Settings → Pages → Source: **Deploy from a branch** → branch `main`, folder `/docs`.
The picker is then served at `https://<user>.github.io/awesome-physical-ai/picker/`.
