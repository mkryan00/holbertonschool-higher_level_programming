#!/usr/bin/python3
"""
module for printing text and new lines
"""


def text_indentation(text):
    """
    whenever the users text has certain symbols
    it will finish the line with them,
    and start up again after a newline betweeete
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Checks if text is a string, if not raise TypeError.
    edit = False
    # A flag to track whether we just printed a '.', '?' or ':'.
    # Starts as False - we haven't printed anything yet.
    for char in text:
        # Loop to iterate through each character at a time.
        if char not in '.?:' and not (edit and char == ' '):
            # Is this character NOT a special character?
            # Are we NOT in a situation where we just printed
            # a special character AND this character is a space?
            # "No spaces at the beginning of a line" rule.
            print("{}".format(char), end="")
            # Print current character with no newline character.
            # Characters stay on the same line until a special character.
            edit = False
            # After printing a normal chracter, reset the flag.
            # No longer at the start of a new line, so don't skip next space.
        else:
            if char in '.?:':
                # Check for special character.
                # If there is a space, then ignore it and skip.
                print("{}".format(char), end="\n\n")
                # Print the special character followed by two newlines
                edit = True
                # On next iteration, skip leading space on the new line.
