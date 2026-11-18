
# GeoPulse Dashboard Data Dictionary

## 1. GPS Ping Dataset

| Column | Description |
|---|---|
| ping_id | Unique GPS ping identifier |
| device_id | Anonymized device identifier |
| latitude | GPS latitude |
| longitude | GPS longitude |
| timestamp | Date and time of GPS ping |
| activity_area | Area associated with GPS activity |
| day_of_week | Day of the week |
| hour | Hour of GPS activity |
| daypart | Time category |
| movement_mode | Movement category |
| gps_accuracy_m | GPS accuracy in metres |
| is_anonymized | Anonymization indicator |
| nearest_store_id | Nearest store identifier |
| nearest_store_distance_m | Distance from nearest store |
| within_500m_of_nearest_store | Proximity indicator |

## 2. Store Locations Dataset

| Column | Description |
|---|---|
| store_id | Store identifier |
| store_name | Store name |
| store_status | Store operational status |
| latitude | Store latitude |
| longitude | Store longitude |
| catchment_radius_m | Store catchment radius in metres |

## 3. Dashboard Usage

GPS dataset:
- KPI cards
- Hourly activity charts
- Daypart analysis
- Movement mode analysis
- Location analysis

Store dataset:
- Store comparison
- Store status
- Store location map
- Catchment analysis

## Note
Column definitions must be checked against the
actual CSV files before building the dashboard.
