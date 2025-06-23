{{ config(
    dataset='staging'
    )
}}

select
    CAST(id as INT) as id,
    CAST(job_title as STRING) as job_title,
    CAST(user_id as INT) as user_id,
    CAST(currency as STRING) as currency,
    CAST(company_id as INT) as company_id,
    CAST(created_at as DATETIME) as created_at,
    CAST(archived_at as DATETIME) as archived_at,
    CAST(archive_reason as STRING) as archive_reason,
    CAST(location_id as INT) as location_id,
    CAST(recruiter_id as INT) as recruiter_id,
    CAST(department_id as INT) as department_id,
    CAST(number_of_openings as INT) as number_of_openings,
    CAST(requisition_status as STRING) as requisition_status,
    JSON_VALUE(custom_form_answers, '$.type_of_position') as type_of_position
from
    {{ source('staging', 'requisitions') }}