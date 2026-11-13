
import pandas as pd

def load_gps_data(file_path):
    return pd.read_csv(file_path)

def load_store_data(file_path):
    return pd.read_csv(file_path)

def inspect_data(gps, stores):
    print("GPS DATASET")
    print("Total GPS Records:", len(gps))
    print("GPS Columns:", list(gps.columns))
    print("\nSTORE DATASET")
    print("Total Stores:", len(stores))
    print("Store Columns:", list(stores.columns))

if __name__ == "__main__":
    gps = load_gps_data(
        "../data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv"
    )

    stores = load_store_data(
        "../data/raw/GeoPulse_Store_Locations.csv"
    )

    inspect_data(gps, stores)
