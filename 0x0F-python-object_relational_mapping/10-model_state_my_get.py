#!/usr/bin/python3
"""
List all State objects' id from hbtn_0e_6_usa
whose name matches that passed as an argument
"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    match = sys.argv[4]
    result = session.query(State).filter_by(name=match).first()
    if result is not None:
        print("{}".format(result.id))
    else:
        print("Not found")
