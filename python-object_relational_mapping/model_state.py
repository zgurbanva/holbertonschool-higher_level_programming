#!/usr/bin/python3
"""SQLAlchemy model for the `states` table.

Defines the Base declarative class and the State ORM model with `id` and `name`
columns, to be used with a MySQL database via mysqlclient (MySQLdb).
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Base class for all ORM models in this project
Base = declarative_base()


class State(Base):
    """ORM model for a U.S. state stored in the `states` table."""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Return a string representation helpful for debugging."""
        return f"<State id={self.id!r} name={self.name!r}>"
