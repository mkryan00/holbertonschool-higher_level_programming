#!/usr/bin/python3
"""
Module for printing fisrt and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.
    Both names must be a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # If first_name isn't a string, raise the error.
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # If last_name isn't a string, raise the error.
    print("My name is {} {}".format(first_name, last_name))
