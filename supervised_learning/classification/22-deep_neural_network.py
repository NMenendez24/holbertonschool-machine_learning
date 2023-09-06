#!/usr/bin/env python3
"""Shebang"""


import numpy as np


class DeepNeuralNetwork:
    """Initializes a deep neural network"""
    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(
               layers) == 0 or min(layers) <= 0:
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(1, self.__L + 1):
            if i == 1:
                self.__weights['W' + str(i)] = np.random.randn(
                    layers[i - 1], nx) * np.sqrt(2. / nx)
            else:
                self.__weights['W' + str(i)] = np.random.randn(
                    layers[i - 1], layers[i - 2]) * np.sqrt(2. / layers[i - 2])
            self.__weights['b' + str(i)] = np.zeros((layers[i - 1], 1))

    @property
    def L(self):
        return self.__L

    @property
    def weights(self):
        return self.__weights

    @property
    def cache(self):
        return self.__cache

    def sigmoid(self, Z):
        """Sigmoid activation Function"""
        return 1 / (1 + np.exp(-Z))

    def forward_prop(self, X):
        """Forward Propagation function"""
        self.__cache["A0"] = X

        for layer in range(self.__L):
            w = "W{}".format(layer + 1)
            b = "b{}".format(layer + 1)
            a = "A{}".format(layer + 1)

            z_1 = np.dot(self.__weights[w], self.__cache["A{}".format(layer)])
            z = z_1 + self.__weights[b]
            self.__cache[a] = self.sigmoid(z)
        return self.__cache[a], self.__cache

    def cost(self, Y, A):
        """Returns the cost"""
        m = Y.shape[1]
        cost = -1/m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """Evaluates the neuron's predictions"""
        predictions, _ = self.forward_prop(X)
        return (predictions >= 0.5).astype(int), self.cost(Y, predictions)

    def gradient_descent(self, Y, cache, alpha=0.05):
        """Gradient Descent"""
        m = Y.shape[1]
        dz = cache["A{}".format(self.__L)] - Y

        for lyr in range(self.__L, 0, -1):
            wN = "W{}".format(lyr)
            bN = "b{}".format(lyr)
            aN = "A{}".format(lyr - 1)

            dw = 1 / m * np.matmul(dz, cache[aN].T)
            db = 1 / m * np.sum(dz, axis=1, keepdims=True)
            dz = (np.matmul(self.__weights[wN].T, dz) *
                  (cache[aN] * (1 - cache[aN])))

            self.__weights[wN] -= alpha * dw
            self.__weights[bN] -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """Train the deep neural network"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        for _ in range(iterations):
            A, cache = self.forward_prop(X)
            self.gradient_descent(Y, cache, alpha)
        return self.evaluate(X, Y)
