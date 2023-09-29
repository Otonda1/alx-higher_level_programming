#!/usr/bin/python3
if __name__ == "__main__":

    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    from sys import argv
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")
    session.close()
