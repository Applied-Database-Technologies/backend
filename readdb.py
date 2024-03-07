
import sqlite3
conn = sqlite3.connect('used_vehicles.db')
cursor = conn.cursor()

 # Execute a query to fetch data from the table
cursor.execute(f"SELECT * FROM used_vehicles")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

    # Close connection
conn.close()