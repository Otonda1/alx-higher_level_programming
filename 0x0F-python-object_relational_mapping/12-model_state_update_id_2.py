#!/usr/bin/python3
"""
Changes State object whose id=2 to
New Mexico
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

    match = 2
    result = session.query(State).filter_by(id=match).first()
    if result is not None:
        result.name = "New Mexico"
        session.add(result)
        session.commit()
