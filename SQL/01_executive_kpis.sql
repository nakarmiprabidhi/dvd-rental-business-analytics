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


-- =========================================================
-- KPI 04: LONGEST CONFIGURED RENTAL DURATION
-- Business Question:
-- What is the longest rental period offered for any film?
-- =========================================================

SELECT
    MAX(rental_duration) AS longest_rental_duration
FROM film;

-- Validation:
-- Returned one row representing the longest configured rental duration.
-- Result: 7 days.


-- =========================================================
-- KPI 05: SHORTEST CONFIGURED RENTAL DURATION
-- Business Question:
-- What is the shortest rental period offered for any film?
-- =========================================================

SELECT
    MIN(rental_duration) AS shortest_rental_duration
FROM film;

Validation:
-- Returned one row representing the shortest configured rental duration.
-- Result: 3 days



