#!/usr/bin/env python3
"""Shebang"""


import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    """Neural Network Class"""
    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1

    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2

    def sigmoid(self, Z):
        """Sigmoid activation Function"""
        return 1 / (1 + np.exp(-Z))

    def forward_prop(self, X):
        """Calculates the forward propagation"""
        self.__A1 = self.sigmoid(np.dot(self.__W1, X) + self.__b1)
        self.__A2 = self.sigmoid(np.dot(self.__W2, self.__A1) + self.__b2)
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """Returns the cost"""
        m = Y.shape[1]
        cost = -1/m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """Evaluates the neuron's predictions"""
        _, predictions = self.forward_prop(X)
        return (predictions >= 0.5).astype(int), self.cost(Y, predictions)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """Gradient descent algorithm"""
        m = X.shape[1]
        dZ2 = A2 - Y
        dW2 = (1/m) * np.dot(dZ2, A1.T)
        db2 = (1/m) * np.sum(dZ2, axis=1, keepdims=True)
        dZ1 = np.dot(self.__W2.T, dZ2) * A1 * (1 - A1)
        dW1 = (1/m) * np.dot(dZ1, X.T)
        db1 = (1/m) * np.sum(dZ1, axis=1, keepdims=True)
        self.__W2 -= alpha * dW2
        self.__b2 -= alpha * db2
        self.__W1 -= alpha * dW1
        self.__b1 -= alpha * db1

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """Train the neural network"""
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
            A1, A2 = self.forward_prop(X)
            cost_value = self.cost(Y, A2)
            cost.append(cost_value)
            if i % step == 0:
                if verbose:
                    print("Cost after {} iterations: {}".format(i, cost_value))
                if graph:
                    plt.plot(iteration_steps[:i//step+1], cost[::step], 'b-')
                    plt.xlabel('Iteration')
                    plt.ylabel('Cost')
                    plt.title('Training Cost')
            A1, A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, A1, A2, alpha)
        if graph:
            plt.show()
        return self.evaluate(X, Y)
