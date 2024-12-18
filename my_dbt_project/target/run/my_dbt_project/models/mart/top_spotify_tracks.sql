
  
    
    

    create  table
      "my_database"."main"."top_spotify_tracks__dbt_tmp"
  
    as (
      

with 

spotify_tracks as (

    select *
    from "my_database"."main"."stg_spotify_tracks"
    limit 5

)

select *
from spotify_tracks
    );
  
  