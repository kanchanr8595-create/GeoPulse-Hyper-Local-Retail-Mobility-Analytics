# GeoPulse – Source Table Verification

## 1. Objective

To support Snowflake queries and confirm the source-table record counts, table structures, and key identifier completeness for the GeoPulse project.

## 2. Activities Completed

- Reviewed the GPS source table `RAW_GPS_PINGS`.
- Reviewed the store reference table `RAW_STORE_LOCATIONS`.
- Executed SQL queries to confirm the record counts of both source tables.
- Inspected column names, data types, and column positions using Snowflake INFORMATION_SCHEMA.
- Checked the source tables for missing key identifiers.
- Confirmed that both tables are available in the `GEOPULSE_DB.PUBLIC` schema.

## 3. Source Table Verification Results

| Source Table | Total Records | Total Columns |
|---|---:|---:|
| RAW_GPS_PINGS | 500 | 15 |
| RAW_STORE_LOCATIONS | 3 | 6 |
| **Total** | **503** | **21** |

## 4. Missing Identifier Validation

| Source Table | Total Records | Missing IDs |
|---|---:|---:|
| RAW_GPS_PINGS | 500 | 0 |
| RAW_STORE_LOCATIONS | 3 | 0 |

Both source tables returned zero missing key identifiers.

## 5. Key Findings

- The GPS source table contains 500 records and 15 columns.
- The store reference table contains 3 records and 6 columns.
- Both table structures were reviewed successfully.
- All expected source-table records were confirmed.
- No missing GPS Ping IDs or Store IDs were detected.

## 6. Tools Used

- Snowflake
- SQL
- INFORMATION_SCHEMA
- GitHub

## 7. Conclusion

The GeoPulse source tables were successfully reviewed and verified in Snowflake. The expected record counts, table structures, and key identifier completeness were confirmed. Both source tables are available for further SQL analysis and subsequent project activities.

**Task Status: Completed**
