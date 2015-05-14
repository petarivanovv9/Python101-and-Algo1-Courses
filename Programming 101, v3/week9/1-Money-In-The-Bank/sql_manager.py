import sqlite3
from settings import DB_NAME, DB_SQL_STRUCTURE
from Client import Client
import os

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# factory pattern
# dependency injection


class BankDatabaseManager:

    @classmethod
    def create_from_db_and_sql(cls, db_name, structure_file, create_if_exists=False):
        conn = sqlite3.connect(db_name)

        if not os.path.exists(db_name) or create_if_exists:
            cursor = conn.cursor()

            with open(DB_SQL_STRUCTURE, "r") as f:
                cursor.executescript(f.read())

            conn.commit()

            return BankDatabaseManager(conn)

        conn = sqlite3.connect(db_name)
        return BankDatabaseManager(conn)

    def __init__(self, conn):
        pass


def create_clients_table():
    with open(DB_SQL_STRUCTURE, "r") as f:
        cursor.executescript(f.read())


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"

    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    insert_sql = "INSERT INTO clients (username, password) VALUES (?, ?)"
    cursor.execute(insert_sql, (username, password))
    conn.commit()


def login(username, password):
    select_query = """SELECT id, username, balance, message
                    FROM clients
                    WHERE username = ? AND password = ? LIMIT 1"""

    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if (user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
