def get_customers(cursor):
    cursor.execute("""
        SELECT
            first_name,
            last_name,
            email, 
            activebool,
            store_id
        FROM customer
        LIMIT 20;
    """)

    customer = cursor.fetchall()

    return customer
