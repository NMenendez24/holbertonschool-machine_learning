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
