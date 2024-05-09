#!/bin/bash

# Variables
HOST="localhost"
PORT="5432"
USER="postgres"
DB="salary"
SCHEMA="salary_data"
TABLE="salaries"
FILE="/psql_data/salaries.csv"

# Data insertion
psql -h $HOST -p $PORT -U $USER -d $DB <<-EOSQL
    -- Copy data from csv to table
    COPY $SCHEMA.$TABLE FROM $FILE CSV HEADER;
EOSQL
