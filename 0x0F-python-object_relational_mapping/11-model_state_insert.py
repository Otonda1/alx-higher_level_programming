#!/usr/bin/python3
if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    loui = State(id=6, name='Louisiana')
    session.add(loui)
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.commit()
    session.close()
