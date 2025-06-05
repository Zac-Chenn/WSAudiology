{{ config(
    dataset='intermediate'
    )
}}

select 
    *
from 
    {{ source('staging', 'jobs') }}
limit 
    100