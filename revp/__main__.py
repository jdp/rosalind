"""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string
having length between 4 and 12. You may return these pairs in any order.

>>> r = problem("TCAATGCATGCGGGTCTATATGCAT")
>>> format(r)
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""

from string import maketrans
from ..util import parse_fasta


def reverse_complement(dna):
    return dna[::-1].translate(maketrans('ATCG', 'TAGC'))


def problem(dna):
    for i in range(4, 13):
        for j in range(len(dna) - i + 1):
            if dna[j:j+i] == reverse_complement(dna[j:j+i]):
                yield j, dna[j:j+i]


def format(result):
    for i, dna in sorted(result):
        print i + 1, len(dna)


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_revp.txt").read()
    for val in parse_fasta(dataset).values():
        format(problem(val))
