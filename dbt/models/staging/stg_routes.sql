SELECT
    route_id,
    agency_id,
    route_short_name,
    route_long_name,
    route_type,
    CASE route_type
        WHEN 100 THEN 'Railway'
        WHEN 101 THEN 'High Speed Rail'
        WHEN 103 THEN 'Inter Regional Rail'
        WHEN 105 THEN 'Sleeper Rail'
        WHEN 106 THEN 'Regional Rail'
        WHEN 401 THEN 'Metro'
        WHEN 700 THEN 'Bus'
        WHEN 714 THEN 'Rail Replacement Bus'
        WHEN 900 THEN 'Tram'
        WHEN 1000 THEN 'Water Transport'
        WHEN 1501 THEN 'Communal Taxi'
        ELSE 'Unknown (' || route_type::TEXT || ')'
    END AS route_type_name,
    route_desc
FROM {{ source('raw', 'routes') }}
