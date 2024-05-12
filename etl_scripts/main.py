import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv
from tasks.fetch_data import fetch_data
from tasks.staging_one import staging_one
from tasks.staging_two import staging_two


def main() -> None:
    '''
    Main entrypoint for pipeline executor
    '''
    load_dotenv()

    # Source JDBC URL and credentials
    src_creds = {
        'user': os.getenv('SOURCE_USER'),
        'password': os.getenv('SOURCE_PASSWORD'),
        'driver': 'org.postgresql.Driver'
    }
    src_conn = {
        'host': os.getenv('SOURCE_HOST'),
        'port': os.getenv('SOURCE_PORT'),
        'db': os.getenv('SOURCE_DB'),
        'schema': os.getenv('SOURCE_SCHEMA'),
        'table': os.getenv('SOURCE_TABLE')
    }
    src_jdbc_url = f'jdbc:postgresql://{src_conn["host"]}:{src_conn["port"]}/{src_conn["db"]}'

    # Target JDBC URL and credentials
    tgt_creds = {
        'user': os.getenv('TARGET_USER'),
        'password': os.getenv('TARGET_PASSWORD'),
        'driver': 'org.postgresql.Driver'
    }
    tgt_conn = {
        'host': os.getenv('TARGET_HOST'),
        'port': os.getenv('TARGET_PORT'),
        'db': os.getenv('TARGET_DB'),
        'schema': os.getenv('TARGET_SCHEMA'),
        'sgone_table': os.getenv('SGONE_TABLE'),
        'sgtwo_table': os.getenv('SGTWO_TABLE')

    }
    tgt_jdbc_url = f'jdbc:postgresql://{tgt_conn["host"]}:{tgt_conn["port"]}/{tgt_conn["db"]}'


    # Create SparkSession
    spark = SparkSession.builder.appName("Pipeline").getOrCreate()

    # Fetch data from source table
    source_df = fetch_data(spark=spark, jdbc_url=src_jdbc_url, connection_properties=src_creds,\
                           schema=src_conn['schema'], table=src_conn['table'])

    # Move data to staging one table
    staging_one(source_df=source_df, jdbc_url=tgt_jdbc_url, connection_properties=tgt_creds,\
                schema=tgt_conn['schema'], table=tgt_conn['sgone_table'])

    # Move from staging one to staging two
    staging_two(spark=spark, jdbc_url=tgt_jdbc_url, connection_properties=tgt_creds,\
                src_table=f'{tgt_conn["schema"]}.{tgt_conn["sgone_table"]}',\
                tgt_table=f'{tgt_conn["schema"]}.{tgt_conn["sgtwo_table"]}')


if __name__ == '__main__':
    main()
