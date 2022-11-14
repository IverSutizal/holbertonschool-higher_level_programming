#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa
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

    datas = session.query(State).first()
    if datas:
        print("{}: {}".format(datas.id, datas.name))
    else:
        print("Nothing")
    session.close()