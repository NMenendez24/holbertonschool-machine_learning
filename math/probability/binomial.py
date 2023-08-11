#!/usr/bin/env python3
"""Shebang"""


pi = 3.1415926536
e = 2.7182818285


class Binomial:
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n < 0:
                raise ValueError("n must be a positive value")
            self.n = round(n)
            if p < 0 or p > 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.p = p
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            sum_data = 0
            for value in data:
                sum_data += ((value - mean) ** 2)
            variance = (sum_data / len(data))
            self.n = round(mean / (1 - (variance / mean)))
            self.p = mean / self.n

    def pmf(self, k):
        """Returns the pmf"""
        if k < 0:
            return 0
        self.k = int(k)
        fact_n = 1
        for i in range(1, self.n):
            fact_n += fact_n * i
        fact_k = 1
        for i in range(1, k):
            fact_k += fact_k * i
        fact_n_k = 1
        for i in range(1, self.n - self.k):
            fact_n_k += fact_n_k * i
        n_k = fact_n / (fact_k * fact_n_k)
        return (n_k * (self.p ** self.k) * ((1 - self.p) ** (self.n - self.k)))

    def cdf(self, k):
        """returns the cdf"""
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
