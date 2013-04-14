"""
Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1
kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings.
As always, note that your answer is allowed an absolute error of 0.001.

>>> r = problem(['TTTCCATTTA', 'GATTCATTTC', 'TTTCCATTTT', 'GTTCCATTTA'])
>>> format(r)
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000
"""

from itertools import product
from ..util import parse_fasta, reshape


def p_distance(a, b):
    return float(sum([1 for x, y in zip(a, b) if x != y])) / len(max(a, b))


def problem(dnas):
    result = [p_distance(a, b) for a, b in product(dnas, dnas)]
    return reshape(result, len(dnas))


def format(result):
    for row in result:
        print " ".join(["{:0.6f}".format(r)[:-1] for r in row])

if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_pdst.txt").read()
    dataset = parse_fasta(dataset)
    format(problem(dataset.values()))
