
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Read store locations
stores = pd.read_csv("data/raw/GeoPulse_Store_Locations.csv")

# Create geographic points
geometry = [
    Point(lon, lat)
    for lon, lat in zip(stores["longitude"], stores["latitude"])
]

gdf = gpd.GeoDataFrame(stores, geometry=geometry, crs="EPSG:4326")

# Project to a metre-based coordinate system
gdf = gdf.to_crs("EPSG:32643")

# Create 500-metre catchment polygons
gdf["geometry"] = gdf.geometry.buffer(gdf["catchment_radius_m"])

# Export polygons as GeoJSON
gdf = gdf.to_crs("EPSG:4326")
gdf.to_file(
    "data/processed/GeoPulse_Catchment_Polygons.geojson",
    driver="GeoJSON"
)

print("Catchment polygons created successfully!")
print(gdf[["store_id", "store_name", "catchment_radius_m"]])
