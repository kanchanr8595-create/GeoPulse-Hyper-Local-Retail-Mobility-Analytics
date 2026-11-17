
# ============================================================
# GeoPulse Project - GPS Data Preparation and Validation
# Purpose: Load, inspect and validate GPS ping and store data
# Tools: Python, Pandas, Google Colab
# ============================================================


# STEP 1: Import required libraries

import pandas as pd

# Pandas is used for loading, cleaning and analysing CSV data.


# STEP 2: Load the GPS dataset

df = pd.read_csv('/content/GeoPulse_500_Synthetic_GPS_Pings.csv')

# Display the first five records
print("GPS Dataset - First Five Records")
print(df.head())


# STEP 3: Inspect GPS dataset structure

print("\nGPS Dataset Information")
df.info()

# Display the number of rows and columns
print("\nGPS Dataset Shape:")
print(df.shape)


# STEP 4: Convert timestamp column into datetime format

df['timestamp'] = pd.to_datetime(df['timestamp'])

print("\nTimestamp Data Type:")
print(df['timestamp'].dtype)


# STEP 5: Check required GPS columns

required_columns = [
    'device_id',
    'latitude',
    'longitude',
    'timestamp'
]

print("\nRequired GPS Columns:")
print(df[required_columns].head(10))

# These columns contain the essential GPS tracking information.


# STEP 6: Check missing values in GPS dataset

print("\nMissing Values in GPS Dataset:")
print(df.isnull().sum())

# Count total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())


# STEP 7: Check duplicate records in GPS dataset

print("\nDuplicate GPS Records:")
print(df.duplicated().sum())

# This checks whether complete rows are repeated.


# STEP 8: Validate latitude and longitude ranges

print("\nLatitude Range:")
print(df['latitude'].min(), df['latitude'].max())

print("\nLongitude Range:")
print(df['longitude'].min(), df['longitude'].max())

# Latitude must be between -90 and 90.
# Longitude must be between -180 and 180.

invalid_coordinates = df[
    (~df['latitude'].between(-90, 90)) |
    (~df['longitude'].between(-180, 180))
]

print("\nInvalid Coordinates:")
print(len(invalid_coordinates))


# STEP 9: Load the store locations dataset

store_df = pd.read_csv('/content/GeoPulse_Store_Locations.csv')

print("\nStore Dataset - First Five Records")
print(store_df.head())


# STEP 10: Inspect store dataset structure

print("\nStore Dataset Information")
store_df.info()

print("\nStore Dataset Shape:")
print(store_df.shape)


# STEP 11: Check missing values in store dataset

print("\nMissing Values in Store Dataset:")
print(store_df.isnull().sum())

# Count total missing values
print("\nTotal Missing Values in Store Dataset:")
print(store_df.isnull().sum().sum())


# STEP 12: Check duplicate store records

print("\nDuplicate Store Records:")
print(store_df.duplicated().sum())

# Check whether any store IDs are repeated
print("\nDuplicate Store IDs:")
print(store_df['store_id'].duplicated().sum())


# STEP 13: Validate GPS Store ID matching

valid_store_ids = store_df['store_id'].unique()

unmatched_stores = df[
    ~df['nearest_store_id'].isin(valid_store_ids)
]

print("\nUnmatched Store IDs:")
print(len(unmatched_stores))

# This checks whether GPS records refer to valid store IDs.


# STEP 14: Display final validation summary

print("\n========== GPS VALIDATION SUMMARY ==========")

print("Total GPS Records:", len(df))
print("Total GPS Columns:", len(df.columns))
print("Unique Devices:", df['device_id'].nunique())
print("Missing GPS Values:", df.isnull().sum().sum())
print("Duplicate GPS Records:", df.duplicated().sum())
print("Invalid Coordinates:", len(invalid_coordinates))

print("\n========== STORE VALIDATION SUMMARY ==========")

print("Total Store Records:", len(store_df))
print("Total Store Columns:", len(store_df.columns))
print("Missing Store Values:", store_df.isnull().sum().sum())
print("Duplicate Store Records:", store_df.duplicated().sum())
print("Duplicate Store IDs:", store_df['store_id'].duplicated().sum())
print("Unmatched Store IDs:", len(unmatched_stores))


# STEP 15: Export validation results to CSV

results = {
    'Validation Check': [
        'Total GPS Records',
        'Total GPS Columns',
        'Unique Devices',
        'Missing GPS Values',
        'Duplicate GPS Records',
        'Invalid Coordinates',
        'Total Store Records',
        'Total Store Columns',
        'Missing Store Values',
        'Duplicate Store Records',
        'Duplicate Store IDs',
        'Unmatched Store IDs'
    ],

    'Result': [
        len(df),
        len(df.columns),
        df['device_id'].nunique(),
        df.isnull().sum().sum(),
        df.duplicated().sum(),
        len(invalid_coordinates),
        len(store_df),
        len(store_df.columns),
        store_df.isnull().sum().sum(),
        store_df.duplicated().sum(),
        store_df['store_id'].duplicated().sum(),
        len(unmatched_stores)
    ]
}

results_df = pd.DataFrame(results)

# Save validation summary as a CSV file
results_df.to_csv('GeoPulse_Validation_Results.csv', index=False)

print("\nValidation results exported successfully!")
