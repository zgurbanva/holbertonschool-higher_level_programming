#!/usr/bin/python3
"""
Defines the City ORM model linked to the 'cities' table.
The City class inherits from Base that is imported from model_state.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City ORM class mapped to the 'cities' table.

    Attributes:
        id (int): Auto-generated primary key, cannot be null.
        name (str): City name (max 128 chars), cannot be null.
        state_id (int): FK referencing states.id, cannot be null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
