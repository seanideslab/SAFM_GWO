#!/usr/bin/env python3
"""Regenerate summary tables from result CSV files."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
TABLES = ROOT / "tables"
TABLES.mkdir(exist_ok=True)

def summarize_30runs(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "configuration" not in df.columns or "run_id" not in df.columns:
        return df
    numeric = [
        c for c in df.columns
        if c not in {"run_id", "seed", "configuration"}
        and pd.api.types.is_numeric_dtype(df[c])
    ]
    rows = []
    for cfg, group in df.groupby("configuration"):
        row = {"configuration": cfg}
        for col in numeric:
            row[f"{col}_mean"] = group[col].mean()
            row[f"{col}_std"] = group[col].std(ddof=1)
        rows.append(row)
    return pd.DataFrame(rows)

def main():
    for csv_path in sorted(RESULTS.glob("*.csv")):
        out = TABLES / csv_path.name.replace(".csv", "_summary.csv")
        summary = summarize_30runs(csv_path)
        summary.to_csv(out, index=False)
        print(f"Wrote {out.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
