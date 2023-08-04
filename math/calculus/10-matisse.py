#!/usr/bin/env python3
"""Shebang"""


def poly_derivative(poly):
    """Calculate the derivative of a poly"""
    if not isinstance(poly, list):
        return None
    if len(poly) < 2:
        return [0]
    new_poly = []
    for x in range(1, len(poly)):
        new_poly.append(x * poly[x])
    return new_poly
