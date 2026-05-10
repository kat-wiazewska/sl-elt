SELECT
    trip_id,
    arrival_time,
    departure_time,
    stop_id,
    stop_sequence,
    stop_headsign,

    pickup_type,
    CASE pickup_type
        WHEN 0 THEN 'Regularly scheduled pickup'
        WHEN 1 THEN 'No pickup available'
        WHEN 2 THEN 'Must phone agency'
        WHEN 3 THEN 'Must coordinate with driver'
    END AS pickup_type_name,

    drop_off_type,
    CASE drop_off_type
        WHEN 0 THEN 'Regularly scheduled drop off'
        WHEN 1 THEN 'No drop off available'
        WHEN 2 THEN 'Must phone agency'
        WHEN 3 THEN 'Must coordinate with driver'
    END AS drop_off_type_name,
    shape_dist_traveled,
    timepoint,

    CASE timepoint
        WHEN 0 THEN 'Approximate'
        WHEN 1 THEN 'Exact'
    END AS timepoint_name,

    pickup_booking_rule_id,
    drop_off_booking_rule_id

FROM {{ source('raw', 'stop_times') }}
