#!/usr/bin/env python3
"""Regenerate figures from figures_data CSV files."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
FIGDATA = ROOT / "figures_data"
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

def save_fig8():
    df = pd.read_csv(FIGDATA / "fig8_dynamic_trajectories.csv")
    for metric, ylabel, name in [
        ("critical_load_served_percent", "Critical load served (%)", "fig8a_critical_load.png"),
        ("aggregate_bess_soc_percent", "Aggregate BESS SoC (%)", "fig8b_bess_soc.png"),
        ("cumulative_ens_kwh", "Cumulative ENS (kWh)", "fig8c_cumulative_ens.png"),
    ]:
        plt.figure(figsize=(6,4))
        for cfg, g in df.groupby("configuration"):
            plt.plot(g["time"], g[metric], marker="o", label=cfg)
        for x, label in [(0,"F1"),(2,"D1"),(3,"R1"),(4,"F2"),(6,"D2")]:
            plt.axvline(x, linestyle="--", linewidth=0.8)
            plt.text(x, plt.ylim()[1], label, ha="center", va="top")
        plt.xlabel("Time step")
        plt.ylabel(ylabel)
        plt.legend()
        plt.tight_layout()
        plt.savefig(OUT / name, dpi=300)
        plt.close()

def save_fig9():
    df = pd.read_csv(FIGDATA / "fig9_convergence.csv")
    plt.figure(figsize=(6,4))
    for method, g in df.groupby("method"):
        plt.plot(g["iteration"], g["normalized_best_objective"], label=method)
    plt.xlabel("Iteration")
    plt.ylabel("Normalized best objective")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "fig9_convergence.png", dpi=300)
    plt.close()

def save_fig10():
    df = pd.read_csv(FIGDATA / "fig10_forecast_noise.csv")
    for metric, ylabel, name in [
        ("cumulative_ens_kwh", "Cumulative ENS (kWh)", "fig10a_forecast_noise_ens.png"),
        ("switching_reversals", "Switching reversals", "fig10b_forecast_noise_switching.png"),
    ]:
        plt.figure(figsize=(6,4))
        for beta, g in df.groupby("beta"):
            g = g.sort_values("forecast_error_percent")
            plt.plot(g["forecast_error_percent"], g[metric], marker="o", label=f"beta={beta}")
        plt.xlabel("Forecast error (%)")
        plt.ylabel(ylabel)
        plt.legend()
        plt.tight_layout()
        plt.savefig(OUT / name, dpi=300)
        plt.close()

def save_figE1():
    df = pd.read_csv(FIGDATA / "figE1_closed_loop_response.csv")
    for metric, ylabel, name in [
        ("filtered_osi", "Filtered OSI", "figE1_filtered_osi.png"),
        ("restored_total_load_percent", "Restored total load (%)", "figE1_total_load.png"),
        ("restored_critical_load_percent", "Restored critical load (%)", "figE1_critical_load.png"),
        ("aggregate_bess_soc_percent", "Aggregate BESS SoC (%)", "figE1_bess_soc.png"),
    ]:
        plt.figure(figsize=(6,4))
        plt.plot(df["time"], df[metric], marker="o")
        plt.xlabel("Time step")
        plt.ylabel(ylabel)
        plt.tight_layout()
        plt.savefig(OUT / name, dpi=300)
        plt.close()

def main():
    save_fig8()
    save_fig9()
    save_fig10()
    save_figE1()
    print(f"Wrote figures to {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
