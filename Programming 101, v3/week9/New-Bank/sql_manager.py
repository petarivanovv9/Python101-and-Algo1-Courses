import sqlite3
import os
import re
import hashlib
from Client import Client
import datetime
from settings import BLOCK_FOR_N_MINUTES, PASSWORD_MIN_LENGTH


class BankDatabaseManager:

    @staticmethod
    def create_from_db_and_sql(db_name, create_tables, drop_database, create_if_exists=False):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        if not os.path.exists(db_name) or create_if_exists:

            with open(drop_database, "r") as f:
                cursor.executescript(f.read())
                conn.commit()

        with open(create_tables, "r") as f:
            cursor.executescript(f.read())
            conn.commit()

        return BankDatabaseManager(conn)

    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    @staticmethod
    def validate_password(username, password):
        are_there_digits = re.search(r'\d+', password)
        are_there_uppercase_letter = re.search(r'[A-Z]+', password)
        enough_length = len(password) >= PASSWORD_MIN_LENGTH
        are_there_symbols = re.search('[\-\/\@\?\!\,\.\#\&\*]+', password)

        if are_there_digits and are_there_uppercase_letter and enough_length and are_there_symbols and username not in password:
            return True
        else:
            return False

    @staticmethod
    def hash_password(password):
        hash_pass = hashlib.sha1(password.encode())
        hex_dig = hash_pass.hexdigest()

        return hex_dig

    def register(self, username, password):
        try:
            if BankDatabaseManager.validate_password(username, password):
                hashed_password = BankDatabaseManager.hash_password(password)
                self.cursor.execute("""INSERT INTO Clients
                    (client_username, client_password)
                    VALUES (?, ?)""", (username, hashed_password))
                self.conn.commit()
                return True
            else:
                return False
        except:
                return False

    def login(self, username, password):
        get_user_query = """SELECT client_id,
                                client_username,
                                client_balance,
                                client_message,
                                client_email
        FROM Clients
        WHERE client_username = ? AND client_password = ?
        LIMIT 1"""

        hashed_password = self.hash_password(password)

        self.cursor.execute(get_user_query, (username, hashed_password))
        user = self.cursor.fetchone()

        if user:
            return Client(user[0], user[1], user[2], user[3], user[4])
        else:
            False

    def is_user_registered(self):
        pass

    def add_blocked_user(self, username):
        self.cursor.execute("""SELECT client_id FROM Clients
            WHERE client_username = ?""", (username, ))
        cleint_id = self.cursor.fetchone()[0]
        blocked_on_date = datetime.datetime.now()

        self.cursor.execute("""INSERT INTO Blocked_Users
        (blocked_client_id, blocked_client_date)
        VALUES (?, ?)""", (cleint_id, blocked_on_date))
        self.conn.commit()

    def get_blocked_users(self):
        return self.cursor.execute("""SELECT client_username FROM Clients
            INNER JOIN Blocked_Users
            ON Clients.client_id = Blocked_Users.blocked_client_id""")

    def update_blocked_users(self):
        time = datetime.datetime.now() - datetime.timedelta(minutes=BLOCK_FOR_N_MINUTES)
        self.cursor.execute("""DELETE FROM Blocked_Users
            WHERE blocked_client_date <= ? """, (time, ))
        self.conn.commit()


# Bam123@Bam
