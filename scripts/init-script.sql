-- CREATE SCHEMA
CREATE SCHEMA IF NOT EXISTS salary_data;

-- CREATE TABLE
CREATE TABLE IF NOT EXISTS salary_data.salaries (
    id SERIAL PRIMARY KEY, 
    work_year TEXT,
    experience_level TEXT,
    employment_type TEXT,
    job_title TEXT,
    salary TEXT,
    salary_currency TEXT,
    salary_in_usd TEXT,
    employee_residence TEXT,
    remote_ratio TEXT,
    company_location TEXT,
    company_size TEXT
);