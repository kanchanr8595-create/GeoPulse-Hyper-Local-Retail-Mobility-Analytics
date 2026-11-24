# Store Reference Data Validation – Results

## 1. Objective

To review and validate store reference data in Snowflake, check coordinate values, verify catchment radius and store status, and identify duplicate store IDs.

## 2. Snowflake Table

- Database: `GEOPULSE_DB`
- Schema: `PUBLIC`
- Table: `RAW_STORE_LOCATIONS`
- Total records: 3

## 3. Store Reference Data

| Store ID | Store Name | Status | Latitude | Longitude | Radius |
|---|---|---|---:|---:|---:|
| CANDIDATE_B | Golf Course Road Candidate | Candidate | 28.4595 | 77.0945 | 500 m |
| STORE_A | Cyber Hub Coffee | Existing | 28.4956 | 77.0895 | 500 m |
| STORE_C | Sector 29 Coffee | Existing | 28.4662 | 77.0620 | 500 m |

## 4. Validation Results

### Coordinate and Radius Validation

| Store ID | Validation Status |
|---|---|
| CANDIDATE_B | VALID |
| STORE_A | VALID |
| STORE_C | VALID |

All three records passed the latitude, longitude, and expected 500m catchment-radius checks.

### Store Status Distribution

| Store Status | Count |
|---|---:|
| Candidate | 1 |
| Existing | 2 |
| Total | 3 |

### Duplicate Store ID Check

| Metric | Result |
|---|---:|
| Total Records | 3 |
| Unique Store IDs | 3 |
| Duplicate Store IDs | 0 |

## 5. Conclusion

The store reference data passed all validation checks performed. All three records have valid coordinate ranges and the expected catchment radius. Store status distribution is consistent, and no duplicate store IDs were found.

No reference-data corrections were required based on these checks.

## 6. Tools Used

- Snowflake
- SQL
- GitHub
