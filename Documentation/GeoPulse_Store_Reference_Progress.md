# GeoPulse – Store Reference Data Validation

## Objective

Review and maintain store reference data in Snowflake by validating store coordinates, catchment radius, store status, and unique store identifiers.

## Activities Completed

- Reviewed the existing `RAW_STORE_LOCATIONS` table.
- Validated latitude and longitude ranges.
- Checked the expected 500m catchment radius for all stores.
- Verified the distribution of existing and candidate stores.
- Checked store ID uniqueness and duplicate records.

## Key Results

- Total store records: 3
- Existing stores: 2
- Candidate stores: 1
- Valid coordinate and radius records: 3
- Duplicate store IDs: 0

## Conclusion

All reviewed store reference records passed the validation checks. No updates were required based on the results.

**Tools:** Snowflake SQL, GitHub

**Status:** Completed
