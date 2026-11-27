\# GeoPulse – Project Methodology



\## 1. Introduction



GeoPulse is a hyper-local retail mobility analytics project that uses synthetic GPS ping data and store location information to analyze customer movement, retail footfall, store proximity and catchment areas.



The project follows a Python-based analytical workflow to evaluate existing retail locations and a potential candidate location.



\## 2. Input Data



The project uses two raw datasets:



\### GPS Pings Dataset

`GeoPulse\_500\_Synthetic\_GPS\_Pings.csv`



Contains GPS ping identifiers, anonymized device IDs, geographic coordinates, timestamps, activity areas, movement modes and nearest-store proximity information.



\### Store Locations Dataset

`GeoPulse\_Store\_Locations.csv`



Contains store IDs, names, location coordinates, store status and catchment radius.



\## 3. Technology Stack



\- Python

\- Pandas

\- GeoPandas

\- GeoJSON

\- Kepler.gl

\- Git and GitHub



\## 4. Analytical Workflow



\### Step 1: GPS Data Summary



Script: `generate\_gps\_summary.py`



Generates summary information about GPS records, unique devices, activity areas and daypart distribution.



\### Step 2: GPS Data Validation



Script: `validate\_gps\_data.py`



Performs data quality checks on the GPS input dataset.



\### Step 3: Footfall Analysis



Script: `analyze\_footfall.py`



Analyzes GPS activity across different geographic areas and time periods.



\### Step 4: Daypart Comparison



Script: `compare\_daypart\_footfall.py`



Compares morning rush and evening rush footfall patterns.



\### Step 5: Store Proximity Analysis



Script: `analyze\_store\_proximity.py`



Calculates store-level footfall records, unique devices, average distance and GPS pings within 500 metres.



\### Step 6: Catchment Polygon Generation



Script: `create\_catchment\_polygons.py`



Generates geographical catchment polygons using store locations and the defined catchment radius.



\### Step 7: Catchment Validation



Script: `validate\_catchments.py`



Checks catchment geometry validity and radius-related quality measures.



\### Step 8: Store Proximity Quality Validation



Script: `validate\_store\_proximity.py`



Checks required fields, duplicate store IDs, footfall counts, unique device counts, 500m proximity counts, percentage calculations and distance values.



\## 5. Visualization



Kepler.gl is used to explore geographical patterns and visualize footfall and catchment information.



The project includes an embedded map and a footfall visualization screenshot in the repository.



\## 6. Key Analytical Findings



\- Total GPS records: 500.

\- Unique devices: 118.

\- GPS records within 500 metres: 333.

\- Overall 500m coverage: 66.6%.

\- Cyber Hub has the highest activity area record count.

\- Evening Rush has the highest daypart footfall.

\- Golf Course Road Candidate has the highest store-level 500m proximity percentage among the three analyzed locations.



\## 7. Quality Assurance



The project includes GPS validation, catchment validation and store proximity validation.



All eight implemented store proximity quality checks passed successfully.



All three catchment geometries passed the reported geometry and radius validity checks.



\## 8. Business Application



The analytical results can support:



\- Retail location assessment.

\- Store catchment evaluation.

\- Footfall-based planning.

\- Customer proximity analysis.

\- Identification of potential retail opportunities.



\## 9. Limitations



\- The project uses synthetic GPS data.

\- Device identifiers are anonymized.

\- Footfall counts do not directly represent actual customer visits or sales.

\- Candidate store performance requires real-world validation.

\- Business investment decisions should use additional commercial and customer data.



\## 10. Conclusion



GeoPulse combines GPS data processing, spatial analysis, data validation and visualization to evaluate retail mobility patterns.



The workflow provides a structured foundation for comparing existing stores and assessing potential retail locations using geospatial analytics.

