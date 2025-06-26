{{ config(
    dataset='intermediate'
    )
}}

select 
    j.id,
    j.title,
    j.status,
    j.company_id,
    j.created_at,
    j.department_id,
    j.requisition_id,
    j.location_id,

    -- Location Dimension
    coalesce(l.country, 'unknown') as location_country,
    coalesce(l.city, 'unknwn') as location_city,

    -- Department Dimension
    coalesce(d.name, 'unknown') as department_name,

    -- Company Dimension
    coalesce(c.name, 'unknown') as company_name,

from 
    {{ ref("stg_jobs") }} as j

left join
    {{ ref("stg_locations") }} as l
    ON j.location_id = l.id

left join
    {{ ref("stg_departments") }} as d
    ON j.department_id = d.id 

left join
    {{ ref("stg_companies") }} as c
    ON j.company_id = c.id

