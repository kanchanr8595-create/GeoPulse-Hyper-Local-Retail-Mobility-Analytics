import geopandas as gpd

file_path = "data/processed/GeoPulse_Catchment_Polygons.geojson"

gdf = gpd.read_file(file_path)

expected_stores = {"STORE_A", "STORE_C", "CANDIDATE_B"}

projected = gdf.to_crs("EPSG:32643")
projected["area_sq_m"] = projected.geometry.area
projected["radius_m"] = (projected["area_sq_m"] / 3.141592653589793) ** 0.5

print("GEOPULSE CATCHMENT VALIDATION")
print("--------------------------------")
print("Total features:", len(gdf))
print("CRS:", gdf.crs)
print(projected[["store_id", "radius_m"]].round(2).to_string(index=False))

valid = (
    len(gdf) == 3
    and set(gdf["store_id"]) == expected_stores
    and gdf.geometry.notna().all()
    and gdf.geometry.is_valid.all()
    and (projected["radius_m"].sub(500).abs() <= 2).all()
)

if valid:
    print("\nRESULT: PASS")
else:
    print("\nRESULT: FAIL")
    raise SystemExit(1)
