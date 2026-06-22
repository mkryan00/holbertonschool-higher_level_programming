#!/usr/bin/python3
"""Function to return dictionary for JSON serialization"""


def class_to_json(obj):
    return obj.__dict__
