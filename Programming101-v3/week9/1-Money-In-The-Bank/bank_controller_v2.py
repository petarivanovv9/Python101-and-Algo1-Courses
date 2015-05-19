from models import Client
from base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import re
import hashlib


class BankController:

    def __init__(self, db_connection_string):
        self.__engine = create_engine(db_connection_string)
        Base.metdata.create_all(self.__engine)

        self.__session = Session(bind=self.__engine)

    def __commit_changes(self, objects):
        self.__session.add_all(objects)
        self.__session.commit()

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
        # try:
        #     if BankDatabaseManager.validate_password(username, password):
        #         hashed_password = BankDatabaseManager.hash_password(password)
        #         self.cursor.execute("""INSERT INTO Clients
        #             (client_username, client_password)
        #             VALUES (?, ?)""", (username, hashed_password))
        #         self.conn.commit()
        #         return True
        #     else:
        #         return False
        # except:
        #     return False
        pass
