SELECT
    service_id,
    TO_DATE(date::TEXT, 'YYYYMMDD') AS date,
    exception_type,
    CASE exception_type
        WHEN 1 THEN 'service added'
        WHEN 2 THEN 'service removed'
    END AS exception_type_name
FROM {{ source('raw', 'calendar_dates') }}
