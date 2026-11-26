# GeoPulse – Source Loading and Row Count Reconciliation Results

## 1. Source Table Count Results

| Source Table | Total Records |
|---|---:|
| RAW_GPS_PINGS | 500 |
| RAW_STORE_LOCATIONS | 3 |
| **Total** | **503** |

## 2. Row Count Reconciliation

| Source Table | Expected Rows | Actual Rows | Difference |
|---|---:|---:|---:|
| RAW_GPS_PINGS | 500 | 500 | 0 |
| RAW_STORE_LOCATIONS | 3 | 3 | 0 |

## 3. Duplicate Identifier Results

### GPS Ping ID Check

| Total Records | Unique Ping IDs | Duplicate Ping IDs |
|---:|---:|---:|
| 500 | 500 | 0 |

### Store ID Check

| Total Records | Unique Store IDs | Duplicate Store IDs |
|---:|---:|---:|
| 3 | 3 | 0 |

## 4. Missing Identifier Results

| Source Table | Total Records | Missing IDs |
|---|---:|---:|
| RAW_GPS_PINGS | 500 | 0 |
| RAW_STORE_LOCATIONS | 3 | 0 |

## 5. GPS CSV Loading History

| Field | Actual Result |
|---|---|
| Table Name | RAW_GPS_PINGS |
| File Name | GeoPulse_500_Synthetic_GPS_Pings (1).csv |
| Status | Loaded |
| Rows Parsed | 500 |
| Rows Loaded | 500 |
| First Error Message | Empty |

## 6. Store CSV Loading History

| Field | Actual Result |
|---|---|
| Table Name | RAW_STORE_LOCATIONS |
| File Name | GeoPulse_Store_Locations (1).csv |
| Status | Loaded |
| Rows Parsed | 3 |
| Rows Loaded | 3 |
| First Error Message | Empty |

## 7. Query Issue and Resolution

The initial COPY_HISTORY query returned a SQL compilation error because the function required two arguments. The query was corrected by specifying the table name and start time. Both corrected loading-history queries executed successfully.

## 8. Final Results

- Total source records verified: 503
- GPS records loaded: 500
- Store records loaded: 3
- Duplicate identifiers: 0
- Missing identifiers: 0
- Row-count differences: 0
- Loading status: Loaded for both tables
- Reported loading errors: None

## 9. Conclusion

Both source tables passed the row-count reconciliation and identifier checks. Snowflake loading history confirmed that all expected records were parsed and loaded successfully. No row-count discrepancies or reported loading errors were found.

**Status: Completed**
