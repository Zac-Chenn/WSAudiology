{{ config(
    dataset='staging'
    )
}}

select 
    *
from 
    {{ source('staging', 'jobs') }}
limit 
    100

