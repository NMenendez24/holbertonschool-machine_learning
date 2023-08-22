#!/usr/bin/env python3
"""Shebang"""


import numpy as np
import matplotlib.pyplot as plt


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
        """Evaluates the neuron's predictions"""
        predictions = self.forward_prop(X)
        return (predictions >= 0.5).astype(int), self.cost(Y, predictions)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Calculates one pass of gradient descent on the neuron"""
        m = X.shape[1]
        dJ_dW = (1/m) * np.dot(X, (A - Y).T)
        dJ_db = (1/m) * np.sum(A - Y)
        self.__W -= alpha * dJ_dW.T
        self.__b -= alpha * dJ_db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """Train the neuron"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if graph or verbose:
            if not isinstance(step, int):
                raise ValueError("step must be an integer")
            if step <= 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")
        iteration_steps = range(0, iterations + 1, step)
        cost = []
        for i in range(iterations + 1):
            cost.append(self.cost(Y, self.forward_prop(X)))
            if i % step == 0:
                if verbose:
                    print("Cost after {} iterations: {}".format(i, self.cost(Y, self.forward_prop(X))))
                if graph:
                    plt.plot(iteration_steps[:i//step+1], cost[::step], 'b-')
                    plt.xlabel('Iteration')
                    plt.ylabel('Cost')
                    plt.title('Training Cost')
            self.gradient_descent(X, Y, self.forward_prop(X), alpha)
        if verbose:
            print("Cost after {} iterations: {}".format(i, self.cost(Y, self.forward_prop(X))))
        if graph:
            plt.show()
        return self.evaluate(X, Y)
