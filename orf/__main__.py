"""
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from
ORFs of s. Strings can be returned in any order.

>>> dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
>>> r = problem(dna)
>>> format(r)
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""

import re
from ..util import get_codon_map, reshape, reverse_complement


def problem(dnaprime):
    codons = get_codon_map()
    start_codon = 'AUG'
    stop_codons = ['UAA', 'UAG', 'UGA']
    for dna in [reverse_complement(dnaprime), dnaprime]:
        rna = dna.replace('T', 'U')
        starts = [m.start() for m in re.finditer(start_codon, rna)]
        for start in starts:
            fragment = rna[start:]
            protein = ""
            for triplet in reshape(fragment, 3):
                codon = codons[''.join(triplet)]
                if not codon:
                    yield protein
                    break
                protein += codon


def format(result):
    seen = set()
    for r in result:
        if r not in seen:
            print r
        seen.update([r])


if __name__ == '__main__':
    import doctest
    from os.path import dirname
    from ..util import parse_fasta

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").read()
    dataset = parse_fasta(dataset)
    for dna in dataset.values():
        format(problem(dna))
