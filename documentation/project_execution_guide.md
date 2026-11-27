\# GeoPulse – Project Execution Guide



\## 1. Overview



This guide explains how to execute the eight Python scripts in the GeoPulse Hyper-Local Retail Mobility Analytics project.



The scripts process synthetic GPS data, analyze retail footfall, evaluate store proximity, generate catchment polygons and perform data quality checks.



\## 2. Input Datasets



The project uses two input files:



\- `data/raw/GeoPulse\_500\_Synthetic\_GPS\_Pings.csv`

\- `data/raw/GeoPulse\_Store\_Locations.csv`



\## 3. Prerequisites



\- Python installed.

\- Required Python libraries installed: Pandas, GeoPandas and Shapely.

\- Project dependencies available in the active Python environment.

\- Run commands from the project root directory.



\## 4. Script Execution Order



Run the following commands one at a time from the project root directory.



\### Step 1: Validate GPS Data



```powershell

python scripts/validate\_gps\_data.py

```



Checks required columns, missing values, duplicate ping IDs, coordinates, GPS accuracy, anonymization and store distances.



\### Step 2: Generate GPS Summary



```powershell

python scripts/generate\_gps\_summary.py

```



Output: `data/processed/GeoPulse\_GPS\_Summary\_Report.csv`



\### Step 3: Analyze Footfall



```powershell

python scripts/analyze\_footfall.py

```



Output: `data/processed/GeoPulse\_Footfall\_Analysis.csv`



Analyzes activity areas and dayparts using footfall records, unique devices and 500m coverage.



\### Step 4: Compare Dayparts



```powershell

python scripts/compare\_daypart\_footfall.py

```



Input: `GeoPulse\_Footfall\_Analysis.csv`



Output: `data/processed/GeoPulse\_Daypart\_Comparison.csv`



Compares Morning Rush and Evening Rush.



\### Step 5: Analyze Store Proximity



```powershell

python scripts/analyze\_store\_proximity.py

```



Output: `data/processed/GeoPulse\_Store\_Proximity\_Analysis.csv`



Calculates store-level footfall, unique devices, average distance and 500m coverage.



\### Step 6: Validate Store Proximity



```powershell

python scripts/validate\_store\_proximity.py

```



Input: `GeoPulse\_Store\_Proximity\_Analysis.csv`



Output: `data/processed/GeoPulse\_Proximity\_Quality\_Report.csv`



Performs eight quality checks on the store proximity report.



\### Step 7: Generate Catchment Polygons



```powershell

python scripts/create\_catchment\_polygons.py

```



Input: `GeoPulse\_Store\_Locations.csv`



Output: `data/processed/GeoPulse\_Catchment\_Polygons.geojson`



Creates 500-metre catchment polygons using GeoPandas and Shapely.



\### Step 8: Validate Catchments



```powershell

python scripts/validate\_catchments.py

```



Input: `GeoPulse\_Catchment\_Polygons.geojson`



Output: `data/processed/GeoPulse\_Catchment\_Quality\_Report.csv`



Checks expected stores, geometry validity and catchment radius.



\## 5. Generated Reports



The execution workflow generates:



1\. `GeoPulse\_GPS\_Summary\_Report.csv`

2\. `GeoPulse\_Footfall\_Analysis.csv`

3\. `GeoPulse\_Daypart\_Comparison.csv`

4\. `GeoPulse\_Store\_Proximity\_Analysis.csv`

5\. `GeoPulse\_Proximity\_Quality\_Report.csv`

6\. `GeoPulse\_Catchment\_Polygons.geojson`

7\. `GeoPulse\_Catchment\_Quality\_Report.csv`



The GPS validation script prints its checks in the terminal and does not generate a separate report file.



\## 6. Expected Validation Results



Previously recorded project results include:



\- 500 GPS records.

\- 118 unique devices.

\- 333 records within 500 metres.

\- All eight implemented store proximity quality checks passed.

\- All three catchment geometries passed the reported geometry and radius checks.



These are existing recorded results. Running the scripts again will perform fresh checks on the current input data.



\## 7. Important Notes



\- Execute scripts from the project root directory.

\- Run dependent scripts after their input files have been generated.

\- The GPS validation script prints check values but does not itself stop execution for every failed check.

\- The project uses synthetic GPS data.

\- Results should not be treated as confirmed real-world customer behavior or store profitability.



\## 8. Conclusion



This execution guide provides a repeatable workflow for running the GeoPulse analysis scripts and generating the project's analytical and validation outputs.

