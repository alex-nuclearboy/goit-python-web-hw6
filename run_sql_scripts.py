import sqlite3


def execute_sql(db_path, sql_file_path):
    """
    Executes an SQL script from a given file on the specified SQLite database.

    Parameters:
    - db_path: Path to the SQLite database file.
    - sql_file_path: Path to the .sql file containing the SQL script.
    """

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # Read SQL script from file
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        # Execute SQL script
        cur.execute(sql_script)

        # Fetch and print all results
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print(f"Error executing SQL script: {error}")
    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()


db_path = 'university_database.db'
sql_file_paths = [f'sql_scripts/queries/query_{i}.sql' for i in range(1, 13)]

for i, sql_file_path in enumerate(sql_file_paths, start=1):
    print(f"Executing query number: {i}")
    execute_sql(db_path, sql_file_path)
    print("\n")
