#!/usr/bin/env python3
import numpy as np
"""
    A function that transposes a matrix
"""
def matrix_transpose(matrix):
    """
    Return the transpose of a 2D matrix.
    """
    return np.array(matrix).T.tolist()
