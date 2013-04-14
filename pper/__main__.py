"""
Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.

>>> problem(21, 7)
51200L
"""

from math import factorial


def problem(n, k):
    # P(n,k) is n!/(n-k)!
    return factorial(n) / factorial(n - k) % 1000000


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + '/rosalind_pper.txt').read().strip()
    n, k = map(int, dataset.split())
    print problem(n, k)
