import csv
from pathlib import Path
from collections import defaultdict

input_file = Path("data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv")
output_file = Path("data/processed/GeoPulse_GPS_Summary_Report.csv")

with input_file.open("r", newline="", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

if not rows:
    raise ValueError("GPS dataset is empty")

summary = []

def add_summary(summary_type, category, records):
    summary.append({
        "summary_type": summary_type,
        "category": category,
        "record_count": len(records),
        "unique_devices": len(set(r["device_id"] for r in records)),
        "within_500m_count": sum(
            r["within_500m_of_nearest_store"].strip().lower() == "true"
            for r in records
        )
    })

add_summary("Overall", "All GPS Records", rows)

for column in ["daypart", "activity_area"]:
    groups = defaultdict(list)
    for row in rows:
        groups[row[column]].append(row)

    for category, records in sorted(groups.items()):
        add_summary(column, category, records)

output_file.parent.mkdir(parents=True, exist_ok=True)

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "summary_type", "category", "record_count",
            "unique_devices", "within_500m_count"
        ]
    )
    writer.writeheader()
    writer.writerows(summary)

print("GEOPULSE GPS SUMMARY REPORT")
print("---------------------------")
print(f"Total records: {len(rows)}")
print(f"Unique devices: {len(set(r['device_id'] for r in rows))}")
print(f"Summary rows generated: {len(summary)}")
print(f"Report saved: {output_file}")
