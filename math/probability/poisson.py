#!/usr/bin/env python3
"""
Create a class Poisson that represents a poisson distribution:
"""

import math

class Poisson:
    """
    The Poisson class
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize the Poisson distribution

        Args:
            data (list, optional): List of data to estimate the distribution. Defaults to None.
            lambtha (float, optional): Expected number of occurrences in a given time frame. Defaults to 1.

        Raises:
            ValueError: If lambtha is not positive when data is None
            TypeError: If data is provided but is not a list
            ValueError: If data is provided but contains fewer than two values
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
        Calculates the value of the PMF for a given number of "successes"

        Args:
            k (int): The number of "successes"

        Returns:
            float: The PMF value for k
        """
        k = int(k)
        if k < 0:
            return 0
        return (math.exp(-self.lambtha) * (self.lambtha ** k)) / math.factorial(k)
