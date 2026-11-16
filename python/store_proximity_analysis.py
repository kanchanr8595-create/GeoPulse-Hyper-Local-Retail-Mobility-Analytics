
import pandas as pd
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

GPS_FILE = ROOT / "data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv"
STORE_FILE = ROOT / "data/raw/GeoPulse_Store_Locations.csv"
OUTPUT_FILE = ROOT / "data/processed/store_proximity_analysis.csv"


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two coordinates in metres."""
    earth_radius = 6371000

    lat1, lon1, lat2, lon2 = map(
        math.radians, [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    return 2 * earth_radius * math.asin(math.sqrt(a))


def analyze_store_proximity():
    gps = pd.read_csv(GPS_FILE)
    stores = pd.read_csv(STORE_FILE)

    required_gps = ["ping_id", "latitude", "longitude"]
    required_stores = [
        "store_id", "store_name", "latitude",
        "longitude", "catchment_radius_m"
    ]

    for col in required_gps:
        if col not in gps.columns:
            raise ValueError(f"Missing GPS column: {col}")

    for col in required_stores:
        if col not in stores.columns:
            raise ValueError(f"Missing store column: {col}")

    results = []

    for _, ping in gps.iterrows():
        if pd.isna(ping["latitude"]) or pd.isna(ping["longitude"]):
            results.append({
                "ping_id": ping["ping_id"],
                "nearest_store_id": None,
                "nearest_store_name": None,
                "distance_m": None,
                "catchment_radius_m": None,
                "within_catchment": False
            })
            continue

        distances = []

        for _, store in stores.iterrows():
            distance = calculate_distance(
                ping["latitude"],
                ping["longitude"],
                store["latitude"],
                store["longitude"]
            )

            distances.append((distance, store))

        distance, nearest_store = min(
            distances, key=lambda item: item[0]
        )

        radius = nearest_store["catchment_radius_m"]

        results.append({
            "ping_id": ping["ping_id"],
            "nearest_store_id": nearest_store["store_id"],
            "nearest_store_name": nearest_store["store_name"],
            "distance_m": round(distance, 2),
            "catchment_radius_m": radius,
            "within_catchment": distance <= radius
        })

    output = pd.DataFrame(results)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(OUTPUT_FILE, index=False)

    print("STORE PROXIMITY ANALYSIS COMPLETED")
    print("Total GPS pings:", len(output))
    print("Pings within catchment:", output["within_catchment"].sum())
    print("Output saved:", OUTPUT_FILE)


if __name__ == "__main__":
    analyze_store_proximity()
