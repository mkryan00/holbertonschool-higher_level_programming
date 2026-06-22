#!/usr/bin/python3
"""Script to add all arguments to a Python list."""


from sys import argv

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    items = load(filename)
except Exception:
    items = []

items.extend(argv[1:])

save(items, filename)
