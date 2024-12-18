
  
    
    

    create  table
      "my_database"."main"."stg_spotify_tracks__dbt_tmp"
  
    as (
      

with source_data as (

    select *
    from main.spotify_tracks 

)

select *
from spotify_tracks
    );
  
  