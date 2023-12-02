import sqlite3


def read_query_from_file(file_path):
    # Read the SQL query from the provided file
    with open(file_path, "r", encoding="utf-8") as file:  # Specifying the encoding
        return file.read()


def execute_query(database_path, query):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute(query)

    # Fetch and return the results
    results = cursor.fetchall()
    conn.close()
    return results


def main():
    database_path = "travel_insurance.db"  # Update with your actual database path
    query_file_path = "query.sql"  # Path to your SQL query file

    # Read the query from the SQL file
    sql_query = read_query_from_file(query_file_path)

    # Execute the query and get results
    results = execute_query(database_path, sql_query)

    # Print the results
    for row in results:
        print(row)


if __name__ == "__main__":
    main()
