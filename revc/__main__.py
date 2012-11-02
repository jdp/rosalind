# -*- coding: utf-8 -*-
from os.path import dirname
from string import maketrans


def problem(dataset=None):
    """
    In a DNA string, the complement of A is T, and the complement of C is G.

    The reverse complement of a DNA string s is the string sc formed by
    reversing the symbols of s, then taking the complement of each symbol
    (e.g., the reverse complement of GTCA is TGAC).

    Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement of s.

    """
    if not dataset:
        dataset = open(dirname(__file__) + "/rosalind_revc.txt").read()
    return dataset[::-1].translate(maketrans('ATCG', 'TAGC'))

if __name__ == '__main__':
    print problem('AAAACCCGGT')
