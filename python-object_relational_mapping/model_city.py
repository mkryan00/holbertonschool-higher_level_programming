#!/usr/bin/python3
"""This module defines the city class."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """This class represents the cities table.

    Attributes:
        id (int): The city's unique id, primary key.
        name (str): The city's name, max 128 characters.
        state_id (int): Foreign key referencing the state's id.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
