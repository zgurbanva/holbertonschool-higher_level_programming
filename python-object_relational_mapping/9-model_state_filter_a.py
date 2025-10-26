#!/usr/bin/python3
"""List all State objects that contain the letter 'a' (sorted by id asc).

Usage:
    ./9-model_state_filter_a.py <mysql_user> <mysql_password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    uri = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, pwd, db)
    engine = create_engine(uri, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        q = session.query(State).filter(State.name.like('%a%')) \
            .order_by(State.id)
        for s in q:
            print("{}: {}".format(s.id, s.name))
    finally:
        session.close()
