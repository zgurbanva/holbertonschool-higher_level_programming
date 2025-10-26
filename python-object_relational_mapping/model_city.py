#!/usr/bin/python3
"""
Defines the City model, linked to State via a foreign key.

This module imports `Base` (and may reference `State`) from `model_state`
but does not execute any code on import. It maps to the `cities` table with
columns `id`, `name`, and `state_id` (FK to states.id).
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    ORM model for the `cities` table.

    Attributes:
        id (int): Primary key, auto-incremented.
        name (str): Non-nullable city name.
        state_id (int): Non-nullable FK referencing states.id.
        state (State): ORM relationship to the parent State.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship is optional for these tasks but harmless and convenient
    state = relationship("State")
