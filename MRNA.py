# -*- coding: utf-8 -*-
from collections import defaultdict
from operator import mul


def problem(dataset=None):
    """
    http://rosalind.info/problems/mrna/

    Given: A protein string of length at most 50 aa.

    Return: The total number of different RNA strings from which the protein
    could have been translated.

    """
    if not dataset:
        dataset = open("datasets/rosalind_mrna.txt").read()

    amino_acids = defaultdict(list)
    with open("codons.txt") as f:
        for line in f:
            if not line.strip():
                continue
            codon, aa = line.strip().split()
            if aa == 'Stop':
                aa = None
            amino_acids[aa].append(codon)

    pool = [amino_acids[aa] for aa in dataset] + [amino_acids[None]]
    return reduce(mul, map(len, pool))


if __name__ == '__main__':
    print problem()
