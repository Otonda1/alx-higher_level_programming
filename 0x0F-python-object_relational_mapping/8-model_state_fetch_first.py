#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State).order_by(State.id).first()
if states is not None:
    print(f"{states.id}: {states.name}")
else:
    print("Nothing")    
session.close()


