#!/usr/bin/python3
"""Delete all State objects whose name contains the letter 'a'.

Usage:
    ./13-model_state_delete_a.py <mysql_user> <mysql_password> <database>
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
        (session.query(State)
               .filter(State.name.like('%a%'))
               .delete(synchronize_session=False))
        session.commit()
    finally:
        session.close()
