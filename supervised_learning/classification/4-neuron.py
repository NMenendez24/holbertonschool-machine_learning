#!/usr/bin/env python3
"""Shebang"""


import numpy as np


class Neuron:
    """Define a neuron"""
    def __init__(self, nx):
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.__b = 0
        self.__A = 0
        self.__W = np.random.normal(size=(1, nx))

    @property
    def W(self):
        """return the W"""
        return self.__W

    @property
    def A(self):
        """return the A"""
        return self.__A

    @property
    def b(self):
        """return the b"""
        return self.__b

    def forward_prop(self, X):
        """forward propagation of the given X"""
        z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))
        return self.__A

    def cost(self, Y, A):
        """Calculate the cost of the given Y"""
        m = Y.shape[1]
        cost = -1/m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        predictions = self.forward_prop(X)
        return (predictions >= 0.5).astype(int), self.cost(Y, predictions)
