SELECT
    ping_id,
    device_id,

    SAFE_CAST(latitude AS FLOAT64) AS latitude,
    SAFE_CAST(longitude AS FLOAT64) AS longitude,

    SAFE_CAST(timestamp AS TIMESTAMP) AS timestamp,

    activity_area,
    day_of_week,

    SAFE_CAST(hour AS INT64) AS hour,

    daypart,
    movement_mode,

    SAFE_CAST(gps_accuracy_m AS FLOAT64)
        AS gps_accuracy_m,

    is_anonymized,
    nearest_store_id,

    SAFE_CAST(nearest_store_distance_m AS FLOAT64)
        AS nearest_store_distance_m,

    SAFE_CAST(
        within_500m_of_nearest_store AS BOOL
    ) AS within_500m_of_nearest_store

FROM geopluse-515615.geopluse.gps_pings
WHERE
    ping_id IS NOT NULL
    AND device_id IS NOT NULL
    AND timestamp IS NOT NULL;