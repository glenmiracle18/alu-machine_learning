#!/usr/bin/env python3
"""
concatenate two matrices along a certain axis
"""
def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.
        axis (int): The axis along which to concatenate.

    Returns:
        list: A new matrix resulting from the concatenation,
              or None if concatenation is not possible.
    """


    if not mat1 or not mat2:
        return None

    # Base case: matrices are 1D
    if not isinstance(mat1[0], list):
        if axis == 0:
            return mat1 + mat2
        elif axis == 1:
            return [list(row) for row in zip(mat1, mat2)]
        else:
            return None

    # Recursive case: matrices are multidimensional
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis > 0:
        if len(mat1) != len(mat2):
            return None
        result = []
        for i in range(len(mat1)):
            concatenated = cat_matrices(mat1[i], mat2[i], axis - 1)
            if concatenated is None:
                return None
            result.append(concatenated)
        return result
    else:
        return None

def matrix_shape(matrix):
    """Helper function to get the shape of a matrix."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
