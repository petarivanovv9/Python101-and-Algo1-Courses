from models import Client
from base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class BankController:

    def __init__(self, db_connection_string):
        self.__engine = create_engine(db_connection_string)
        Base.metdata.create_all(self.__engine)

        self.__session = Session(bind=self.__engine)

    def __commit_changes(self, objects):
        self.__session.add_all(objects)
        self.__session.commit()
