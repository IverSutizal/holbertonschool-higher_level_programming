#!/usr/bin/python3
"""Lists all State objects that contain the letter a from
   the database hbtn_0e_6_usa.
   Created on Sunday, December 13, 2022
   @author: DaisyG Chipana Lapa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%'))\
                                     .order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()