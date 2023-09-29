#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import create_engine

    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter_by(name=argv[4]).first()
    if states is not None:
        print(str(states.id))
    else:
        print("Not found")
    session.close()
