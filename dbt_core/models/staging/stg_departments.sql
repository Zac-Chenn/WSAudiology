{{ config(
    dataset='staging'
    )
}}

select
    CAST(id as INT) as id,
    CAST(name as STRING) as name,
    CAST(company_id as INT) as company_id
from
    {{ source('staging', 'departments') }}