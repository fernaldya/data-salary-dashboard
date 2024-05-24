import os
import logging
from pyspark.sql import SparkSession
from tasks.fetch_data import fetch_data
from tasks.staging_one import staging_one
from tasks.staging_two import staging_two
from functions.read_conn import load_conn_config


def main() -> None:
    '''
    Main entrypoint for pipeline executor
    '''

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Source JDBC URL and credentials
    src_creds = {
        'user': os.getenv('SOURCE_DB_USER'),
        'password': os.getenv('SOURCE_DB_PASS'),
        'driver': 'org.postgresql.Driver'
    }
    
    src_conn = load_conn_config(filename='src_conn_config.json')['source_database']
    # print(src_conn)
    src_jdbc_url = f'jdbc:postgresql://{src_conn["host"]}:{src_conn["port"]}/{src_conn["database"]}'

    # Target JDBC URL and credentials
    tgt_creds = {
        'user': os.getenv('TARGET_DB_USER'),
        'password': os.getenv('TARGET_DB_PASS'),
        'driver': 'org.postgresql.Driver'
    }
    tgt_conn = load_conn_config(filename='tgt_conn_config.json')['target_database']
    # print(tgt_conn)
    tgt_jdbc_url = f'jdbc:postgresql://{tgt_conn["host"]}:{tgt_conn["port"]}/{tgt_conn["database"]}'


    # Create SparkSession
    spark = SparkSession.builder \
            .appName('Pipeline') \
            .config('spark.jars', '/opt/spark/jars/postgresql-42.2.5.jar') \
            .config('spark.sql.legacy.timeParserPolicy', 'LEGACY') \
            .getOrCreate()
            
    logger.info('Spark Session created')

    try:
        # Fetch data from source table
        source_df = fetch_data(spark=spark, jdbc_url=src_jdbc_url, connection_properties=src_creds,\
                            schema=src_conn['schema'], table=src_conn['table'])
        
        # Move data to staging one table
        staging_one(source_df=source_df, jdbc_url=tgt_jdbc_url, connection_properties=tgt_creds,\
                    schema=tgt_conn['schema'], table=tgt_conn['staging_one_table'])

        # Move from staging one to staging two
        staging_two(spark=spark, jdbc_url=tgt_jdbc_url, connection_properties=tgt_creds,\
                    src_table=f'{tgt_conn["schema"]}.{tgt_conn["staging_one_table"]}',\
                    tgt_table=f'{tgt_conn["schema"]}.{tgt_conn["staging_two_table"]}')
    except Exception as e:
        logger.error('Pipeline exec failed: %s', str(e))

    finally:
        spark.stop()
        logger.info('Spark Session stopped')

if __name__ == '__main__':
    main()
