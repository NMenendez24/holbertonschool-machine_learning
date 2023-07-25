#!/usr/bin/env python3
"""Shebang"""


def matrix_transpose(matrix):
    """Returns the transpose of a matrix"""
    new_matrix = [[matrix[i][j] for i in range(len(matrix))]\
                   for j in range(len(matrix[0]))]
    return new_matrix
