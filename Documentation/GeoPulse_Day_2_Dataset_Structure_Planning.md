# GeoPulse – Day 2: Dataset Structure Planning

## Objective
To design the structure of a synthetic GPS dataset and define the reference schema for target-store metadata as part of the GeoPulse project.

## Work Completed

### 1. Synthetic GPS Dataset Structure
Identified the required columns and proposed data types for storing GPS tracking records.

| Column Name | Data Type | Description |
|---|---|---|
| DeviceID | VARCHAR | Unique device identifier |
| Lat | FLOAT | GPS latitude coordinate |
| Long | FLOAT | GPS longitude coordinate |
| Timestamp | TIMESTAMP_NTZ | Date and time of GPS record |

### 2. Sample Synthetic GPS Records
Prepared illustrative GPS records for three devices to demonstrate the planned dataset structure.

| DeviceID | Lat | Long | Timestamp |
|---|---:|---:|---|
| D001 | 10.0150 | 76.3100 | 2026-11-12 09:00:00 |
| D002 | 10.0200 | 76.3150 | 2026-11-12 09:05:00 |
| D003 | 10.0250 | 76.3200 | 2026-11-12 09:10:00 |

### 3. Target-Store Metadata Planning
Defined the reference table structure required to store target-store information.

| Column Name | Data Type | Description |
|---|---|---|
| Store_ID | VARCHAR | Unique store identifier |
| Store_Name | VARCHAR | Retail store name |
| Latitude | FLOAT | Store latitude |
| Longitude | FLOAT | Store longitude |

### 4. Snowflake GEOGRAPHY Planning
Reviewed the project requirement for a Snowflake raw table containing a `GEOGRAPHY` column. This column will represent GPS coordinates as geographic locations and support future location-based analysis.

## Expected Outcome
- Defined the GPS dataset schema and proposed data types.
- Prepared sample synthetic GPS records.
- Planned the target-store metadata reference structure.
- Identified the Snowflake `GEOGRAPHY` requirement for the raw table.
- Established the initial structure for the next stage of synthetic data generation and Snowflake integration.

## Next Steps
Proceed with synthetic GPS data generation, target-store metadata preparation, and Snowflake raw table implementation.

