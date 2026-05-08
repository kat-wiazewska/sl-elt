SELECT
    service_id,
    monday,
    tuesday,
    wednesday,
    thursday,
    friday,
    saturday,
    sunday,
    TO_DATE(start_date::TEXT, 'YYYYMMDD') AS start_date,
    TO_DATE(end_date::TEXT, 'YYYYMMDD') AS end_date
FROM
    {{ source('raw', 'calendar') }}
