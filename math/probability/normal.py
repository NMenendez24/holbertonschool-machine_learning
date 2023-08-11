#!/usr/bin/env python3
"""Shebang"""


pi = 3.1415926536
e = 2.7182818285


def erf(x):
    """Error function"""
    return ((2 / (pi ** 0.5)) * (x - ((x ** 3) / 3) + ((x ** 5) / 10) -
                                 ((x ** 7) / 42) + ((x ** 9) / 216)))


class Normal:
    """Define a normal class"""
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

    def z_score(self, x):
        """Return z score"""
        return ((x - self.mean) / self.stddev)

    def x_value(self, z):
        """Return x score"""
        return ((z * self.stddev) + self.mean)

    def pdf(self, x):
        """Returns pdf"""
        return (1 / (self.stddev * ((2 * pi) ** 0.5))) * \
               (e ** - ((((x - self.mean) ** 2)) / (2 * (self.stddev ** 2))))

    def cdf(self, x):
        """Returns cdf"""
        return (0.5 * (1 + erf((x - self.mean) / (self.stddev * (2 ** 0.5)))))
