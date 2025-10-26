#!/usr/bin/python3
"""
Prints all City objects from hbtn_0e_14_usa as:
<state name>: (<city id>) <city name>

Usage:
    ./14-model_city_fetch_by_state.py <mysql_user> <mysql_password> <database>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Connects to MySQL via SQLAlchemy ORM and prints cities joined to states."""
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost/{db}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Join City -> State; order by City.id ascending
        q = (
            session.query(City, State)
            .join(State, City.state_id == State.id)
            .order_by(City.id.asc())
        )
        for city, state in q:
            print(f"{state.name}: ({city.id}) {city.name}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
