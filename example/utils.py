from django.db import connection

def create_table_in_db(table_name):
    # SQL query to create a table with the given table name
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        status TEXT
    );
    """

    # Execute the query
    with connection.cursor() as cursor:
        cursor.execute(query)
