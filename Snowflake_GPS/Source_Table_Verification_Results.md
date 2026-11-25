# GeoPulse – Source Table Verification Results

## Objective
To support Snowflake queries and confirm the record counts, schemas, and key identifier completeness of the GeoPulse source tables.

## Snowflake Details
- Database: GEOPULSE_DB
- Schema: PUBLIC

## Source Table Counts

| Source Table | Total Records |
|---|---:|
| RAW_GPS_PINGS | 500 |
| RAW_STORE_LOCATIONS | 3 |
| Total | 503 |

## Schema Verification

| Source Table | Total Columns |
|---|---:|
| RAW_GPS_PINGS | 15 |
| RAW_STORE_LOCATIONS | 6 |

Both source-table schemas were reviewed using INFORMATION_SCHEMA.COLUMNS.

## Missing Identifier Check

| Source Table | Total Records | Missing IDs |
|---|---:|---:|
| RAW_GPS_PINGS | 500 | 0 |
| RAW_STORE_LOCATIONS | 3 | 0 |

## Conclusion

Both GeoPulse source tables were successfully verified in Snowflake. The expected 500 GPS records and 3 store reference records were confirmed. All 15 GPS columns and 6 store columns were reviewed, and no missing key identifiers were found.

**Status:** Completed

**Tools:** Snowflake, SQL, GitHub
