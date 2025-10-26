#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage: ./13-model_state_delete_a.py <mysql_user> <mysql_password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connects via SQLAlchemy ORM, deletes matching State rows, and commits."""
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        to_delete = session.query(State).filter(State.name.like('%a%')).all()
        for obj in to_delete:
            session.delete(obj)
        session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    main()
