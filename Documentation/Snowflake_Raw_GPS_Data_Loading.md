# GeoPulse – Snowflake Setup and Raw GPS Data Loading

## Objective
To set up Snowflake and prepare the environment for loading the raw GPS dataset.

## Work Completed
- Created a Snowflake trial account.
- Accessed the Snowflake workspace.
- Selected the `GEOPULSE_DB` database and `PUBLIC` schema.
- Selected the option to create a new table.
- Entered `RAW_GPS_PINGS` as the target table name.
- Selected the GPS CSV file for upload.
- Reached the **Load Data into Table** screen.
- Reviewed the schema preview, including column names, data types, and sample data.

## Current Status
Snowflake setup and initial CSV upload configuration are completed. The data loading process is pending final schema verification.

## Next Steps
1. Verify all column names and data types.
2. Load the raw GPS data into the Snowflake table.
3. Run SQL queries to verify the loaded records.
4. Capture screenshots of the loading process and query results.

## Tools Used
- Snowflake
- Python
- Pandas
- GitHub
