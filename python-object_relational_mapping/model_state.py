#!/usr/bin/python3
"""
Defines the Base class and the State model for the ORM tasks.

This module exposes SQLAlchemy's declarative Base as `Base` and a `State`
class mapped to the `states` table with columns `id` (PK) and `name`.
No code is executed on import; it only provides model definitions.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """
    ORM model for the `states` table.

    Attributes:
        id (int): Primary key, auto-incremented.
        name (str): Non-nullable name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
