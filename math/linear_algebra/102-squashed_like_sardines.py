#!/usr/bin/env python3

"""
This module provides a function to concatenate two matrices
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenate two matrices along a specified axis.

    Args:
    mat1 (list): First input matrix (list of lists).
    mat2 (list): Second input matrix (list of lists).
    axis (int): Axis along which to concatenate

    Returns:
    list: A new matrix resulting from the concatenation
    """
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    if axis not in [0, 1]:
        return None

    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row.copy() for row in mat1] + [row.copy() for row in mat2]
    else:  # axis == 1
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
