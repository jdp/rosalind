# -*- coding: utf-8 -*-
from functools import cmp_to_key
from itertools import chain, product


def problem(dataset=None):
    """
    http://rosalind.info/problems/lexf/

    Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜
    and a positive integer n (n≤12).

    Return: All strings of length at most n formed from 𝒜, ordered
    lexicographically. (Note: As in “Enumerating k-mers Lexicographically”,
    alphabet order is based on the order in which the symbols are given.)

    """
    if not dataset:
        dataset = open("datasets/rosalind_lexv.txt").read()

    # Parse input from dataset
    input = dataset.strip().split()
    alphabet, n = (input[:-1], int(input[-1]))

    # Define a table and comparison function for the alphabet
    table = dict((c, i) for i, c in enumerate(alphabet))

    def compare(a, b):
        for i in range(max(len(a), len(b)) + 1):
            try:
                diff = table[a[i]] - table[b[i]]
                if diff == 0:
                    continue
                return diff
            except IndexError:
                if i not in a:
                    return 1
                if i not in b:
                    return -1
        return 0

    # Return the sorted items
    items = chain(*[product(alphabet, repeat=i) for i in range(1, n + 1)])
    return sorted(items, key=cmp_to_key(compare))

if __name__ == '__main__':
    print '\n'.join(map(''.join, problem()))
