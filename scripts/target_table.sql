-- CREATE SCHEMA
CREATE SCHEMA IF NOT EXISTS salary_data;

-- CREATE TABLE
CREATE TABLE IF NOT EXISTS salary_data.salaries (
    id SERIAL,
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