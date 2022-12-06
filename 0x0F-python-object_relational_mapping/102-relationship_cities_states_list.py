#!/usr/bin/python3
"""list all cities"""
from relationship_state import Base, State
from relationship_city import City
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
    cities_objs = session.query(City).order_by(City.id)
    for c in cities_objs:
        print("{}: {} -> {}".format(c.id, c.name, c.state.name))
