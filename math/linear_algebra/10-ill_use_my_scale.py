#!/usr/bin/env python3
import numpy as np
"""
    A function that calculates the shape of a matrix
"""


def np_shape(matrix):
    """
    Return the shape of a numpy matrix.
    """
    np_matrix = np.array(matrix)
    return np_matrix.shape
