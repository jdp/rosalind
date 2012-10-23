# -*- coding: utf-8 -*-
from itertools import count, islice, permutations


def problem(dataset=None):
    """
    http://rosalind.info/problems/perm/

    Given: A positive integer n≤7.

    Return: The total number of permutations of length n, followed by a list of
    all such permutations (in any order).

    """
    if not dataset:
        dataset = open("datasets/rosalind_perm.txt").read()
    n = int(dataset.strip())
    return permutations(islice(count(start=1), 0, n))

if __name__ == '__main__':
    perms = list(problem())
    print len(perms)
    for p in perms:
        print ' '.join(map(str, p))
