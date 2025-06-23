{{ config(
    dataset='staging'
    )
}}

select
    CAST(id as INT) as id,
    CAST(country as STRING) as country,
    CAST(city as STRING) as city,
    CAST(name as STRING) as name,
    CAST(company_id as INT) as company_id
from 
    {{ source('staging', 'locations') }} 
