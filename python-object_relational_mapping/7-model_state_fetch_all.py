#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
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
    datas = session.query(State).order_by(State.id)

    for elem in datas:
        print("{}: {}".format(elem.id, elem.name))

    session.close()