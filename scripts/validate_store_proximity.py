import pandas as pd
from pathlib import Path

input_file = Path(
    "data/processed/GeoPulse_Store_Proximity_Analysis.csv"
)

output_file = Path(
    "data/processed/GeoPulse_Proximity_Quality_Report.csv"
)

df = pd.read_csv(input_file)

checks = []

def add_check(name, passed, details):
    checks.append({
        "check_name": name,
        "status": "PASS" if passed else "FAIL",
        "details": details
    })

required_columns = [
    "store_id",
    "footfall_records",
    "unique_devices",
    "average_distance_m",
    "pings_within_500m",
    "within_500m_percentage"
]

missing = [
    col for col in required_columns
    if col not in df.columns
]

add_check(
    "Required columns",
    len(missing) == 0,
    f"Missing columns: {missing}"
)

if not missing:
    add_check(
        "Duplicate store IDs",
        not df["store_id"].duplicated().any(),
        "Each store should appear only once"
    )

    add_check(
        "Negative footfall",
        (df["footfall_records"] >= 0).all(),
        "Footfall counts must be non-negative"
    )

    add_check(
        "Unique devices within footfall",
        (df["unique_devices"] <= df["footfall_records"]).all(),
        "Unique devices cannot exceed total pings"
    )

    add_check(
        "Valid 500m counts",
        (
            (df["pings_within_500m"] >= 0) &
            (df["pings_within_500m"] <= df["footfall_records"])
        ).all(),
        "500m counts must be within total footfall"
    )

    add_check(
        "Percentage range",
        (
            (df["within_500m_percentage"] >= 0) &
            (df["within_500m_percentage"] <= 100)
        ).all(),
        "Percentage must be between 0 and 100"
    )

    expected_percentage = (
        df["pings_within_500m"] /
        df["footfall_records"].replace(0, 1) * 100
    ).round(2)

    add_check(
        "Percentage calculation",
        (
            expected_percentage ==
            df["within_500m_percentage"]
        ).all(),
        "Verify 500m percentage calculation"
    )

    add_check(
        "Non-negative distance",
        (df["average_distance_m"] >= 0).all(),
        "Average distance must not be negative"
    )

report = pd.DataFrame(checks)

output_file.parent.mkdir(parents=True, exist_ok=True)
report.to_csv(output_file, index=False)

print(report.to_string(index=False))
print(f"\nQuality report saved to: {output_file}")
print(
    "\nOverall status:",
    "PASS" if (report["status"] == "PASS").all()
    else "CHECK REQUIRED"
)