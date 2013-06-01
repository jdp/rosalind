"""
Given: Two protein strings s and t in FASTA format (each of length at most 1000
aa).

Return: The edit distance dE(s,t).

>>> problem('PLEASANTLY', 'MEANLY')
5
"""

from ..util import levenshtein


def problem(s, t):
    return levenshtein(s, t)


if __name__ == '__main__':
    import doctest
    from os.path import dirname
    from ..util import parse_fasta

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").read()
    dataset = parse_fasta(dataset)
    s, t = dataset.values()
    print problem(s, t)
