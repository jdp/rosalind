"""
Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA
format.

Return: A longest common subsequence of s and t. (If more than one solution
exists, you may return any one.)

>>> problem('AACCTTGG', 'ACACTGTGA')
'AACTTG'
"""

from ..util import lcs


def problem(s, t):
    return ''.join(lcs(s, t))


if __name__ == '__main__':
    import doctest
    from os.path import dirname
    from ..util import parse_fasta

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").read()
    dataset = parse_fasta(dataset)
    s, t = dataset.values()
    print problem(s, t)
