{{ config(materialized='table') }}

with 

spotify_tracks as (

    select *
    from {{ref("stg_spotify_tracks")}}
    limit 5

)

select *
from spotify_tracks
