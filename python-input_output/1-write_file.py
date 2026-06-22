#!/usr/bin/python3
"""Function that writes a string to a text file
and returns number of characters.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
