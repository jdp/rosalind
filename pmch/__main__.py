# -*- coding: utf-8 -*-

"""
Given: An RNA string s of length at most 80 bp having the same number of
occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the
bonding graph of s.

>>> problem("AGCUAGUCAU")
12
"""

from math import factorial
from os.path import dirname
from ..util import parse_fasta


def problem(rna):
    return factorial(rna.count("A")) * factorial(rna.count("C"))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_pmch.txt").read()
    for name, rna in parse_fasta(dataset).iteritems():
        print problem(rna)
