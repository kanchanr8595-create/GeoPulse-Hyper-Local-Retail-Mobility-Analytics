
# Store Proximity and Catchment Analysis

## Objective
The objective of this analysis is to understand GPS
activity around different store locations.

## Data Sources
- Synthetic GPS Pings Dataset
- Store Locations Dataset

## Analysis Performed
1. Loaded GPS ping and store location datasets.
2. Calculated distance between GPS coordinates and stores
   using the Haversine formula.
3. Identified the nearest store for each GPS ping.
4. Compared the distance with the store catchment radius.
5. Classified GPS pings as within or outside the catchment.

## Store Activity Summary
The analysis summarizes:
- Total GPS pings near each store
- Pings within the catchment radius
- Pings outside the catchment radius
- Average distance from the nearest store

## Business Benefits
- Understand store-level location activity.
- Compare store catchment performance.
- Support location-based business decisions.
- Identify areas with potential customer movement.

## Output Files
- store_proximity_analysis.csv
- store_activity_summary.csv

## Note
The analysis uses synthetic GPS data and does not
represent actual customer visits or transactions.
