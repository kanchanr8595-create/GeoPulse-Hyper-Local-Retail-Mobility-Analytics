import pandas as pd
from pathlib import Path

input_file = Path("data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv")
store_file = Path("data/raw/GeoPulse_Store_Locations.csv")
output_file = Path("data/processed/GeoPulse_Store_Proximity_Analysis.csv")

# Load GPS and store datasets
gps = pd.read_csv(input_file)
stores = pd.read_csv(store_file)

# Group GPS records by nearest store
analysis = gps.groupby("nearest_store_id").agg(
    footfall_records=("ping_id", "count"),
    unique_devices=("device_id", "nunique"),
    average_distance_m=("nearest_store_distance_m", "mean"),
    pings_within_500m=("within_500m_of_nearest_store", "sum")
).reset_index()

# Calculate percentage of pings within 500 metres
analysis["within_500m_percentage"] = (
    analysis["pings_within_500m"] /
    analysis["footfall_records"] * 100
).round(2)

analysis["average_distance_m"] = analysis["average_distance_m"].round(2)

# Add store details
analysis = analysis.merge(
    stores,
    left_on="nearest_store_id",
    right_on="store_id",
    how="right"
)

# Select final report columns
analysis = analysis[
    [
        "store_id",
        "store_name",
        "store_status",
        "footfall_records",
        "unique_devices",
        "average_distance_m",
        "pings_within_500m",
        "within_500m_percentage"
    ]
]

# Replace missing counts with zero
count_columns = [
    "footfall_records",
    "unique_devices",
    "pings_within_500m"
]
analysis[count_columns] = analysis[count_columns].fillna(0).astype(int)

# Save output
output_file.parent.mkdir(parents=True, exist_ok=True)
analysis.to_csv(output_file, index=False)

print("Store proximity analysis completed successfully.")
print(analysis.to_string(index=False))
print(f"\nOutput saved to: {output_file}")
