import sqlite3
from settings import DB_NAME, SQL_FILE
from Client import Client

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def create_clients_table():
    cursor.execute(SQL_FILE)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?", (
        new_message, logged_user.get_id())

    cursor.execute(update_sql)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?", (
        new_pass, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()


def register(username, password):
    insert_sql = "INSERT INTO clients (username, password) VALUES (?, ?)", (
        username, password)
    cursor.execute(insert_sql)
    conn.commit()


def login(username, password):
    select_query = """SELECT id, username, balance, message
                    FROM clients
                    WHERE username = ? AND password = ? LIMIT 1""", (
        username, password)

    cursor.execute(select_query)
    user = cursor.fetchone()

    if (user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
