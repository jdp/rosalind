"""
Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms: k individuals are homozygous dominant for a factor,
m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will
produce an individual possessing a dominant allele (and thus displaying the
dominant phenotype). Assume that any two organisms can mate.

>>> round(problem(2, 2, 2), 5)
0.78333
"""

import os
from itertools import chain, combinations, product


def mate(a, b):
    return map(''.join, product(a, b))


def problem(k, m, n):
    population = ["AA"] * k + ["Aa"] * m + ["aa"] * n
    possible = list(chain(*[mate(a, b) for a, b in combinations(population, 2)]))
    print possible
    doms = [p for p in possible if "A" in p]
    print doms
    return float(len(doms)) / len(possible)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    dataset = open(os.path.dirname(__file__) + "/rosalind_iprb.txt").read()
    k, m, n = map(int, dataset.strip().split())
    print problem(k, m, n)
