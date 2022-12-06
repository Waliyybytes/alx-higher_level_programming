#!/usr/bin/python3
""" Declaring State Model """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """ state class """
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
