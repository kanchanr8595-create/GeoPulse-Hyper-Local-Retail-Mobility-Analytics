
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

GPS_FILE = ROOT / "data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv"
STORE_FILE = ROOT / "data/raw/GeoPulse_Store_Locations.csv"


def validate_gps_data():
    gps = pd.read_csv(GPS_FILE)
    stores = pd.read_csv(STORE_FILE)

    print("\n=== GEOPULSE FINAL DATA VALIDATION ===")

    print("\nGPS DATASET")
    print("Total rows:", len(gps))
    print("Total columns:", len(gps.columns))
    print("Duplicate rows:", gps.duplicated().sum())
    print("Duplicate ping IDs:", gps["ping_id"].duplicated().sum())

    print("\nMissing values:")
    print(gps.isnull().sum())

    print("\nCoordinate validation:")
    invalid_lat = ~gps["latitude"].between(-90, 90)
    invalid_lon = ~gps["longitude"].between(-180, 180)

    print("Invalid latitude:", invalid_lat.sum())
    print("Invalid longitude:", invalid_lon.sum())

    print("\nSTORE DATASET")
    print("Total stores:", len(stores))
    print("Duplicate store IDs:", stores["store_id"].duplicated().sum())
    print("Missing values:")
    print(stores.isnull().sum())

    print("\nStore coordinate validation:")
    print("Invalid store latitude:",
          (~stores["latitude"].between(-90, 90)).sum())
    print("Invalid store longitude:",
          (~stores["longitude"].between(-180, 180)).sum())


if __name__ == "__main__":
    validate_gps_data()
