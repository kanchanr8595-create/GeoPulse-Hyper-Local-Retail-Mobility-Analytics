
import geopandas as gpd
import pandas as pd
from pathlib import Path

file_path = "data/processed/GeoPulse_Catchment_Polygons.geojson"
output_path = "data/processed/GeoPulse_Catchment_Quality_Report.csv"

gdf = gpd.read_file(file_path)

expected_stores = {"STORE_A", "STORE_C", "CANDIDATE_B"}

# Convert geometry to metres for accurate area calculation
projected = gdf.to_crs("EPSG:32643")

projected["area_sq_m"] = projected.geometry.area
projected["radius_m"] = (
    projected["area_sq_m"] / 3.141592653589793
) ** 0.5

projected["geometry_valid"] = projected.geometry.is_valid
projected["radius_valid"] = (
    projected["radius_m"].sub(500).abs() <= 2
)

report = projected[
    ["store_id", "area_sq_m", "radius_m",
     "geometry_valid", "radius_valid"]
].copy()

report["area_sq_km"] = report["area_sq_m"] / 1_000_000

Path("data/processed").mkdir(parents=True, exist_ok=True)
report.to_csv(output_path, index=False)

print("GEOPULSE CATCHMENT QUALITY ANALYSIS")
print("------------------------------------")
print("Total stores:", len(report))
print(report.round(2).to_string(index=False))

valid = (
    len(gdf) == 3
    and set(gdf["store_id"]) == expected_stores
    and gdf.geometry.notna().all()
    and gdf.geometry.is_valid.all()
    and report["radius_valid"].all()
)

if valid:
    print("\nRESULT: PASS")
    print("Quality report saved:", output_path)
else:
    print("\nRESULT: FAIL")
    raise SystemExit(1)
