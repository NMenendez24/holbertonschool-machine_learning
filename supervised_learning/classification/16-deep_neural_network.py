#!/usr/bin/env python3
"""Shebang"""


import numpy as np


class DeepNeuralNetwork:
    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list):
            raise TypeError("layers must be a list of positive integers")
        if not all(num > 0 for num in layers):
            raise TypeError("layers must be a list of positive integers")
        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(1, self.L + 1):
            if i == 1:
                self.weights['W' + str(i)] = np.random.randn(
                    layers[i - 1], nx) * np.sqrt(2. / nx)
            else:
                self.weights['W' + str(i)] = np.random.randn(
                    layers[i - 1], layers[i - 2]) * np.sqrt(2. / layers[i - 2])
            self.weights['b' + str(i)] = np.zeros((layers[i - 1], 1))
