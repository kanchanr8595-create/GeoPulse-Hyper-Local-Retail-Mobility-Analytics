# GeoPulse – Store Coordinate Validation Results
**Database:** GEOPULSE_DB  
**Schema:** PUBLIC  
**Table:** RAW_STORE_LOCATIONS

## 1. Total Store Records

**Result:**

| TOTAL_STORES |
|---:|
| 3 |

**Observation:** Three store-location records were successfully loaded into Snowflake.

## 2. Store-Location Metadata

| STORE_ID | STORE_NAME | STORE_STATUS | LATITUDE | LONGITUDE | CATCHMENT_RADIUS_M |
|---|---|---|---:|---:|---:|
| STORE_A | Cyber Hub Coffee | existing | 28.4956 | 77.0895 | 500 |
| STORE_C | Sector 29 Coffee | existing | 28.4662 | 77.0620 | 500 |
| CANDIDATE_B | Golf Course Road Candidate | candidate | 28.4595 | 77.0945 | 500 |

**Observation:** The table contains two existing stores and one candidate store. All three records include latitude, longitude, and a catchment radius of 500 metres.

## 3. Table Structure Verification

The `DESC TABLE` operation returned six columns.

| Column Name | Data Type |
|---|---|
| STORE_ID | VARCHAR(16777216) |
| STORE_NAME | VARCHAR(16777216) |
| STORE_STATUS | VARCHAR(16777216) |
| LATITUDE | NUMBER(38,4) |
| LONGITUDE | NUMBER(38,4) |
| CATCHMENT_RADIUS_M | NUMBER(38,0) |

**Observation:** The table structure contains the required store identifiers, names, status, geographic coordinates, and catchment radius.

## 4. Missing-Value Validation

| Validation | Result |
|---|---:|
| Total Records | 3 |
| Missing Store IDs | 0 |
| Missing Store Names | 0 |
| Missing Latitudes | 0 |
| Missing Longitudes | 0 |

**Observation:** No missing values were found in the validated fields.

## 5. Duplicate Store ID Validation

| Validation | Result |
|---|---:|
| Total Records | 3 |
| Unique Store IDs | 3 |
| Duplicate Store IDs | 0 |

**Observation:** All three store IDs are unique.

## 6. Coordinate Range Validation

| Validation | Result |
|---|---:|
| Total Records | 3 |
| Invalid Latitudes | 0 |
| Invalid Longitudes | 0 |

**Observation:** All latitude and longitude values fall within valid geographic ranges.

## 7. GPS-to-Store Metadata Mapping

The GPS records were joined with the store-location metadata using `NEAREST_STORE_ID` and `STORE_ID`.

| GPS Records | Store ID | Store Name | Latitude | Longitude |
|---:|---|---|---:|---:|
| 101 | CANDIDATE_B | Golf Course Road Candidate | 28.4595 | 77.0945 |
| 214 | STORE_A | Cyber Hub Coffee | 28.4956 | 77.0895 |
| 185 | STORE_C | Sector 29 Coffee | 28.4662 | 77.0620 |
| **500** | | **Total** | | |

**Observation:**
- All three store IDs appeared in the mapping results.
- GPS records were associated with the corresponding store names and coordinates.
- The three groups account for all 500 GPS records.

## 8. Conclusion

The store-location dataset was successfully loaded into Snowflake and verified. The three records contain complete store identifiers and coordinate information. Duplicate ID and coordinate range checks returned no issues.

The GPS-to-store mapping also returned all three store locations.

**Status:** Store-coordinate metadata verification completed.

**Tools Used:** Snowflake, SQL, CSV, GitHub.
