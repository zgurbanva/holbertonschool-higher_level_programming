#!/usr/bin/python3
"""List all State objects from hbtn_0e_6_usa using SQLAlchemy.

Usage:
    ./7-model_state_fetch_all.py <mysql_user> <mysql_pwd> <db_name>

Prints lines like: `<id>: <name>` sorted by states.id (ascending).
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to MySQL on localhost:3306 and list all State rows."""
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
        pool_pre_ping=True,
        future=True
    )

    Session = sessionmaker(bind=engine, future=True)
    session = Session()

    try:
        for state in session.query(State).order_by(State.id).all():
            print(f"{state.id}: {state.name}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
