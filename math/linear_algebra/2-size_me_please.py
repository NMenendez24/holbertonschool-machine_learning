#!/usr/bin/env python3
"""Shebang"""

def matrix_shape(matrix):
    """Returns the shape of the matrix"""
    shape = []
    while (isinstance(matrix, list)):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
