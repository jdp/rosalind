"""
Given: Positive integers n and m with 0≤m≤n≤2000.

Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo
1,000,000. In shorthand, ∑nk=m(nk).

>>> problem(6, 3)
42
"""

from ..util import binomial


def problem(n, m):
    return sum(binomial(n, k) for k in range(m, n+1)) % 1000000


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").read()
    n, m = map(int, dataset.strip().split())
    print problem(n, m)
