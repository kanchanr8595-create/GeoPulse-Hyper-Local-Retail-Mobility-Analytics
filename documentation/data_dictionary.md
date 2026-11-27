\# GeoPulse Data Dictionary



\## 1. Overview



This document describes the raw datasets used in the GeoPulse Hyper-Local Retail Mobility Analytics project.



The project uses two synthetic datasets:



1\. GeoPulse\_500\_Synthetic\_GPS\_Pings.csv

2\. GeoPulse\_Store\_Locations.csv



These datasets support GPS movement analysis, footfall analysis, store proximity calculations and catchment area generation.



\## 2. GPS Pings Dataset



\*\*File:\*\* `GeoPulse\_500\_Synthetic\_GPS\_Pings.csv`



\*\*Description:\*\* Contains anonymized synthetic GPS activity records representing device movement across different retail areas.



| Column | Description |

|---|---|

| ping\_id | Unique identifier for each GPS ping |

| device\_id | Anonymized device identifier |

| latitude | Geographic latitude of the GPS ping |

| longitude | Geographic longitude of the GPS ping |

| timestamp | Date and time of the GPS record |

| activity\_area | Geographic area associated with the ping |

| day\_of\_week | Day of the week |

| hour | Hour of recorded activity |

| daypart | Time-based activity category |

| movement\_mode | Recorded movement mode |

| gps\_accuracy\_m | GPS accuracy in metres |

| is\_anonymized | Indicates whether the device record is anonymized |

| nearest\_store\_id | Identifier of the nearest store |

| nearest\_store\_distance\_m | Distance to the nearest store in metres |

| within\_500m\_of\_nearest\_store | Indicates whether the GPS ping is within 500 metres of the nearest store |



\### Important Fields



\- `ping\_id`: Used to identify individual GPS records.

\- `device\_id`: Used to calculate unique device counts.

\- `timestamp`: Supports time-based activity analysis.

\- `activity\_area`: Supports geographic footfall comparisons.

\- `nearest\_store\_distance\_m`: Supports store proximity analysis.



\## 3. Store Locations Dataset



\*\*File:\*\* `GeoPulse\_Store\_Locations.csv`



\*\*Description:\*\* Contains geographical information about existing stores and a candidate retail location.



| Column | Description |

|---|---|

| store\_id | Unique identifier for each store |

| store\_name | Name of the store or candidate location |

| store\_status | Indicates existing or candidate status |

| latitude | Store latitude |

| longitude | Store longitude |

| catchment\_radius\_m | Store catchment radius in metres |



\### Store Categories



| Store ID | Store Name | Status |

|---|---|---|

| STORE\_A | Cyber Hub Coffee | Existing |

| STORE\_C | Sector 29 Coffee | Existing |

| CANDIDATE\_B | Golf Course Road Candidate | Candidate |



All three locations have a defined catchment radius of 500 metres.



\## 4. Processed Datasets and Reports



| File | Purpose |

|---|---|

| GeoPulse\_GPS\_Summary\_Report.csv | Summarizes GPS records and device activity |

| GeoPulse\_Footfall\_Analysis.csv | Analyzes footfall by activity area and daypart |

| GeoPulse\_Daypart\_Comparison.csv | Compares morning and evening footfall |

| GeoPulse\_Store\_Proximity\_Analysis.csv | Summarizes store-level proximity metrics |

| GeoPulse\_Catchment\_Quality\_Report.csv | Reports catchment geometry and radius validation |

| GeoPulse\_Proximity\_Quality\_Report.csv | Reports store proximity data quality checks |



\## 5. Data Usage



The raw GPS dataset is used for:



\- Footfall analysis

\- Unique device analysis

\- Daypart comparisons

\- Geographic activity analysis

\- Store proximity calculations



The store locations dataset is used for:



\- Store-level analysis

\- Catchment polygon generation

\- Existing and candidate location comparisons

\- Retail location assessment



\## 6. Data Limitations



\- The datasets contain synthetic GPS records.

\- Device identifiers are anonymized.

\- The analysis does not represent confirmed real-world customer behaviour.

\- Business decisions should be validated using real-world sales and customer data.



\## 7. Conclusion



This data dictionary provides a reference for understanding the raw GPS and store location datasets used throughout the GeoPulse project.



It supports consistent interpretation of source fields and processed analytical reports.

