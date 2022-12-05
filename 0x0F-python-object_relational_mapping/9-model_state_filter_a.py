#!/usr/bin/python3
"""lists State objects from the database hbtn_0e_6_usa that contains a"""
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
    for c_id, c_name in session.query(
            State.id, State.name).order_by(
                    State.id).filter(
                            State.name.contains('a')):
        print("{}: {}".format(c_id, c_name))
