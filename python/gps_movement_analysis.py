
import pandas as pd
from gps_movement_logic import calculate_distance


def analyze_device_movement(gps_data):

    gps_data["timestamp"] = pd.to_datetime(
        gps_data["timestamp"],
        errors="coerce"
    )

    gps_data = gps_data.dropna(
        subset=["device_id", "latitude", "longitude", "timestamp"]
    )

    gps_data = gps_data.sort_values(
        ["device_id", "timestamp"]
    ).copy()

    gps_data["previous_latitude"] = (
        gps_data.groupby("device_id")["latitude"].shift(1)
    )

    gps_data["previous_longitude"] = (
        gps_data.groupby("device_id")["longitude"].shift(1)
    )

    gps_data["distance_km"] = gps_data.apply(
        lambda row: calculate_distance(
            row["previous_latitude"],
            row["previous_longitude"],
            row["latitude"],
            row["longitude"]
        )
        if pd.notna(row["previous_latitude"])
        else 0,
        axis=1
    )

    gps_data["time_difference_hours"] = (
        gps_data.groupby("device_id")["timestamp"]
        .diff()
        .dt.total_seconds() / 3600
    )

    gps_data["speed_kmph"] = (
        gps_data["distance_km"] /
        gps_data["time_difference_hours"]
    )

    return gps_data


if __name__ == "__main__":

    gps = pd.read_csv(
        "../data/raw/GeoPulse_500_Synthetic_GPS_Pings.csv"
    )

    result = analyze_device_movement(gps)

    print(result[
        ["device_id", "timestamp", "distance_km", "speed_kmph"]
    ].head(10))
