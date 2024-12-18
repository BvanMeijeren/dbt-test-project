import pandas as pd
import duckdb

# Connect to the DuckDB database file
conn = duckdb.connect('my_database.db')

# Query the data and load it directly into a Pandas DataFrame
df = conn.execute("SELECT * FROM main.stg_spotify_tracks LIMIT 5").fetchdf()

# Display the first 5 rows from the DataFrame
print("Sample Data from spotify_tracks:")
print(df)

