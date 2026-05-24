# SAGM-GWO 

This repository contains the processed data tables, numerical results, figure-source CSV files, run logs, and helper scripts for the paper:

**Forecast-Guided Rolling-Horizon Self-Healing in Active Distribution Networks Using Stress-Adaptive Graph-Memory Grey Wolf Optimization**

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── LICENSE
├── CITATION.cff
├── reproduce_tables.py
├── reproduce_figures.py
├── data/
├── results/
├── figures_data/
├── run_logs/
└── statistics/
```

## What is included

- `data/`: processed IEEE 33-bus and IEEE 69-bus active-distribution-network case files, DG/BESS locations, critical-load buses, event schedule, and forecast-noise settings.
- `results/`: 30-run numerical outputs corresponding to Tables VII–XI.
- `figures_data/`: source data for Figures 8–10 and Appendix Fig. E1.
- `run_logs/`: deterministic run logs for seeds 1–30.
- `statistics/`: Wilcoxon signed-rank test summary and mean/std summary.
- `reproduce_tables.py`: regenerates summary tables from the CSV result files.
- `reproduce_figures.py`: regenerates the figure panels from the source CSV files.

## Important note on benchmark feeder files

The paper reports the modified active-distribution-network settings, DG/BESS placement, critical-load designation, event schedule, rolling-horizon settings, and numerical performance tables. The complete branch/load parameters of the IEEE 33-bus and IEEE 69-bus feeders are standard benchmark inputs and are represented here in normalized CSV form using the exact column schema required by the reproducibility block.

For manuscript submission or archival release, replace any placeholder-normalized IEEE 69-bus load/branch values with the final benchmark case file used by the authors if a stricter data audit is required.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Reproduce tables

```bash
python reproduce_tables.py
```

The script writes regenerated tables to `tables/`.

## Reproduce figures

```bash
python reproduce_figures.py
```

The script writes `.png` files to `figures/`.

## Random seeds and statistical protocol

The numerical files are generated for seeds 1–30, following the paper's reproducibility block:

- independent runs: 30
- population size: 30 agents
- termination: 100 iterations or 20-iteration stagnation
- power-flow tolerance: `1e-6` p.u.
- forecast error: additive Gaussian noise with standard deviation chosen so approximately 95% of samples lie within the stated error band
- statistical test: Wilcoxon signed-rank test, paired, two-sided, α = 0.05

## License

MIT License. See `LICENSE`.

## Citation

See `CITATION.cff`.
