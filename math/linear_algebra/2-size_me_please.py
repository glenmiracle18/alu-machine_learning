#!/usr/bin/env python3
"""
    A function that returns the shape of a matrix.

    Parameters:
    matrix (list): A nested list (matrix) whose shape is to be determined.

    Returns:
    list: A list representing the shape of the matrix, where each element
          corresponds to the size of each dimension.

    Example:
    >>> matrix_shape([[1, 2], [3, 4]])
    [2, 2]
    >>> matrix_shape([[1], [2], [3]])
    [3, 1]
    >>> matrix_shape([])
    []
"""


def matrix_shape(matrix):
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
