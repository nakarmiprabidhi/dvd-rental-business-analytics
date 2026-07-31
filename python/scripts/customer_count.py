from Python.database.connection import connect_database
from Python.queries.customer_queries import get_customers
from Python.transforms.customer_transform import select_customer_columns
import pandas as pd 

# Start with empty variables
connection = None
cursor = None



try:
    # Connect Python to PostgreSQL
    connection = connect_database()

    print("Successfully connected to PostgreSQL.")

    # Create a cursor so Python can execute SQL
    cursor = connection.cursor()

    # Retrieve customers from PostgreSQL
    results = get_customers(cursor)

    df = pd.DataFrame(
    results,
    columns=[
        "First Name",
        "Last Name",
        "Email",
        "Active",
        "Store"
    ]
     )
    customer_report =select_customer_columns(df)

    print(customer_report)

    customer_report.to_csv(
        "Python/output/customers.csv",
        index=False
    )

    print("CSV file created successfully.")


except Exception as error:
    # This runs if something fails
    print(f"An error occurred: {error}")

finally:
    # Close the cursor if it was created
    if cursor is not None:
        cursor.close()
        print("Cursor closed.")

    # Close the database connection if it was created
    if connection is not None:
        connection.close()
        print("Database connection closed.")

