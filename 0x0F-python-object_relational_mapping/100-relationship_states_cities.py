#!/usr/bin/python3
""" rows using relationship"""
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
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    r_city = City(name="San Francisco")
    r_state = State(name="California", cities=[r_city])
    session.add(r_city)
    session.add(r_state)
    session.commit()
