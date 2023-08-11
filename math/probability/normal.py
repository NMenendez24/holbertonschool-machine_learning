#!/usr/bin/env python3
"""Shebang"""


pi = 3.1415926536
e = 2.7182818285


class Normal:
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            sum_data = 0
            for value in data:
                sum_data += (value - self.mean) ** 2
            self.stddev = (sum_data / len(data)) ** 0.5
