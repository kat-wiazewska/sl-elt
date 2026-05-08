SELECT
    route_id,
    service_id,
    trip_id,
    trip_headsign,
    trip_short_name,
    direction_id,
    CASE direction_id
        WHEN 0 THEN 'Outbound'
        WHEN 1 THEN 'Inbound'
    END AS direction_id_name,
    shape_id,
    samtrafiken_internal_trip_number
FROM {{ source('raw', 'trips')}}
