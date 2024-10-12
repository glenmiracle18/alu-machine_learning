#!/usr/bin/env python3
"""
Create a class Poisson that represents a poisson distribution:
"""


class Poisson:
    """
    The Poisson class
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize the Poisson distribution
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a number
        """
        k = int(k)
        if k < 0:
            return 0
        return (self.exp(-self.lambtha) * (self.lambtha ** k)) / self.factorial(k)

    def exp(self, x):
        """
        Calculates the exponential of x
        """
        result = 1.0
        term = 1.0
        n = 1
        while term > 1e-15:  # A small threshold for convergence
            term *= x / n
            result += term
            n += 1
        return result

    def factorial(self, n):
        """
        Calculates the factorial of n
        """
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
