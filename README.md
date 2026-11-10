# GeoPulse – Hyper-Local Retail Mobility Analytics

### Geospatial Analytics for Smarter Retail Location Decisions

## 1. Project Overview

GeoPulse is a geospatial retail analytics project designed to analyse anonymized mobile GPS foot traffic and customer movement patterns to support smarter retail location decisions.

The project focuses on understanding how people move around retail locations, identifying store catchment areas, measuring visitor overlap between stores, and estimating potential store cannibalization risks.

Using geospatial technologies and data analytics, GeoPulse aims to help retail businesses identify promising store locations and make data-driven decisions.

## 2. Problem Statement

Retail businesses often face challenges when selecting new store locations. Opening a new store too close to an existing one may result in overlapping customer traffic and potential revenue cannibalization.

Traditional location planning may not provide sufficient insights into actual movement patterns and customer overlap.

GeoPulse addresses this challenge by analysing synthetic and anonymized GPS mobility data, store locations, and commercial zoning areas to identify foot traffic patterns and potential location conflicts.

## 3. Project Objectives

- Generate synthetic GPS mobility data for analysis.
- Store and manage geospatial data using Snowflake.
- Create 500-meter store catchment areas.
- Perform spatial joins between GPS points and store catchment polygons.
- Calculate hourly unique visitor metrics.
- Identify DeviceID overlap across multiple retail stores.
- Estimate potential store cannibalization risks.
- Visualize customer movement and foot traffic patterns.
- Develop an interactive geospatial dashboard.
- Automate the analytical workflow.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Synthetic GPS data generation |
| Snowflake | Geospatial data storage |
| PySpark | Large-scale data processing |
| Apache Sedona | Geospatial operations and spatial joins |
| dbt | Data transformation and testing |
| SQL | Visitor overlap and cannibalization analysis |
| Kepler.gl | Geospatial data visualization |
| React | Interactive dashboard development |
| H3 | Hexagonal spatial aggregation |
| Apache Airflow | Workflow orchestration |

## 5. Project Workflow

The project follows an end-to-end geospatial analytics workflow:

1. **GPS Data Generation:** Generate synthetic GPS pings containing DeviceID, latitude, longitude, and timestamp.
2. **Data Storage:** Store raw GPS records and geospatial information in Snowflake.
3. **Catchment Area Creation:** Create 500-meter catchment zones around selected retail stores.
4. **Spatial Processing:** Use PySpark and Apache Sedona to perform spatial joins between GPS points and store polygons.
5. **Data Transformation:** Use dbt to clean, transform, and calculate hourly unique visitor metrics.
6. **Cannibalization Analysis:** Use SQL to identify overlapping DeviceIDs and estimate potential store cannibalization.
7. **Dashboard Development:** Visualize foot traffic, movement patterns, and H3 hexagonal maps using Kepler.gl and React.
8. **Pipeline Automation:** Use Apache Airflow to orchestrate the daily analytical workflow.

## 6. Key Project Modules

### Module 1 – Geospatial Data Engineering
- Synthetic GPS data generation.
- Snowflake geospatial tables.
- GPS data loading and management.

### Module 2 – Spatial Analysis
- Store catchment area creation.
- GPS point and polygon intersection.
- Spatial joins using PySpark and Sedona.

### Module 3 – Data Transformation
- Data cleaning and standardization.
- Hourly unique visitor aggregation.
- dbt models and data quality tests.

### Module 4 – Cannibalization Analysis
- DeviceID overlap analysis.
- Multi-store visitor comparison.
- Potential cannibalization risk estimation.

### Module 5 – Interactive Dashboard
- Kepler.gl mobility visualization.
- H3 hexagonal foot traffic maps.
- 24-hour timeline and movement patterns.

### Module 6 – Pipeline Orchestration
- Apache Airflow DAG development.
- Daily pipeline execution.
- End-to-end integration.

## 7. Repository Structure

```text
GeoPulse-Hyper-Local-Retail-Mobility-Analytics/
│
├── data/
├── python/
├── pyspark_sedona/
├── snowflake/
├── dbt/
├── sql/
├── airflow/
├── dashboard/
├── documentation/
│
└── README.md
```

## 8. Expected Deliverables

- Synthetic GPS mobility dataset.
- Snowflake geospatial database tables.
- Store catchment area analysis.
- Spatial join results.
- Hourly unique visitor metrics.
- DeviceID overlap and cannibalization analysis.
- Interactive Kepler.gl dashboard.
- H3-based foot traffic visualization.
- Automated Airflow workflow.
- Complete technical documentation.

## 9. Project Duration

**4 Weeks**

The project is planned across four weeks, covering data generation, geospatial processing, data transformation, cannibalization analysis, dashboard development, and final pipeline integration.

## 10. Data Privacy and Disclaimer

This project uses synthetic and anonymized GPS mobility data for educational and analytical purposes. It does not use real customer GPS records or personally identifiable information.

Cannibalization results represent potential visitor overlap and analytical risk estimates. Visitor overlap alone does not establish actual lost sales or revenue.

## 11. Team Collaboration

The project is developed collaboratively using GitHub.

Each team member works on an individual development branch, and completed work is reviewed before integration into the main branch.

**Project:** GeoPulse – Hyper-Local Retail Mobility Analytics  
**Domain:** Retail Strategy & Geospatial Analytics  
**Duration:** 4 Weeks
