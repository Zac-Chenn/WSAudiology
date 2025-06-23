{{ config(
    dataset='staging'
    )
}}

select 
    CAST(j.id as INT) as id,
    CAST(j.title as STRING) as title,
    CAST(j.status as STRING) as status,
    CAST(j.role_id as INT) as role_id,
    CAST(j.user_id as INT) as user_id,
    CAST(j.company_id as INT) as company_id,
    CAST(j.created_at as DATETIME) as created_at,
    CAST(j.internal as STRING) as internal_job,
    CAST(j.department_id as INT) as department_id,
    CAST(j.internal_name as STRING) as internal_title,
    CAST(j.requisition_id as INT) as requisition_id,
    -- Keep the original for debugging/auditing if needed
    CAST(j.location_ids AS STRING) AS original_location_ids_json,
    CAST(location_id_str AS INT) AS location_id
from 
    {{ source('staging', 'jobs') }} as j,
    -- JSON_QUERY_ARRAY = returns a BigQuery ARRAY<JSON> data type
    -- UNNEST = flatten array into set of rows
    UNNEST(JSON_QUERY_ARRAY(j.location_ids, '$')) AS location_id_str


