#!/usr/bin/python3
"""lists all city objects from the database hbtn_0e_6_usa
"""
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )
    session = sessionmaker(bind=engine)()
    for c_id, c_name, s_name in session.query(City.id, City.name, State.name).join(State).order_by(City.id):
        print("{}: ({}) {}".format(s_name, c_id, c_name))
