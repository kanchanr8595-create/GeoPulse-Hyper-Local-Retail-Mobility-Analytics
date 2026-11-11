# GeoPulse – Day 1: Snowflake Research

## 1. What is Snowflake?

Snowflake is a cloud-based data platform used to store, manage, process, and analyse structured and semi-structured data. It provides a scalable environment for handling data using SQL.

## 2. Purpose of Snowflake in GeoPulse

Snowflake will be used as the central data storage platform for the GeoPulse project. It will store synthetic GPS records and reference data. SQL queries will be used to retrieve, validate, and analyse the stored information.

## 3. Important Snowflake Concepts

- **Database:** An organized container used to store and manage data.
- **Schema:** A logical structure inside a database used to organize database objects such as tables and views.
- **Table:** A database object that stores data in rows and columns.
- **GEOGRAPHY:** A data type used to represent geographical features such as points, lines, and polygons.
- **CSV:** A comma-separated values file format used to store tabular data and transfer records into Snowflake.

## 4. Required GPS Fields

The following fields are required for storing synthetic GPS records in the GeoPulse project:

| Field Name | Description |
|---|---|
| DeviceID | Unique identifier of the GPS device |
| Latitude | Geographical latitude coordinate |
| Longitude | Geographical longitude coordinate |
| Timestamp | Date and time when the GPS record was captured |

## 5. Planned Data Loading Process

The planned workflow for loading GPS records into Snowflake is:

1. Prepare synthetic GPS data.
2. Export the prepared data into CSV format.
3. Create a database and schema in Snowflake.
4. Create a table with the required GPS fields.
5. Load the CSV data into the Snowflake table.
6. Verify the loaded records using SQL queries.

**Workflow:**

Prepare GPS Data → Export CSV → Create Snowflake Table → Load Data → Verify Records Using SQL

## 6. Expected Outcome

- Understand the basic concepts and architecture of Snowflake.
- Identify the database, schema, and table structure required for the GeoPulse project.
- Understand the required GPS fields and geographical data representation.
- Gain knowledge of the CSV-based data-loading process.
- Prepare for upcoming Snowflake implementation and SQL-based data validation tasks.

## Day 1 Summary

Completed the initial research on Snowflake, explored its important concepts, identified the required GPS data fields, and understood the planned workflow for storing and verifying synthetic GPS records in the GeoPulse project.

**Status:** Completed – Snowflake fundamentals and GPS data-loading requirements researched.
