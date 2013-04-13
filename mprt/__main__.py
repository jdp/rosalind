# -*- coding: utf-8 -*-

"""
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given
access ID followed by a list of locations in the protein string where the motif
can be found.

>>> r = problem(['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST'])
>>> format(r)
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

import urllib2
from ..util import parse_fasta


def fetch_fasta(uniprot_id):
    uri = 'http://www.uniprot.org/uniprot/{}.fasta'.format(uniprot_id)
    response = urllib2.urlopen(uri)
    return parse_fasta(response.read())


def matches(protein):
    for i in range(len(protein) - 3):
        if protein[i] != 'N':
            continue
        if protein[i+1] == 'P':
            continue
        if protein[i+2] not in ['S', 'T']:
            continue
        if protein[i+3] == 'P':
            continue
        yield i


def problem(uniprot_ids):
    for uniprot_id in uniprot_ids:
        for _, protein in fetch_fasta(uniprot_id).items():
            pos = list(matches(protein))
            if pos:
                yield (uniprot_id, [p + 1 for p in pos])


def format(result):
    for uniprot_id, pos in result:
        print uniprot_id
        print ' '.join(map(str, pos))


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_mprt.txt").readlines()
    dataset = [l.strip() for l in dataset if l.strip()]
    format(problem(dataset))
