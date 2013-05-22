"""
After identifying the exons and introns of an RNA string, we only need to
delete the introns and concatenate the exons to form a new string ready for
translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons
of s. (Note: Only one solution will exist for the dataset provided.)

>>> dna = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
>>> introns = ['ATCGGTCGAA', 'ATCGGTCGAGCGTGT']
>>> problem(dna, introns)
'MVYIADKQHVASREAYGHMFKVCA'
"""

from ..util import get_codon_map


def problem(dna, introns):
    introns = sorted(introns, key=len, reverse=True)
    for intron in introns:
        while intron in dna:
            dna = dna.replace(intron, '')
    codons = get_codon_map()
    rna = dna.replace('T', 'U')
    return ''.join([codons[rna[t:t+3]] for t in range(0, len(rna)-2, 3)][:-1])


if __name__ == '__main__':
    import doctest
    from os.path import dirname
    from ..util import parse_fasta

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").read()
    dataset = parse_fasta(dataset)
    dna, introns = dataset.values()[0], dataset.values()[1:]
    print problem(dna, introns)
