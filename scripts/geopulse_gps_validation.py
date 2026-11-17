"""
GeoPulse – Mock GPS Data Preparation and Validation
Keep both original CSV files in the same folder as this script.
Run: python geopulse_gps_validation.py
"""
import pandas as pd

GPS_FILE = "GeoPulse_500_Synthetic_GPS_Pings.csv"
STORE_FILE = "GeoPulse_Store_Locations.csv"

# Load datasets
df = pd.read_csv(GPS_FILE)
store_df = pd.read_csv(STORE_FILE)

# Inspect GPS dataset
print("\n--- GPS FIRST 5 ROWS ---")
print(df.head())
print("\n--- GPS DATASET INFO ---")
df.info()

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# GPS missing values, duplicates, and required columns
print("\n--- GPS MISSING VALUES ---")
print(df.isnull().sum())
print("GPS duplicate records:", df.duplicated().sum())

required_columns = ["device_id", "latitude", "longitude", "timestamp"]
print("\n--- REQUIRED GPS FIELDS (FIRST 10 ROWS) ---")
print(df[required_columns].head(10))

# GPS coordinate validation
invalid_coordinates = df[
    (~df["latitude"].between(-90, 90)) |
    (~df["longitude"].between(-180, 180))
]
print("\nLatitude range:", df["latitude"].min(), df["latitude"].max())
print("Longitude range:", df["longitude"].min(), df["longitude"].max())
print("Invalid coordinates:", len(invalid_coordinates))

# Inspect store dataset
print("\n--- STORE FIRST 5 ROWS ---")
print(store_df.head())
print("\n--- STORE DATASET INFO ---")
store_df.info()

# Store missing values and duplicates
print("\n--- STORE MISSING VALUES ---")
print(store_df.isnull().sum())
print("Store duplicate records:", store_df.duplicated().sum())
print("Duplicate Store IDs:", store_df["store_id"].duplicated().sum())

# Check GPS-to-store ID matching
unmatched_stores = df[
    ~df["nearest_store_id"].isin(store_df["store_id"].unique())
]
print("Unmatched Store IDs:", len(unmatched_stores))

# Export validation results
results = {
    "GPS total records": len(df),
    "GPS total columns": len(df.columns),
    "Unique GPS devices": df["device_id"].nunique(),
    "GPS missing values (all columns)": int(df.isnull().sum().sum()),
    "GPS duplicate records": int(df.duplicated().sum()),
    "Minimum latitude": df["latitude"].min(),
    "Maximum latitude": df["latitude"].max(),
    "Minimum longitude": df["longitude"].min(),
    "Maximum longitude": df["longitude"].max(),
    "Invalid GPS coordinates": len(invalid_coordinates),
    "Store total records": len(store_df),
    "Store total columns": len(store_df.columns),
    "Store missing values (all columns)": int(store_df.isnull().sum().sum()),
    "Store duplicate records": int(store_df.duplicated().sum()),
    "Duplicate Store IDs": int(store_df["store_id"].duplicated().sum()),
    "Unmatched Store IDs": len(unmatched_stores),
}
results_df = pd.DataFrame(
    [{"Validation": key, "Result": value} for key, value in results.items()]
)
results_df.to_csv("GeoPulse_Validation_Results.csv", index=False)
print("\nSaved: GeoPulse_Validation_Results.csv")
