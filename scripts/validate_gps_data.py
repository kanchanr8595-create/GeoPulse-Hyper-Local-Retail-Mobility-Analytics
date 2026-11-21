import csv
from pathlib import Path

input_file = Path("data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv")

with input_file.open("r", newline="", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

required_columns = [
    "ping_id", "device_id", "latitude", "longitude",
    "timestamp", "gps_accuracy_m", "is_anonymized",
    "nearest_store_distance_m"
]

if not rows:
    raise ValueError("GPS dataset is empty")

missing_columns = [col for col in required_columns if col not in rows[0]]
if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

checks = {
    "Total GPS records": len(rows),
    "Duplicate ping IDs": len(rows) - len(set(r["ping_id"] for r in rows)),
    "Missing required values": sum(
        1 for row in rows for col in required_columns
        if not row.get(col, "").strip()
    ),
    "Invalid coordinates": sum(
        1 for r in rows
        if not (-90 <= float(r["latitude"]) <= 90)
        or not (-180 <= float(r["longitude"]) <= 180)
    ),
    "Invalid GPS accuracy": sum(
        1 for r in rows if float(r["gps_accuracy_m"]) < 0
    ),
    "Non-anonymized records": sum(
        1 for r in rows if r["is_anonymized"].strip().lower() != "true"
    ),
    "Negative store distances": sum(
        1 for r in rows if float(r["nearest_store_distance_m"]) < 0
    )
}

print("\nGEOPULSE GPS DATA QUALITY REPORT")
print("--------------------------------")
for name, value in checks.items():
    print(f"{name}: {value}")

print("\nRESULT: CHECK COMPLETE")
