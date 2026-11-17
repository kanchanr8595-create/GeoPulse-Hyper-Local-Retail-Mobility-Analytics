# Objectives of Data Quality Checking
The main objectives are:
## 1.Identify missing values or null values.
## 2.Detect Duplicate records.
## 3.Validate DeviceID and values.
## 4.Check latitude and longitude ranges.
## 5.Validate timestamp formats.
## 6.Identify invalid pr unusual GPS records.
## 6.Ensure store location is suitable for geospatial analysis.
## 7.Prepare clean and reliable data for further processing.

## Data Validation Rules:

# DeviceID Validation:
 #### 1..DeviceID should not contain null values.
 #### 2.DeviceID should follow consistent format.
 #### 3.DeviceID should not contain unexpected blank spaces.
 #### 3..Device identifiers should be checked for consistency across record.

## Latitude Validation:
 #### 1.Latitude must be within the range of -90 to +90.
 #### 2.Latitude should not contain null values.
 #### 3.Values outside the valid geographic range should be treated as invalid.

## Longitude Validation:
 #### 1.Longitude must be within the range of -180 to +180.
 #### 2.Latitude should not contain null values.
 #### 3.Values outside the valid geographic range should be treated as invalid.

## Timestamp Validation:
 #### 1.Timestamp should follow a valid date-time format.
 #### 2.Timestamp Should not contain null values.
 #### 3.Invalid date-time values should be identified.
 #### 4.GPS records should be checked for unexpected chronological inconsistencies.

## Duplicate Validation:
 #### 1.Identify completely duplicated rows.
 #### 2.Check duplicate GPS records.
 #### 3.Check repeated store identifiers in the store reference dataset.
 #### 4.Investigate repeated device and timestamp combinations.


