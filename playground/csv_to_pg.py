import psycopg2
import sqlalchemy
import os
import duckdb
import pandas as pd
import glob
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def initiate_engine():
    """
    Establishes a connection to a PostgreSQL database using credentials from
    environment variables.  Handles potential connection errors.
    """
    # Get the credentials from environment variables.
    host = os.environ.get("LOCAL_PG_HOST")
    port = os.environ.get("LOCAL_PG_PORT")
    database = os.environ.get("LOCAL_PG_DB")
    user = os.environ.get("LOCAL_PG_USER")
    password = os.environ.get("LOCAL_PG_PASSWORD")

    engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    return engine


if __name__ == "__main__":
    folder_path = "data/recruitment_data" 
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    csv_file = 'data/recruitment_data/answers.csv'
    engine = initiate_engine()

    if not csv_files:
        print(f"No CSV files found in the folder: {folder_path}")
        exit()

    for csv_file in csv_files:
        table_name = os.path.splitext(os.path.basename(csv_file))[0]

        # Create & Insert CSV into PostgreSQL
        print(f"Begin process for creating {table_name} table")
        df = pd.read_csv(csv_file)
        df.to_sql(name=table_name, con=engine, if_exists='replace')
        print(f"Table {table_name} has been created")






        


