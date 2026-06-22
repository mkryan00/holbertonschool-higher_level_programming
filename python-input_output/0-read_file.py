#!/usr/bin/python3
"""Module that defines the read_file function."""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout.
    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename) as f:
        print(f.read())
