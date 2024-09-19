#!/usr/bin/env python3
"""
    A function that calculates the minor of a matrix
"""


def minor(matrix):
    """
    Returns the minor matrix of a matrix
    """

    # checks the type of the matrix if is matrix
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a list of lists")

    # checks if it is a square matrix
    n = len(matrix)  # the number of items in the matrix

    if n == 1:  # Add this check for 1x1 matrix
        return [[0]]  # Return a matrix with 0 for 1x1 case

    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    def determinant(mat):
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for j in range(len(mat)):
            submatrix = [row[:j] + row[j+1:] for row in mat[1:]]
            det += ((-1) ** j) * mat[0][j] * determinant(submatrix)
        return det

    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            submatrix = [
                row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])
            ]
            minor_row.append(determinant(submatrix))
        minor_matrix.append(minor_row)

    return minor_matrix
