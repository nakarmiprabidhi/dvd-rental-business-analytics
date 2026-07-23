/*
Project: DVD Rental Business Analytics
File: 01_executive_kpis.sql
Author: Prabidhi

Purpose:
Create executive-level KPIs for the DVD Rental leadership team.

Database:
PostgreSQL DVD Rental sample database
*/


-- =========================================================
-- KPI 01: TOTAL CUSTOMERS
-- Business Question:
-- How many customers are currently stored in the database?
SELECT 
COUNT(*) AS total_customers
FROM customer;

-- Validation:
-- Returned 599 customers.
-- The query produced one aggregate row representing the entire customer table.
-- =========================================================

SELECT
    active,
    COUNT(*) AS total_customers
FROM customer
GROUP BY active
ORDER BY active DESC;

-- Validation:
-- Active Customers: 584
-- Inactive Customers: 15


-- =========================================================
-- KPI 03: CUSTOMERS PER STORE
-- Business Question:
-- How many customers belong to each store?
-- =========================================================

SELECT
    store_id,
    COUNT(*) AS total_customers
FROM customer
GROUP BY store_id
ORDER BY store_id;

-- Validation:
-- Store 1: 326 customers
-- Store 2: 273 customers
