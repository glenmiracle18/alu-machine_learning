#!/usr/bin/env python3
"""
    Numpy Elementwise
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.
    
    Args:
    mat1, mat2: numpy.ndarray inputs
    
    Returns:
    A tuple containing the element-wise sum, difference, product, and quotient.
    """
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return (add, sub, mul, div)
