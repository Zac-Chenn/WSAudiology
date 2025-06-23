{{ config(
    dataset='staging'
    )
}}

select
    CAST(id as INT) as id,
    CAST(name as STRING) as name
from
    {{ source('staging', 'company') }}