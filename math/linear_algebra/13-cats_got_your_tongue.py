#!/usr/bin/env python3
"""Shebang"""

import numpy as np
def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices"""
    return np.concatenate((mat1, mat2), axis=axis)
