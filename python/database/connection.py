import psycopg2
from dotenv import dotenv_values


def connect_database():
    config = dotenv_values("Python/config/database.env")

    connection = psycopg2.connect(
        host=config["DB_HOST"],
        port=config["DB_PORT"],
        database=config["DB_NAME"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"]
    )

    return connection