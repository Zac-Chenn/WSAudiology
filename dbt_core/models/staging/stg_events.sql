{{ config(
    dataset='staging'
    )
}}

select
    CAST(id as INT) as id,
    CAST(job_id as INT) as job_id,
    CAST(job_title as STRING) as job_title,
    CAST(user_id as INT) as user_id,
    CAST(stage_id as INT) as stage_id,
    CAST(timestamp as DATETIME) as timestamp,
    CAST(company_id as INT) as company_id,
    CAST(event_type as STRING) as event_type,
    CAST(candidate_id as STRING) as candidate_id
from
    {{ source('staging', 'events') }}