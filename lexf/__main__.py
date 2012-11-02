# -*- coding: utf-8 -*-
from functools import cmp_to_key
from itertools import product
from os.path import dirname


def problem(dataset=None):
    """
    http://rosalind.info/problems/lexf/

    Given: A collection of at most 10 symbols defining an ordered alphabet, and
    a positive integer n (n≤10).

    Return: All strings of length n that can be formed from the alphabet,
    ordered lexicographically.

    """
    if not dataset:
        dataset = open(dirname(__file__) + "/rosalind_lexf.txt").read()

    # Parse input from dataset
    input = dataset.strip().split()
    alphabet, n = (input[:-1], int(input[-1]))

    # Define a table and comparison function for the alphabet
    table = dict((c, i) for i, c in enumerate(alphabet))

    def compare(a, b):
        for i in range(len(a) + 1):
            diff = table[a[i]] - table[b[i]]
            if diff == 0:
                continue
            return diff
        return 0

    # Return the sorted alphabet
    return sorted(product(alphabet, repeat=n), key=cmp_to_key(compare))

if __name__ == '__main__':
    print '\n'.join(map(''.join, problem()))
