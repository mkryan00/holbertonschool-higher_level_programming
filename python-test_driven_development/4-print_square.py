#!/usr/bin/python3
"""
Module for printing a square with hashtags.
"""


def print_square(size):
    """
    Prints a square using the character #.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        for n in range(size):
            print("#", end="")
        print()
