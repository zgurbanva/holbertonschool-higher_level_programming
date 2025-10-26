#!/usr/bin/python3
"""List all State objects that contain the letter 'a' (sorted by id asc)."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 3 + 1:
        sys.exit(1)

    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s in session.query(State).filter(State.name.like('%a%')).order_by(State.id):
        print(f"{s.id}: {s.name}")

    session.close()
