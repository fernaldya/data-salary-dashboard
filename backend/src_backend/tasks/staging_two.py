# staging_two.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, monotonically_increasing_id


def staging_two(spark: SparkSession, jdbc_url: str, connection_properties: dict, src_table: str, tgt_table: str) -> None:
    '''
    Fetches data from the first staging table and writes into the second staging table
    '''
    try:
        staging_one_df = spark.read.jdbc(url=jdbc_url, table=src_table, properties=connection_properties)
        print('Read success')
          
        # Write DataFrame to staging two table
        staging_one_df = staging_one_df \
                        .withColumn('id', monotonically_increasing_id()) \
                        .withColumn('work_year', staging_one_df['work_year'].cast('INTEGER')) \
                        .withColumn('salary', staging_one_df['salary'].cast('DECIMAL(20, 3)')) \
                        .withColumn('salary_in_usd', staging_one_df['salary_in_usd'].cast('DECIMAL(20, 3)')) \
                        .withColumn('remote_ratio', staging_one_df['remote_ratio'].cast('SMALLINT')) \
                        .withColumn('ts_processed', current_timestamp())
        staging_one_df.write.jdbc(url=jdbc_url, table=tgt_table, mode='append', properties=connection_properties)
        print('Write success')
    
    except Exception as e:
        print('Write error', str(e))
        