# GeoPulse – Hyper-Local Retail Mobility Analytics

##  Project Overview

GeoPulse is a geospatial analytics project designed to analyze city-level human mobility patterns using anonymized, synthetic mobile GPS data. The project focuses on understanding retail foot traffic, identifying store catchment areas, measuring visitor overlap between retail locations, and estimating potential store cannibalization risks.

The project aims to help retail businesses, particularly coffee chains, make better decisions when selecting new store locations by understanding customer movement patterns and geographical relationships between existing and potential stores.

# Project Objectives

- Analyze synthetic GPS location data to understand customer movement patterns.
- Identify store catchment areas using 500-metre geographical buffers.
- Perform spatial joins to identify GPS points falling within store catchment areas.
- Calculate hourly unique visitors for each retail location.
- Analyze visitor overlap between multiple stores.
- Estimate potential store cannibalization risks.
- Visualize geographical foot traffic patterns using interactive maps.
- Build an automated and reliable geospatial data analytics pipeline.

# Project Workflow

The project follows a structured data engineering and analytics workflow:

1. Data Generation: Prepare synthetic mobile GPS data containing DeviceID, Latitude, Longitude and Timestamp.
2. Data Storage: Load raw GPS records into Snowflake.
3. Data Processing: Use Python and PySpark with Apache Sedona for geospatial processing.
4. Spatial Analysis: Create 500-metre store catchment areas and perform spatial joins.
5. Data Transformation: Use dbt to clean, transform and aggregate GPS and store data.
6. Foot Traffic Analysis: Calculate hourly unique visitors for individual stores.
7. Cannibalization Analysis: Identify devices visiting multiple stores and estimate visitor overlap.
8. Visualization: Present geographical insights using Kepler.gl and React.
9. Pipeline Automation: Use Apache Airflow to orchestrate the end-to-end workflow.

Technologies Used

Technology| Purpose
Python| Data processing and analysis
Snowflake| Cloud data storage and SQL queries
PySpark| Large-scale data processing
Apache Sedona| Geospatial analysis and spatial joins
dbt| Data transformation, testing and documentation
SQL| Data querying and visitor overlap analysis
Kepler.gl| Geospatial data visualization
React| Interactive map interface
Apache Airflow| Workflow automation and orchestration

My Role and Responsibilities

Team Member: Akshaya

My primary responsibility in this project is Data Quality, dbt Modeling, Testing and Validation.

My contributions include:

- Preparing data quality checklists and validation rules.
- Inspecting GPS datasets for missing values, duplicate records and invalid data.
- Validating DeviceID, latitude, longitude and timestamp fields.
- Preparing dbt staging models for cleaned GPS and store data.
- Developing hourly unique visitor aggregation models.
- Implementing dbt tests to maintain data accuracy and consistency.
- Validating DeviceID-based store visitor overlap calculations.
- Checking percentage denominators and time-window consistency.
- Documenting data integrity checks, validation results and exceptions.
- Preparing technical documentation and evidence for the final project.

Expected Project Deliverables

- Synthetic GPS dataset and data dictionary.
- Snowflake raw data tables.
- 500-metre store catchment areas.
- PySpark/Sedona spatial processing pipeline.
- dbt staging and aggregation models.
- Hourly unique visitor analysis.
- Store visitor overlap and cannibalization-risk estimates.
- Interactive Kepler.gl map visualization.
- React-based map interface.
- Apache Airflow workflow.
- Data quality reports, validation evidence and project documentation.

Business Value

GeoPulse aims to support retail expansion and location-planning decisions through geospatial insights.

The analysis can help businesses:

- Understand customer movement and foot traffic.
- Identify geographical areas with potential retail demand.
- Compare visitor patterns across different store locations.
- Identify overlapping customer visits between stores.
- Evaluate potential store-location cannibalization risks.
- Make more informed decisions about future store expansion.

Important: Visitor overlap is an estimate of potential cannibalization risk. It does not directly represent lost sales or prove actual revenue cannibalization.


Project Status

In Progress

This project uses synthetic and anonymized GPS data for analytical and demonstration purposes. Final results and performance claims will be documented based on actual execution and validation evidence. 
