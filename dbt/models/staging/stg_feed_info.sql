SELECT
    feed_id,
    feed_publisher_name,
    feed_publisher_url,
    feed_lang,
    feed_version
FROM {{ source('raw', 'feed_info') }}
