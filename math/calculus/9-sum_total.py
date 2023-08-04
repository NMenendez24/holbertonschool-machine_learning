#!/usr/bin/env python3
"""Shebang"""


def summation_i_squared(n):
    """Sumation of the square"""
    if not isinstance(n, int) or n < 1:
        return None
    return int((n * ((n + 1) * ((2 * n) + 1))) / 6)
