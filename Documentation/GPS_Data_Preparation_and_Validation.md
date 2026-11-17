# GeoPulse – GPS Data Preparation and Validation

## 1. Objective

The objective of this task was to prepare, inspect, and validate the synthetic GPS tracking dataset and store location reference dataset provided by the team lead.

The validation process ensures that the datasets have the required structure, contain valid GPS coordinates, and have no missing or duplicate records.

## 2. Datasets Used

Two CSV datasets were used for this task.

### GPS Pings Dataset
- **File:** `GeoPulse_500_Synthetic_GPS_Pings.csv`
- **Total Records:** 500
- **Total Columns:** 15

Important columns:
- `device_id` – Unique identifier for the device
- `latitude` – GPS latitude coordinate
- `longitude` – GPS longitude coordinate
- `timestamp` – Date and time of the GPS ping
- `nearest_store_id` – Identifier of the nearest store

### Store Locations Dataset
- **File:** `GeoPulse_Store_Locations.csv`
- **Total Records:** 3
- **Total Columns:** 6

Important columns:
- `store_id` – Unique store identifier
- `store_name` – Store name
- `store_status` – Store status
- `latitude` – Store latitude
- `longitude` – Store longitude
- `catchment_radius_m` – Store catchment radius in metres

## 3. Tools and Technologies

- Python
- Google Colab
- Pandas
- NumPy
- CSV datasets
- GitHub

## 4. Data Preparation and Validation Process

The following activities were performed using Python.

1. Imported the required Python libraries.
2. Loaded both GPS and store location CSV datasets.
3. Inspected the datasets using `head()`, `info()`, and `shape`.
4. Converted the GPS timestamp column into datetime format.
5. Selected and inspected the required GPS fields: DeviceID, Latitude, Longitude, and Timestamp.
6. Checked for missing values in both datasets.
7. Identified duplicate records in the GPS dataset.
8. Checked the latitude and longitude ranges.
9. Validated GPS coordinates against the standard geographical coordinate ranges.
10. Checked duplicate store records and duplicate store IDs.
11. Verified whether GPS records referenced valid store IDs.
12. Generated a validation summary and exported the results into a CSV file.

## 5. Validation Results

| Validation Check | Result |
|---|---:|
| Total GPS Records | 500 |
| GPS Dataset Columns | 15 |
| Unique Devices | 118 |
| Missing GPS Values | 0 |
| Duplicate GPS Records | 0 |
| Invalid Coordinates | 0 |
| Total Store Records | 3 |
| Store Dataset Columns | 6 |
| Missing Store Values | 0 |
| Duplicate Store Records | 0 |
| Duplicate Store IDs | 0 |
| Unmatched Store IDs | 0 |

## 6. Key Observations

- The GPS dataset contains 500 records from 118 unique devices.
- All required GPS fields were available for inspection.
- No missing values were identified in either dataset.
- No duplicate GPS records or duplicate store records were found.
- All GPS coordinates were within valid geographical ranges.
- All GPS records were successfully matched with the available store IDs.

## 7. Output Files

The following files were organised for the project repository:

- `GeoPulse_GPS_Data_Validation.py` – Python code used for dataset preparation and validation.
- `GeoPulse_Validation_Results.csv` – Exported validation summary.
- Original GPS Pings and Store Locations CSV datasets.

## 8. Conclusion

The synthetic GPS pings dataset and store locations dataset were successfully inspected and validated using Python.

The validation checks identified no missing values, duplicate records, invalid GPS coordinates, or unmatched store IDs.

Both datasets are ready for the next stage of the GeoPulse project, including GPS location analysis and Snowflake data integration.
