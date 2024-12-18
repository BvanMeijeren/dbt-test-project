
import duckdb

# Connect to a DuckDB database file
conn = duckdb.connect('my_database.db')

# Specify the CSV file path
csv_file = 'my_dbt_project/data/spotify_tracks.csv'

# Create a table and load the CSV data into it
conn.execute(f"""
    CREATE TABLE main.spotify_tracks AS
    SELECT * FROM read_csv_auto('{csv_file}');
""")

# Verify that the data has been loaded by querying the table
result = conn.execute("SELECT * FROM main.spotify_tracks LIMIT 5;").fetchall()
print("Sample Data from spotify_tracks:")
for row in result:
    print(row)

# Optional: Check the schema of the table
schema = conn.execute("DESCRIBE spotify_tracks;").fetchall()
print("\nSchema of spotify_tracks:")
for column in schema:
    print(column)

