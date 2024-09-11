#!/usr/bin/env python3
"""
    Slicing of matrices along an axis
"""
import numpy as np



def np_slice(matrix, axes={}):
    """
    Slices a numpy.ndarray along specified axes.
    
    Args:
    matrix: A numpy.ndarray to be sliced
    axes: A dictionary where the key is an axis to slice along and the value
          is a tuple representing the slice to make along that axis
    
    Returns:
    A new numpy.ndarray with the specified slices applied
    """
    slices = [slice(None)] * matrix.ndim
    for axis, slice_info in axes.items():
        slices[axis] = slice(*slice_info)
    return matrix[tuple(slices)]
