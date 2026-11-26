# GeoPulse – Source Loading and Row Count Reconciliation

## 1. Objective

To investigate potential Snowflake loading and query issues and reconcile the source CSV record counts with the records available in the Snowflake source tables.

## 2. Activities Completed

- Verified the GPS source table `RAW_GPS_PINGS`.
- Verified the store reference table `RAW_STORE_LOCATIONS`.
- Compared the current Snowflake row counts with the expected source dataset counts.
- Checked for duplicate GPS Ping IDs and Store IDs.
- Checked for missing key identifiers in both source tables.
- Reviewed Snowflake loading history using the `COPY_HISTORY` function.
- Verified the number of rows parsed and loaded from both CSV files.
- Identified and corrected an initial SQL compilation issue with the `COPY_HISTORY` function.

## 3. Source Table Row Count Reconciliation

| Source Table | Expected Rows | Actual Rows | Difference |
|---|---:|---:|---:|
| RAW_GPS_PINGS | 500 | 500 | 0 |
| RAW_STORE_LOCATIONS | 3 | 3 | 0 |
| **Total** | **503** | **503** | **0** |

Both Snowflake source tables matched their expected record counts.

## 4. Duplicate and Missing Identifier Validation

| Source Table | Total Records | Duplicate IDs | Missing IDs |
|---|---:|---:|---:|
| RAW_GPS_PINGS | 500 | 0 | 0 |
| RAW_STORE_LOCATIONS | 3 | 0 | 0 |

No duplicate or missing key identifiers were detected.

## 5. Snowflake CSV Loading History

| Source Table | CSV File | Status | Rows Parsed | Rows Loaded |
|---|---|---|---:|---:|
| RAW_GPS_PINGS | GeoPulse_500_Synthetic_GPS_Pings (1).csv | Loaded | 500 | 500 |
| RAW_STORE_LOCATIONS | GeoPulse_Store_Locations (1).csv | Loaded | 3 | 3 |

Snowflake loading history showed that all expected records were successfully parsed and loaded. The error message field was empty for both loading results.

## 6. Query Issue and Resolution

During the initial loading-history verification, the `COPY_HISTORY` function returned a SQL compilation error because the query did not provide the required arguments. The query was corrected by specifying the table name and start time. The corrected queries successfully retrieved the loading history for both source tables.

## 7. Key Findings

- A total of 503 source records were verified.
- All 500 GPS records were successfully loaded.
- All 3 store reference records were successfully loaded.
- Both source tables matched their expected row counts.
- No duplicate or missing key identifiers were found.
- No loading errors were reported in the returned Snowflake history.

## 8. Tools Used

- Snowflake
- SQL
- COPY_HISTORY
- GitHub

## 9. Conclusion

The GeoPulse source-table loading and row-count reconciliation checks were completed successfully. Both CSV files were confirmed as loaded in Snowflake, and their parsed and loaded record counts matched the expected source counts. No discrepancies, duplicate identifiers, or missing key identifiers were identified. The initial query syntax issue was also resolved, allowing the loading history to be verified successfully.

**Task Status: Completed**
