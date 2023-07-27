#!/usr/bin/env python3
"""Shebang"""


import numpy as np


def np_elementwise(mat1, mat2):
    """Return a tuple with some calculations between matrices"""
    return (mat1 + mat2, mat1 - mat2, np.multiply(mat1, mat2),
            np.divide(mat1, mat2))
