# GeoPulse – Snowflake GPS Data Validation Results

## Objective

To verify the successful loading of raw GPS data into Snowflake, inspect the table structure, and analyze GPS pings by day of week using SQL queries.

## 1. Total GPS Records Verification

**SQL Query:**

```sql
SELECT COUNT(*) AS TOTAL_RECORDS
FROM GEOPULSE_DB.PUBLIC.RAW_GPS_PINGS;
```

**Result:**

| Metric | Value |
|---|---:|
| Total GPS Records | 500 |

**Observation:** A total of 500 GPS records were successfully loaded into the Snowflake table.

## 2. Snowflake Table Structure Verification

**SQL Query:**

```sql
DESC TABLE GEOPULSE_DB.PUBLIC.RAW_GPS_PINGS;
```

**Result:**

The table structure was successfully retrieved from Snowflake.

| Column Name | Data Type |
|---|---|
| PING_ID | VARCHAR(16777216) |
| DEVICE_ID | VARCHAR(16777216) |
| LATITUDE | NUMBER(38,6) |
| LONGITUDE | NUMBER(38,6) |
| TIMESTAMP | TIMESTAMP_NTZ(9) |
| ACTIVITY_AREA | VARCHAR(16777216) |
| DAY_OF_WEEK | VARCHAR(16777216) |
| HOUR | NUMBER(38,0) |
| DAYPART | VARCHAR(16777216) |
| MOVEMENT_MODE | VARCHAR(16777216) |
| GPS_ACCURACY_M | NUMBER(38,0) |
| IS_ANONYMIZED | BOOLEAN |
| NEAREST_STORE_ID | VARCHAR(16777216) |
| NEAREST_STORE_DISTANCE_M | NUMBER(38,1) |
| WITHIN_500M_OF_NEAREST_STORE | BOOLEAN |

**Observation:**
- Total columns: 15
- GPS coordinates use NUMBER(38,6).
- Timestamp uses TIMESTAMP_NTZ(9).
- Boolean fields include IS_ANONYMIZED and WITHIN_500M_OF_NEAREST_STORE.

## 3. GPS Pings by Day of Week

**SQL Query:**

```sql
SELECT
    DAY_OF_WEEK,
    COUNT(*) AS TOTAL_PINGS
FROM GEOPULSE_DB.PUBLIC.RAW_GPS_PINGS
GROUP BY DAY_OF_WEEK
ORDER BY DAY_OF_WEEK;
```

**Results:**

| Day | Total Pings |
|---|---:|
| Friday | 82 |
| Monday | 65 |
| Saturday | 71 |
| Sunday | 64 |
| Thursday | 78 |
| Tuesday | 71 |
| Wednesday | 69 |
| **Total** | **500** |

**Observations:**
- Friday recorded the highest number of GPS pings (82).
- Sunday recorded the lowest number (64).
- All seven days account for 500 GPS records.

## Conclusion

The raw GPS data was successfully loaded and verified in Snowflake. The total record count of 500 was confirmed, the table structure containing 15 columns was inspected, and GPS ping distribution across all seven days was analyzed using SQL queries.

**Status: Completed – Snowflake GPS Data Loading, Table Structure Verification, and Initial SQL Analysis.**

## Tools Used
- Snowflake
- SQL
- GitHub
