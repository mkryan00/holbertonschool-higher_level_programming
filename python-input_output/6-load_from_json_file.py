#!/usr/bin/python3
"""Module that creates an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
