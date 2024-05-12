# staging_two.py


def staging_two(spark, jdbc_url: str, connection_properties: dict, src_table: str, tgt_table: str) -> None:
    '''
    Fetches data from the first staging table and writes into the second staging table
    '''
    try:
        staging_one_df = spark.read.jdbc(url=jdbc_url, table=src_table, properties=connection_properties)
        print('Read success')
              
    except Exception as e:
        print('Read error', str(e))
     
    try:        
        # Write DataFrame to staging two table
        staging_one_df.write.jdbc(url=jdbc_url, table=tgt_table, mode='overwrite', properties=connection_properties)
        print('Write success')
    
    except Exception as e:
        print('Write error', str(e))
        