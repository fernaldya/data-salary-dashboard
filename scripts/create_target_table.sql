-- CREATE SCHEMA
CREATE SCHEMA IF NOT EXISTS salary_data;

-- CREATE STAGING TABLE 1
CREATE TABLE IF NOT EXISTS salary_data.staging_one (
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

-- CREATE STAGING TABLE 2
CREATE TABLE IF NOT EXISTS salary_data.staging_two (
    id SERIAL PRIMARY KEY,
    work_year INT,
    experience_level VARCHAR(3),
    employment_type VARCHAR(3),
    job_title TEXT,
    salary DECIMAL(20, 3),
    salary_currency VARCHAR(3) DEFAULT 'USD',
    salary_in_usd DECIMAL(20, 3),
    employee_residence VARCHAR(3),
    remote_ratio SMALLINT,
    company_location VARCHAR(3),
    company_size VARCHAR(3)
);