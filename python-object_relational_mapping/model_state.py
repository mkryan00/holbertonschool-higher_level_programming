#!/usr/bin/python3
"""Defines the State class, linked to the MySQL table 'states'."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state, mapped to the states table

    Attributes:
        id (int): The state's unique id, primary key.
        name (str): The state's name, max 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
