#!/usr/bin/env python3
"""Shebang"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two matrices by axis"""
    new_matrix = []
    if axis == 0:
        new_matrix = mat1[:] + mat2[:]
    if axis == 1:
        new_matrix = mat1[:]
        for i in range(len(new_matrix)):
            new_matrix[i] = new_matrix[i] + mat2[i][:]
    return new_matrix
