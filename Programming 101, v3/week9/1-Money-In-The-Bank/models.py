from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


from base import Base


class Client(Base):
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float)
    message = Column(String)
    email = Column(String)


class BlockedClient(Base):
    __tablename__ = "BlockedClients"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey(Client.id))
    client_date = Column(DateTime)
    # relationship
