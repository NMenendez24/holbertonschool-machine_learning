#!/usr/bin/env python3
"""Shebang"""


pi = 3.1415926536
e = 2.7182818285


class Poisson:
    """Define a Poisson Class"""
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """Returns the pmf probability"""
        k = k if type(k) == int else int(k)
        if k < 0:
            return 0
        k_fact = 1
        for i in range(k):
            k_fact += k_fact * i
        return ((e ** -self.lambtha * self.lambtha ** k) / (k_fact))
