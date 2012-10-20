# -*- coding: utf-8 -*-
from difflib import SequenceMatcher
from itertools import combinations


def problem(dataset=None):
    """
    http://rosalind.info/problems/lcs/

    Given: A collection of k DNA strings (of length at most 1 kbp each; k≤100).

    Return: A longest common substring of the collection. (If multiple
    solutions exist, you may return any single solution.)

    """
    if not dataset:
        dataset = open("datasets/rosalind_lcs.txt").read()
    dnas = [l.strip() for l in dataset.splitlines() if l.strip()]

    def lcs(a, b):
        sm = SequenceMatcher(None, a, b, False)
        match = sm.find_longest_match(0, len(a), 0, len(b))
        matchstr = a[match.a:match.a + match.size]
        return matchstr

    # TODO: Optimize! This is embarassingly slow
    possible = filter(None, [lcs(*pair) for pair in combinations(dnas, 2)])
    likely = filter(lambda s: all((s in dna) for dna in dnas), possible)
    return sorted(likely, key=len)[-1]

if __name__ == '__main__':
    print problem()
