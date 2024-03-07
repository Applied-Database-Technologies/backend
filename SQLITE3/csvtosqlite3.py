
import pandas as pd
import sqlite3

def csv_to_sqlite(csv_file, sqlite_file, table_name):
    # Read CSV file into pandas DataFrame
    df = pd.read_csv(csv_file)

    # Connect to SQLite database
    conn = sqlite3.connect(sqlite_file)

    # Write DataFrame to SQLite database
    df[:1000].to_sql(table_name, conn, if_exists='replace', index=False)

    # Close connection
    conn.close()


csv_file = 'data/vehicles.csv'
sqlite_file = 'used_vehicles.db'
table_name = 'used_vehicles'
csv_to_sqlite(csv_file, sqlite_file, table_name)
