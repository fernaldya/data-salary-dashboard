def fetch_data(spark, jdbc_url: str, connection_properties: dict, schema: str, table: str):
    '''
    Fetches data from the given database and store as a variable
    '''
    try:
        source_df = spark.read.jdbc(url=jdbc_url, table=f'{schema}.{table}', properties=connection_properties)
        return source_df
    
    except Exception as e:
        print('Error occured', str(e))
        