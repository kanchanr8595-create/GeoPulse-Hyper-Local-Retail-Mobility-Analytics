
import csv
from pathlib import Path
from collections import defaultdict

input_file = Path("data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv")
output_file = Path("data/processed/GeoPulse_Footfall_Analysis.csv")

with input_file.open("r", newline="", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

if not rows:
    raise ValueError("GPS dataset is empty")

required_columns = {
    "device_id",
    "daypart",
    "activity_area",
    "within_500m_of_nearest_store"
}

if not required_columns.issubset(rows[0].keys()):
    raise ValueError("Required GPS columns are missing")

def analyze(records):
    within_count = sum(
        row["within_500m_of_nearest_store"].strip().lower() == "true"
        for row in records
    )

    return {
        "record_count": len(records),
        "unique_devices": len(set(row["device_id"] for row in records)),
        "within_500m_count": within_count,
        "coverage_percentage": round(
            within_count / len(records) * 100, 2
        )
    }

results = []

for analysis_type, column in [
    ("Activity Area", "activity_area"),
    ("Daypart", "daypart")
]:
    groups = defaultdict(list)

    for row in rows:
        groups[row[column]].append(row)

    sorted_groups = sorted(
        groups.items(),
        key=lambda item: len(item[1]),
        reverse=True
    )

    for rank, (category, records) in enumerate(sorted_groups, start=1):
        metrics = analyze(records)

        results.append({
            "analysis_type": analysis_type,
            "rank": rank,
            "category": category,
            **metrics
        })

output_file.parent.mkdir(parents=True, exist_ok=True)

fieldnames = [
    "analysis_type",
    "rank",
    "category",
    "record_count",
    "unique_devices",
    "within_500m_count",
    "coverage_percentage"
]

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("GEOPULSE FOOTFALL ANALYSIS")
print("--------------------------")
print(f"Total GPS records: {len(rows)}")
print(f"Activity areas analyzed: {sum(r['analysis_type'] == 'Activity Area' for r in results)}")
print(f"Dayparts analyzed: {sum(r['analysis_type'] == 'Daypart' for r in results)}")
print(f"Highest footfall area: {results[0]['category']}")
print(f"Report saved: {output_file}")
