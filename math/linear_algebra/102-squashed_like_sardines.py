#!/usr/bin/env python3
def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.
        axis (int): The axis along which to concatenate (0 or 1).

    Returns:
        list: A new matrix resulting from the concatenation,
              or None if concatenation is not possible.
    """
    # Check if matrices are empty
    if not mat1 or not mat2:
        return None

    # Handle 1D matrices
    if not isinstance(mat1[0], list):
        if axis == 0:
            return mat1 + mat2
        elif axis == 1:
            return [list(row) for row in zip(mat1, mat2)]
        else:
            return None

    # Handle 2D matrices
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
