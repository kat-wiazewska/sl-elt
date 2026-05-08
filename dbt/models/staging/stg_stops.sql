SELECT
    stop_id,
    stop_name,
    stop_lat,
    stop_lon,
    location_type,
    CASE location_type
        WHEN 0 THEN 'Stop/platform'
        WHEN 1 THEN 'Station (parent)'
        WHEN 2 THEN 'Entrance/exit'
    END AS location_type_name,
    parent_station,
    platform_code
FROM {{ source('raw', 'stops') }}
