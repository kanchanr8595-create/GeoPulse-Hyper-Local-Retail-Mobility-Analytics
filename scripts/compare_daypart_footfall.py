
import pandas as pd
from pathlib import Path

input_file = Path("data/processed/GeoPulse_Footfall_Analysis.csv")
output_file = Path("data/processed/GeoPulse_Daypart_Comparison.csv")

df = pd.read_csv(input_file)

daypart_data = df[df["analysis_type"] == "Daypart"].copy()

comparison = daypart_data[
    daypart_data["category"].isin(["Morning Rush", "Evening Rush"])
].copy()

comparison = comparison[
    ["category", "record_count", "unique_devices", "coverage_percentage"]
]

comparison = comparison.rename(columns={
    "category": "daypart",
    "record_count": "footfall_records"
})

comparison.to_csv(output_file, index=False)

print("Morning vs Evening comparison completed.")
print(comparison)
print(f"Output saved to: {output_file}")
