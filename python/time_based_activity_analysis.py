
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = ROOT / "data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv"
OUTPUT_FILE = ROOT / "data/processed/time_based_activity_summary.csv"


def analyze_time_activity():
    data = pd.read_csv(INPUT_FILE)

    if "daypart" not in data.columns:
        raise ValueError("daypart column not found")

    if "hour" not in data.columns:
        raise ValueError("hour column not found")

    data["hour"] = pd.to_numeric(
        data["hour"], errors="coerce"
    )

    daypart_summary = (
        data.groupby("daypart", dropna=False)
        .agg(total_pings=("ping_id", "count"))
        .reset_index()
    )

    hourly_summary = (
        data.groupby("hour", dropna=False)
        .agg(total_pings=("ping_id", "count"))
        .reset_index()
        .sort_values("hour")
    )

    daypart_summary["analysis_type"] = "Daypart"
    hourly_summary["analysis_type"] = "Hour"

    daypart_summary = daypart_summary.rename(
        columns={"daypart": "time_period"}
    )

    hourly_summary = hourly_summary.rename(
        columns={"hour": "time_period"}
    )

    result = pd.concat(
        [daypart_summary, hourly_summary],
        ignore_index=True
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT_FILE, index=False)

    print("TIME-BASED ACTIVITY ANALYSIS")
    print(result.to_string(index=False))
    print("Output saved:", OUTPUT_FILE)


if __name__ == "__main__":
    analyze_time_activity()
