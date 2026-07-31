import psycopg2
from dotenv import dotenv_values


# Read database settings from database.env
config = dotenv_values("Python/config/database.env")

# Start with empty variables
connection = None
cursor = None

try:
    # Connect Python to PostgreSQL
    connection = psycopg2.connect(
        host=config["DB_HOST"],
        port=config["DB_PORT"],
        database=config["DB_NAME"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"]
    )

    print("Successfully connected to PostgreSQL.")

    # Create a cursor so Python can execute SQL
    cursor = connection.cursor()

    # Run the SQL query
    cursor.execute("""
        SELECT
        first_name,
        last_name,
        email
    FROM customer
    LIMIT 5;
    """)

    # Retrieve all result rows
    results = cursor.fetchall()
# Print each returned row
    for row in results:
     print(row)

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

