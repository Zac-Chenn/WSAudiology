{{ config(
    dataset='intermediate'
    )
}}

select 
    job_id,
    job_title,
    timestamp,
    event_type,
    candidate_id

from 
    {{ ref("stg_events") }}

where
    event_type = 'hired'

