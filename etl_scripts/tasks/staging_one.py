# staging_one.py
from pyspark.sql.functions import current_timestamp

def staging_one(source_df, jdbc_url: str, connection_properties: dict, schema: str, table: str) -> None: 
    '''
    Writes the source data into the first staging table
    '''

    source_df = source_df.withColumn('ts_processed', current_timestamp())
    try:
        # Write DataFrame to staging one table
        source_df.write.jdbc(url=jdbc_url, table=f'{schema}.{table}', mode='overwrite', properties=connection_properties)
        print('Write success')
    
    except Exception as e:
        print('Error occured', str(e))
        