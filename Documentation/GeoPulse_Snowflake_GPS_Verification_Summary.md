# GeoPulse – Snowflake GPS Data Loading and Verification

## 1. Objective

To upload the prepared synthetic GPS dataset into Snowflake, verify the successful data load, inspect the table structure, and perform an initial analysis of GPS records.

## 2. Activities Completed

- Accessed the Snowflake workspace and selected the `GEOPULSE_DB` database and `PUBLIC` schema.
- Created the target table `RAW_GPS_PINGS`.
- Uploaded the `GeoPulse_500_Synthetic_GPS_Pings.csv` dataset into Snowflake.
- Verified the uploaded data and confirmed the total number of records.
- Inspected the table structure and reviewed all available columns and their data types.
- Checked sample GPS records to confirm that the uploaded data was accessible.
- Performed an initial analysis of GPS pings based on the day of the week.
- Created a Snowflake SQL file containing the validation and analysis work.
- Prepared the SQL script and result documentation for GitHub.

## 3. Results and Observations

- Successfully loaded **500 GPS records** into the Snowflake table.
- Verified the table structure, which contains **15 columns**.
- Confirmed that GPS information, including device IDs, latitude, longitude, timestamps, movement details, and store-related metadata, is available in the table.
- Completed the day-of-week analysis, covering all 500 GPS records.
- Friday recorded the highest number of GPS pings (82), while Sunday recorded the lowest (64).

## 4. Tools and Technologies Used

- Snowflake – Data loading, table management, and verification.
- SQL – Data validation and initial analysis.
- GitHub – Code and project documentation management.
- CSV – Synthetic GPS dataset.

## 5. Conclusion

The Snowflake raw GPS data loading and initial verification activities were successfully completed. The uploaded dataset was verified, its table structure was inspected, and an initial analysis of GPS activity across different days was performed.

**Status:** Completed

**Next Step:** Verify the store-location dataset and provide store-coordinate metadata in Snowflake.
