\# GeoPulse – Final Business Insights and Recommendations



\## 1. Project Overview



GeoPulse is a hyper-local retail mobility analytics project that evaluates customer movement, store proximity, footfall patterns and potential retail locations using synthetic GPS data.



The analysis uses 500 GPS records and 118 unique devices.



\## 2. Overall GPS Insights



\- Total GPS records: 500

\- Unique devices: 118

\- Records within 500 metres: 333

\- Overall 500m coverage: 66.6%



The results provide an overview of customer movement and proximity to retail locations.



\## 3. Activity Area Analysis



| Activity Area | Records | 500m Coverage |

|---|---:|---:|

| Cyber Hub | 133 | 96.99% |

| Sector 29 | 118 | 94.07% |

| Golf Course Road | 101 | 92.08% |

| Residential | 76 | 0% |

| Office District | 72 | 0% |



\### Key Findings



\- Cyber Hub has the highest activity with 133 GPS records.

\- Sector 29 also shows strong activity with 118 records.

\- Golf Course Road has 101 records and high proximity coverage.

\- Residential and Office District records have zero pings within the defined 500m proximity metric.



\## 4. Daypart Footfall Analysis



| Daypart | Footfall Records | Coverage |

|---|---:|---:|

| Evening Rush | 151 | 66.23% |

| Morning Rush | 112 | 66.96% |

| Midday | 88 | 65.91% |

| Early Morning | 77 | 68.83% |

| Night | 72 | 65.28% |



\### Key Findings



\- Evening Rush records the highest footfall with 151 records.

\- Morning Rush follows with 112 records.

\- Early Morning has the highest coverage percentage at 68.83%.

\- Evening Rush represents an important period for retail activity planning.



\## 5. Store Proximity Analysis



| Store | Status | Footfall | 500m Coverage |

|---|---|---:|---:|

| Cyber Hub Coffee | Existing | 214 | 60.28% |

| Sector 29 Coffee | Existing | 185 | 60.00% |

| Golf Course Road Candidate | Candidate | 101 | 92.08% |



\### Key Findings



\- Cyber Hub Coffee has the highest assigned footfall among the three locations.

\- Sector 29 Coffee records 185 footfall records.

\- Golf Course Road Candidate has the highest 500m proximity percentage at 92.08%.

\- The candidate location shows promising proximity characteristics based on the available GPS data.



\## 6. Catchment Quality Review



All three store catchment geometries passed the geometry validation checks.



\- Geometry validity: True for all three locations.

\- Radius validity: True for all three locations.

\- Catchment radius: Approximately 500 metres.

\- Catchment area: Approximately 0.784 square kilometres per location.



This confirms that the generated catchment areas passed the implemented spatial quality checks.



\## 7. Business Recommendations



1\. Prioritize further retail opportunity assessment in Golf Course Road because of its high 500m proximity percentage.

2\. Continue monitoring customer activity around Cyber Hub because it has the highest recorded activity and assigned store footfall.

3\. Consider additional promotional campaigns during Evening Rush.

4\. Investigate Residential and Office District areas to understand their low 500m proximity coverage.

5\. Use catchment maps to support future retail location planning.



\## 8. Conclusion



The GeoPulse analysis identifies Cyber Hub as the highest-activity area and Evening Rush as the busiest daypart.



Golf Course Road Candidate demonstrates strong proximity coverage compared with the existing stores.



All three catchment geometries passed the implemented quality checks.



These findings provide a data-driven starting point for retail location assessment and customer movement analysis. Further validation using real-world customer and sales data is recommended before making final investment decisions.



\## 9. Supporting Project Reports



\- GeoPulse\_Footfall\_Analysis.csv

\- GeoPulse\_Daypart\_Comparison.csv

\- GeoPulse\_Store\_Proximity\_Analysis.csv

\- GeoPulse\_GPS\_Summary\_Report.csv

\- GeoPulse\_Catchment\_Quality\_Report.csv

