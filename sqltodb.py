import sqlite3

def create_database(sql_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(sql_file, 'r') as sql_script:
        sql_commands = sql_script.read()
        cursor.executescript(sql_commands)

    conn.commit()
    conn.close()

# Specify the SQL file and database file paths
sql_file = 'Database before_norm/Used_Vehicle.sql'
db_file = 'vehicles_used.db'

create_database(sql_file, db_file)

