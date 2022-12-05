#!/usr/bin/python3
"""lists one State objects from the database hbtn_0e_6_usa """
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
    check = session.query(State.id, State.name).first()
    if check:
        print("{}: {}".format(check.id, check.name))
    else:
        print("Nothing")
