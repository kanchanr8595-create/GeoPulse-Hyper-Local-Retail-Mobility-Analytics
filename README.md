# GeoPulse – Hyper-Local Retail Mobility Analytics

## Project Overview

GeoPulse – Hyper-Local Retail Mobility Analytics is a four-week data analytics project focused on understanding city foot traffic, retail store catchment areas, and visitor movement patterns using synthetic and anonymized mobile GPS data.

The project aims to build a geospatial analytics pipeline to analyse movement patterns, identify visitor overlap between retail locations, and help a coffee-chain real estate team assess potential store-location cannibalization risk.

## Project Objectives

- Generate and prepare synthetic mobile GPS movement data.
- Set up Snowflake for storing and managing GPS records.
- Load and validate raw GPS data in Snowflake.
- Maintain store reference data, including store identifiers and coordinates.
- Analyse store-wise and hourly visitor information.
- Support the identification of visitor overlap between retail locations.
- Prepare structured data for spatial analysis, dbt modelling, and visualization.
- Maintain SQL queries, documentation, and validation evidence in GitHub.

## My Role and Responsibilities

**Role: Synthetic GPS Dataset Preparation and Snowflake Data Management**

My primary responsibilities in the GeoPulse project focus on preparing synthetic GPS data, setting up Snowflake tables, loading raw records, maintaining store reference information, and performing basic SQL-based data verification.

### Key Responsibilities

- Research GPS data fields and Snowflake input requirements.
- Define the synthetic GPS dataset structure.
- Prepare mock GPS records containing DeviceID, latitude, longitude, and timestamp.
- Set up Snowflake tables and load raw GPS data.
- Verify store coordinates and maintain store reference data.
- Execute basic SQL queries to check source-table counts and loading results.
- Prepare store-wise and hourly visitor extracts for team analysis.
- Support store comparison and footfall analysis by providing verified data.
- Document Snowflake tables, data-loading procedures, SQL queries, and verification results.
- Maintain project documentation and meaningful commits in GitHub.

## Tools and Technologies

- **Python** – Synthetic GPS data preparation and movement-data generation as part of the team workflow.
- **Snowflake** – Cloud data storage, raw GPS data loading, and SQL querying.
- **SQL** – Data exploration, record counting, and data verification.
- **PySpark / Apache Sedona** – Geospatial processing and spatial analysis within the team pipeline.
- **dbt** – Data transformation, modelling, and validation.
- **Kepler.gl** – Geospatial data visualization.
- **React** – Map interface development.
- **Airflow** – Workflow orchestration and pipeline automation.
- **Git and GitHub** – Version control, documentation, and team collaboration.

## Dataset Overview

The project uses synthetic and anonymized mobile GPS ping records to represent device movement across a city.

**Planned GPS data fields:**

| Field | Description |
|---|---|
| DeviceID | Identifier representing a mobile device |
| Lat | Latitude coordinate of the GPS location |
| Long | Longitude coordinate of the GPS location |
| Timestamp | Date and time associated with the GPS ping |

**Store Reference Data:**

Store reference information includes store identifiers and location coordinates required to support store-wise comparisons and geospatial analysis.

## Weekly Work Plan and Responsibilities

### Week 1 – Data Synthesis and Snowflake Setup

- Researched GPS data fields and Snowflake input requirements.
- Planned the synthetic GPS dataset structure and target-store metadata.
- Prepared mock GPS records containing DeviceID, latitude, longitude, and timestamp.
- Set up Snowflake tables and loaded raw GPS data.
- Prepared raw-data loading evidence and Snowflake table details.

### Week 2 – Spatial Joins and dbt Modelling Support

- Verified the raw GPS data loaded into Snowflake.
- Maintained store-coordinate metadata and store reference data.
- Checked store coordinates and supported Snowflake queries.
- Confirmed source-table record counts.
- Investigated loading and query issues and reconciled source row counts.
- Submitted Snowflake loading and query evidence for the mid-project review.

### Week 3 – Cannibalization Analysis and Store Comparison Support

- Provided store-wise and hourly visitor extracts.
- Verified source counts and store identifiers.
- Prepared store comparison figures.
- Supported existing-store performance comparison.
- Documented store-level visitor and footfall comparisons.
- Submitted store comparison findings for team review.

### Week 4 – Airflow Automation and Final Review Support

- Verified final Snowflake source and output tables.
- Documented Snowflake tables, data-loading procedures, and verification queries.
- Checked row counts and Snowflake outputs after pipeline execution.
- Finalized Snowflake documentation and supporting evidence.
- Prepared to present the GPS dataset, Snowflake setup, and data-loading process during the final review.

## Project Workflow

1. **GPS Data Preparation:** Generate synthetic and anonymized GPS movement records.
2. **Snowflake Setup:** Create the required Snowflake tables and load raw GPS data.
3. **Data Verification:** Check source-table counts, store coordinates, and data-loading results.
4. **Spatial Processing:** Use PySpark and Apache Sedona to create store catchment areas and perform spatial joins.
5. **Data Transformation:** Prepare cleaned and aggregated data using dbt.
6. **Visitor Analysis:** Calculate hourly unique visitors and analyse visitor overlap between stores.
7. **Cannibalization Analysis:** Estimate potential visitor overlap and store-location cannibalization risk.
8. **Visualization:** Present footfall and geospatial patterns using Kepler.gl and React.
9. **Automation:** Integrate the pipeline through Airflow.
10. **Final Documentation:** Maintain SQL scripts, data evidence, project documentation, and final presentation in GitHub.

## Expected Deliverables

My assigned deliverables include:

- Synthetic GPS dataset.
- Snowflake raw-data table.
- Store reference data and coordinate information.
- Snowflake loading evidence.
- Basic SQL verification queries and results.
- Store-wise and hourly visitor extracts.
- Store comparison findings.
- Snowflake documentation and final review evidence.

The broader team deliverables include spatial-join outputs, dbt models and tests, visitor-overlap analysis, Kepler.gl visualizations, React map interface, and Airflow workflow.

## Data Privacy and Limitations

The project uses synthetic and anonymized GPS data. Real personal location information should not be published in GitHub or shared outside the approved project environment.

Visitor overlap is an estimate of potential store-location cannibalization risk. It does not independently prove a percentage of lost sales or actual business impact. Project claims and results should be supported by actual query outputs and test evidence.

## Conclusion

GeoPulse combines data preparation, cloud data management, geospatial analytics, and visualization to understand retail mobility patterns. My contribution focuses on synthetic GPS dataset preparation, Snowflake setup and loading, store reference data management, basic SQL verification, and documentation. These activities provide the required data foundation for the team's spatial analysis, visitor-overlap investigation, and retail location assessment.
