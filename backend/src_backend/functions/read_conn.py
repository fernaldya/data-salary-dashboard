import json


def load_conn_config(filename: str) -> dict:
    '''
    Reads a json file (Filled with the config of the database, schema, table) 
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config

    except Exception as e:
        print('Error occurred ', str(e))
