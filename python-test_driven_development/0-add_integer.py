#!/usr/bin/python3
"""
A module to add two numbers
This module performs the addition operation between two numbers,
these numbers can be integers or floats.
"""


def add_integer(a, b=98):
    """Adds two numbers
    Returns the addition of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
