#!/usr/bin/python3
"""
List all State objects that contain the letter 'a' from the database.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password> <db_name>

The output is sorted by states.id ascending and printed as:
<id>: <name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Entrypoint for filtering states containing 'a'."""
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    uri = f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}"
    engine = create_engine(uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        q = (session.query(State)
             .filter(State.name.ilike('%a%'))
             .order_by(State.id.asc()))

        for s in q:
            print(f"{s.id}: {s.name}")
    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    main()
