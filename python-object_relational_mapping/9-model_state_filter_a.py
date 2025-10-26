#!/usr/bin/python3
"""List all State objects containing the letter 'a' using SQLAlchemy.

This script connects to a local MySQL server and prints each matching row from
the `states` table as `<id>: <name>`, ordered by `states.id` in ascending
order.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to MySQL and list State rows whose names contain 'a'."""
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine_url = (
        f"mysql+mysqldb://{user}:{password}@localhost/{db_name}"
    )
    engine = create_engine(engine_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        q = session.query(State).filter(State.name.like("%a%")) \
            .order_by(State.id.asc())
        for state in q:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
