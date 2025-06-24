{{ config(
    dataset='marts'
    )
}}

with hired_candidate as (
    select 
        *
    from 
        {{ ref("int_hired_candidate") }}
),

jobs as (
    select 
        *
    from 
        {{ ref("int_jobs") }}
)

select
    j.id as job_id,
    j.title as job_title,
    j.status as job_status,
    j.created_at as job_created_at,
    j.department_name as department_name,
    j.location_country as job_country,
    j.company_name as company_name,

    -- Candidate Hired Date
    h.candidate_id as candidate_id,
    h.timestamp as hired_at,

    -- Metrics 
    DATETIME_DIFF(h.timestamp, j.created_at, day) as time_to_hire

from
    jobs j
left join
    hired_candidate h
    ON j.id = h.job_id