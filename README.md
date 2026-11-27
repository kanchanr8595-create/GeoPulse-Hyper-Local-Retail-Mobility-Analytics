\# GeoPulse – Hyper-Local Retail Mobility Analytics



\## Project Overview



GeoPulse is a geospatial retail analytics project designed to analyze anonymized GPS foot traffic, store catchment areas, visitor proximity and potential retail expansion opportunities.



The project uses synthetic GPS mobility data to understand customer movement patterns and evaluate potential store locations.



\## Project Objectives



\- Analyze GPS-based footfall patterns.

\- Identify high-activity retail areas.

\- Compare morning and evening footfall.

\- Evaluate customer proximity to existing and candidate stores.

\- Generate 500-metre store catchment areas.

\- Identify potential retail expansion opportunities.



\## Technology Stack



\- Python

\- Pandas

\- GeoPandas

\- GeoJSON

\- Kepler.gl

\- Git and GitHub



\## Project Workflow



1\. Load GPS ping and store location datasets.

2\. Validate GPS records and catchment inputs.

3\. Generate GPS summary reports.

4\. Analyze footfall by activity area and daypart.

5\. Calculate store proximity and 500m coverage.

6\. Generate store catchment polygons.

7\. Visualize geographical patterns using Kepler.gl.

8\. Perform data quality checks.

9\. Prepare business insights and recommendations.



\## Key Analysis Results



| Metric | Result |

|---|---:|

| GPS Records | 500 |

| Unique Devices | 118 |

| Records Within 500m | 333 |

| Overall 500m Coverage | 66.6% |

| Highest Activity Area | Cyber Hub |

| Highest Footfall Daypart | Evening Rush |



\## Store Proximity Findings



| Store | Footfall Records | 500m Coverage |

|---|---:|---:|

| Cyber Hub Coffee | 214 | 60.28% |

| Sector 29 Coffee | 185 | 60.00% |

| Golf Course Road Candidate | 101 | 92.08% |



Golf Course Road Candidate demonstrates promising proximity coverage in the analyzed synthetic dataset.



\## Data Quality



The project includes validation checks for:



\- GPS data quality

\- Catchment geometry validity

\- Store proximity metrics

\- Duplicate store IDs

\- Footfall counts

\- 500m proximity percentages



All eight implemented store proximity quality checks passed.



\## Repository Structure



```text

GeoPulse-Hyper-Local-Retail-Mobility-Analytics/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── scripts/

│   ├── analyze\_footfall.py

│   ├── analyze\_store\_proximity.py

│   ├── compare\_daypart\_footfall.py

│   ├── create\_catchment\_polygons.py

│   ├── generate\_gps\_summary.py

│   ├── validate\_catchments.py

│   ├── validate\_gps\_data.py

│   └── validate\_store\_proximity.py

│

├── documentation/

│

├── README.md

└── kepler.gl embedded map.html

```



\## Business Recommendations



\- Evaluate Golf Course Road as a potential retail expansion location.

\- Focus on customer engagement during evening rush hours.

\- Continue monitoring high-activity areas such as Cyber Hub and Sector 29.

\- Investigate areas with low 500m proximity coverage.

\- Validate findings with real-world sales and customer data before investment decisions.



\## Conclusion



GeoPulse demonstrates how geospatial analytics and GPS mobility data can support retail location planning, customer footfall analysis and catchment evaluation.



\*\*Note:\*\* This project uses synthetic GPS data. The findings are analytical indicators and do not represent confirmed real-world customer behavior or store profitability.

