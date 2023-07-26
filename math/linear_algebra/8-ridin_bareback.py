#!/usr/bin/env python3
"""Shebang"""


def mat_mul(mat1, mat2):
    """Multiplies 2 matrices"""
    if len(mat1[0]) != len(mat2):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat1[0])):
                sum += mat1[i][k] * mat2[k][j]
            new_row.append(sum)
        new_matrix.append(new_row)
    return new_matrix
