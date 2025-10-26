#!/usr/bin/python3
"""
Prints all City objects from hbtn_0e_14_usa in the format:
<state name>: (<city id>) <city name>
Sorted by cities.id ascending.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """
    Connects to MySQL via SQLAlchemy and prints cities joined with states,
    ordered by City.id ascending, using ORM only (no raw execute).
    """
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Join City -> State and order strictly by cities.id
        rows = (session.query(City, State)
                .join(State, City.state_id == State.id)
                .order_by(City.id.asc())
                .all())
        for city, state in rows:
            print(f"{state.name}: ({city.id}) {city.name}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
