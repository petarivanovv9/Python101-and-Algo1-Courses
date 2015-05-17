import sqlite3
# from settings import DB_NAME, DB_SQL_STRUCTURE
import os


class BankDatabaseManager:

    @classmethod
    def create_from_db_and_sql(cls, db_name, structure_file):
        conn = sqlite3.connect(db_name)

        if not os.path.exists(db_name):
            cursor = conn.cursor()

            with open(structure_file, "r") as f:
                cursor.executescript(f.read())

            conn.commit()

            return BankDatabaseManager(conn)

        conn = sqlite3.connect(db_name)
        return BankDatabaseManager(conn)

    def __init__(self, conn):
        pass
