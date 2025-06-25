import os
import csv
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def connect_to_postgres():
    """
    Establishes a connection to a PostgreSQL database using psycopg2,
    with credentials loaded from environment variables.

    Returns:
        psycopg2.extensions.connection: A psycopg2 connection object,
                                          or None if the connection fails.
    """
    # Get the credentials from environment variables.
    host = os.environ.get("POSTGRES_HOST")
    port = os.environ.get("POSTGRES_PORT", "5432")
    database = os.environ.get("POSTGRES_DB")
    user = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")

    if None in (host, database, user, password):
        print("Error: Required environment variables are not set.")
        print(
            "Please set POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, and POSTGRES_PASSWORD."
        )
        return None

    try:
        # Establish the connection using psycopg2.connect()
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )
        return conn

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return False


if __name__ == "__main__":
    conn = connect_to_postgres()

    with conn.cursor() as cursor:
        query = """
            SELECT * 
            FROM pg_catalog.pg_tables
            WHERE schemaname = 'public';
        """
        cursor.execute(query)
        table_names_tuple = cursor.fetchall()

        for i, table_name in enumerate(table_names_tuple):
            table_name = table_name[1]
            print(f"Beginning Process: Creating {table_name}.csv")
            select_query = f"SELECT * FROM {table_name}"
            cursor.execute(select_query)
            table_data = cursor.fetchall()

            with open(
                f"data/recruitment_data/{table_name}.csv", "w", newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow([col[0] for col in cursor.description])
                writer.writerows(table_data)

            print(f"{table_name}.csv has been created")

        print("Table downloads has been completed")

    # close the cursor and connection
    cursor.close()
    conn.close()
