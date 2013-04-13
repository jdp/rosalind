# -*- coding: utf-8 -*-

"""
Given: A positive integer n (n≤1000).

Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.

>>> problem(3)
8
"""

from ..util import binomial


def problem(n):
    return sum([binomial(n, i) for i in range(n + 1)]) % 1000000


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    n = int(open(dirname(__file__) + "/rosalind_sset.txt").read().strip())
    print problem(n)
