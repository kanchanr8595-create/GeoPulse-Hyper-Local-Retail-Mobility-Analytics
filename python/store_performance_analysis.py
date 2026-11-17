
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = ROOT / "data/processed/store_proximity_analysis.csv"
OUTPUT_FILE = ROOT / "data/processed/store_performance_analysis.csv"


def analyze_store_performance():
    data = pd.read_csv(INPUT_FILE)

    data["within_catchment"] = (
        data["within_catchment"]
        .astype(str).str.lower().map({"true": True, "false": False})
    )

    summary = (
        data.dropna(subset=["nearest_store_id"])
        .groupby(
            ["nearest_store_id", "nearest_store_name"]
        )
        .agg(
            total_pings=("ping_id", "count"),
            catchment_pings=("within_catchment", "sum"),
            average_distance_m=("distance_m", "mean")
        )
        .reset_index()
    )

    summary["outside_catchment"] = (
        summary["total_pings"] - summary["catchment_pings"]
    )

    summary["catchment_percentage"] = (
        summary["catchment_pings"]
        / summary["total_pings"] * 100
    ).round(2)

    summary["average_distance_m"] = (
        summary["average_distance_m"].round(2)
    )

    summary = summary.sort_values(
        "total_pings", ascending=False
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT_FILE, index=False)

    print("STORE PERFORMANCE ANALYSIS")
    print(summary.to_string(index=False))
    print("Output saved:", OUTPUT_FILE)


if __name__ == "__main__":
    analyze_store_performance()
