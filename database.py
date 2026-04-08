import os
from dotenv import load_dotenv
import mysql.connector

# Load variables from .env
load_dotenv()


def get_database():
    database_vm = mysql.connector.connect(
        host=os.getenv("DB_VM_IP"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return database_vm


def check_cache(query):
    connect_db_vm = get_database()
    cursor = connect_db_vm.cursor()

    cursor.execute("SELECT result FROM cache WHERE query = %s", (query,))
    row = cursor.fetchone()

    connect_db_vm.close()

    if row:
        return row[0]
    return None


def save_cache(query, result):
    connect_db_vm = get_database()
    cursor = connect_db_vm.cursor()

    cursor.execute(
        "INSERT INTO cache (query, result) VALUES (%s, %s)",
        (query, result)
    )

    connect_db_vm.commit()
    connect_db_vm.close()