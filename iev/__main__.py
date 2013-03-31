"""
Given: Six positive integers, each of which does not exceed 20,000. The
integers correspond to the number of couples in a population possessing each
genotype pairing for a given factor. In order, the six given integers represent
the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in
the next generation, under the assumption that every couple has exactly two
offspring.

>>> problem([1, 0, 0, 1, 0, 1])
3.5

"""

from itertools import product
from os.path import dirname

couples = [('AA', 'AA'),
           ('AA', 'Aa'),
           ('AA', 'aa'),
           ('Aa', 'Aa'),
           ('Aa', 'aa'),
           ('aa', 'aa')]


def punnett(a, b):
    return map(''.join, product(a, b))


def P(square):
    return float(len([x for x in square if 'A' in x])) / len(square)


def E(k, p):
    return k * p


def problem(counts):
    return sum(2 * E(k, P(punnett(*c))) for k, c in zip(counts, couples))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_iev.txt").read()
    print problem(map(int, dataset.strip().split()))
