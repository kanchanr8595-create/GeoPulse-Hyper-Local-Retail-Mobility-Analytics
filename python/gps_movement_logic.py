
import math

# Earth's approximate radius in meters
EARTH_RADIUS = 6371000


def validate_coordinates(latitude, longitude):
    """Check whether GPS coordinates are valid."""
    if not -90 <= latitude <= 90:
        raise ValueError("Invalid latitude")

    if not -180 <= longitude <= 180:
        raise ValueError("Invalid longitude")

    return True


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two GPS points in meters."""

    validate_coordinates(lat1, lon1)
    validate_coordinates(lat2, lon2)

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return EARTH_RADIUS * c


def calculate_next_position(
    latitude,
    longitude,
    speed_kmph,
    heading,
    interval_seconds
):
    """Calculate the next GPS position using speed and direction."""

    validate_coordinates(latitude, longitude)

    if speed_kmph < 0 or interval_seconds < 0:
        raise ValueError("Speed and interval cannot be negative")

    distance = (speed_kmph * 1000 / 3600) * interval_seconds

    angular_distance = distance / EARTH_RADIUS
    bearing = math.radians(heading % 360)

    lat1 = math.radians(latitude)
    lon1 = math.radians(longitude)

    lat2 = math.asin(
        math.sin(lat1) * math.cos(angular_distance)
        + math.cos(lat1) * math.sin(angular_distance)
        * math.cos(bearing)
    )

    lon2 = lon1 + math.atan2(
        math.sin(bearing) * math.sin(angular_distance)
        * math.cos(lat1),
        math.cos(angular_distance)
        - math.sin(lat1) * math.sin(lat2)
    )

    return math.degrees(lat2), math.degrees(lon2)
