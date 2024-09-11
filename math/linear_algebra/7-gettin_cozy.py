#!/usr/bin/env python3
"""
    A function that concatenates a 2d matix
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Return the concatenation of two 2D matrices.
    """
    if axis == 0:
        return mat1 + mat2
    elif axis == 1:
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
