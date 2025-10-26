#!/usr/bin/python3
"""Print the first State object (by id) from hbtn_0e_6_usa using SQLAlchemy.

This script connects to a local MySQL server and prints the first row from the
`states` table as `<id>: <name>` ordered by `states.id`. If the table is
empty, it prints `Nothing`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to MySQL and print the first State ordered by id."""
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine_url = (
        f"mysql+mysqldb://{user}:{password}@localhost/{db_name}"
    )
    engine = create_engine(engine_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State).order_by(State.id.asc()).first()
        if state is None:
            print("Nothing")
        else:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
