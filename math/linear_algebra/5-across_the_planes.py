#!/usr/bin/env python3
"""Shebang"""


def add_matrices2D(mat1, mat2):
    """Add two matrices"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    new_matrix = []
    new_row = []
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            new_row.append(mat1[i][j] + mat2[i][j])
        new_matrix.append(new_row)
        new_row = []
    return new_matrix
