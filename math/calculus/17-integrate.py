#!/usr/bin/env python3
"""Shebang"""


def poly_integral(poly, C=0):
    """Calculates the integral of a poly"""
    if not isinstance(poly, list):
        return None
    if not isinstance(C, int) or len(poly) < 1:
        return None
    new_poly = [C]
    for i in range(len(poly)):
        if i == len(poly) - 1 and poly[i] == 0:
            continue
        elif poly[i] != 0:
            result = poly[i] / (i + 1)
            new_poly.append(result if result % 1 else int(result))
        else:
            new_poly.append(0)
    return new_poly
