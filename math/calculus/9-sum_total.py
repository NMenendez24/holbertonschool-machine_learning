#!/usr/bin/env python3
"""Shebang"""


def summation_i_squared(n):
    """Sumation of the square"""
    if not isinstance(n, int or float):
        return None
    result = 0
    for i in range(1, n + 1):
        result = result + i ** 2
    return result
