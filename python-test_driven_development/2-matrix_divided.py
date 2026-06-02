#!/usr/bin/python3
"""
Module for dividing all elements in a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div and round to 2 decimal places.
    """
    em = "matrix must be a matrix (list of lists) of integers/floats"
    # Store long error message in short variable(pycode)
    if not isinstance(matrix, list):
        raise TypeError(em)
    # If matrix is not a list, raise an error.
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(em)
    # If any row isn't a list, raise the error.
    if not all(isinstance(n, (int, float)) for row in matrix for n in row):
        raise TypeError(em)
    # Nested loop in one line -
    # for every row in matrix, for every n in that row
    # check is n if an integer or float.
    # If any element fails, raise the error
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    # len(row) gives the length of each row
    # set() removes duplicates
    # if all rows are the same length, the set has only 1 value.
    # If len(set(...)) > 1, rows have different sizes,
    # so raise the error.
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Same pattern as with above
    # Checks if div is an integer or float
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # If div is 0, raise the error
    new_matrix = []
    for row in matrix:
        new_row = []
        for n in row:
            new_row.append(round(n / div, 2))
        new_matrix.append(new_row)
    return new_matrix
# Start with an empty new_matrix
# For each row, create empty new_row
# For each element n in the row
# Divide by div, round to 2 decimal places and append to new_row
# After finishing each roe, append new_row to new_matrix
# Return the completed new_matrix
