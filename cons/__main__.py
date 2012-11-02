# -*- coding: utf-8 -*-
from collections import Counter
from os.path import dirname


def problem(dataset=None):
    """
    http://rosalind.info/problems/cons/

    Given: A collection of at most 10 DNA strings of equal length, at most 1
    kbp.

    Return: A consensus string and profile matrix for the collection. If
    several possible consensus strings exist, then you may return any one of
    them.

    """
    if not dataset:
        dataset = open(dirname(__file__) + "/rosalind_cons.txt").read()
    dnas = [line.strip() for line in dataset.splitlines()]
    counts = map(Counter, zip(*dnas))
    consensus = [c.most_common(1)[0][0] for c in counts]
    acids = ('A', 'C', 'G', 'T')
    profile = dict((acid, [c.get(acid, 0) for c in counts]) for acid in acids)
    return consensus, profile

if __name__ == '__main__':
    consensus, profile = problem()
    print ''.join(consensus)
    for acid in ('A', 'C', 'G', 'T'):
        print "%s: %s" % (acid, ' '.join(map(str, profile[acid])))
