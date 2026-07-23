# Project Journal

## Day 1 — Project Initialization and First Executive KPI

### Work Completed

- Created the DVD Rental Analytics project structure.
- Created the project README.
- Documented the initial business requirements.
- Created the executive KPI SQL file.
- Developed the total customer KPI.
- Validated the SQL result in PostgreSQL.

### Concepts Practiced

- PostgreSQL
- SQL aggregate functions
- COUNT()
- SQL aliases
- Business requirement interpretation
- Git project organization
- Technical documentation

### Business Insight

The database contains 599 registered customers.

### Challenges

Document any errors, incorrect predictions, or syntax issues encountered today.

### Next Steps

- Calculate active and inactive customers.
- Calculate customers per store.
- Add additional executive KPIs.

## Day 2 - Executive Dashboard KPIs

### Business Tickets Completed

- DA-001 - Total Customers
- DA-002 - Active vs Inactive Customers
- DA-003 - Customers Per Store

### SQL Concepts Used

- COUNT()
- GROUP BY
- ORDER BY
- Aggregate Functions

### Business Insights

- Total Customers: 599
- Active Customers: 584
- Inactive Customers: 15
- Store 1 Customers: 326
- Store 2 Customers: 273

### Lessons Learned

- Validate data before assuming a column represents the business meaning.
- `activebool` and `active` are different columns with different purposes.
- Use `ORDER BY` to produce consistent report output.

## Day 3 - Rental Duration KPIs

### Business Tickets

- DA-004 - Longest configured rental duration
- DA-005 - Shortest configured rental duration

### Concepts Practiced

- MAX()
- MIN()
- Single-value aggregate queries
- Distinguishing configured duration from actual rental behavior

### Business Insights

- Longest configured rental duration: [7 days]
- Shortest configured rental duration: [3 days]

### Key Lesson

The `film.rental_duration` column represents the rental period established for each film. It is different from the actual time a customer kept a rental, which must be calculated from `rental.return_date - rental.rental_date`.

s


