#!/usr/bin/python3
"""cript that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    Base.metadata.create_all(engine)

    change_state = session.query(State).filter(State.id == 2).first()
    change_state.name = "New Mexico"

    session.commit()
    session.close()