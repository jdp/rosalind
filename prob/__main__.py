"""
Given: A DNA string s of length at most 100 bp and an array A containing at
most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the
common logarithm of the probability that a random string constructed with the
GC-content found in A[k] will match s exactly.

>>> s = "ACGATACAA"
>>> A = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]
>>> r = problem(s, A)
>>> format(r)
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009
"""

from math import log


def problem(s, A):
    for a in A:
        pgc = a / 2
        pat = (1 - a) / 2
        pmf = {"G": pgc, "C": pgc, "A": pat, "T": pat}
        yield log(reduce(lambda x, y: x * y, map(lambda k: pmf.get(k), s)), 10)


def format(result):
    print " ".join("{:0.3f}".format(r) for r in result)


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    s, A = open(dirname(__file__) + '/data.txt').readlines()
    s = s.strip()
    A = map(float, A.strip().split())
    format(problem(s, A))
