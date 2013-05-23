"""
For DNA strings s1 and s2 having the same length, their transition/transversion
ratio R(s1,s2) is the ratio of the total number of transitions to the total
number of transversions, where symbol substitutions are inferred from
mismatched corresponding symbols as when calculating Hamming distance (see
“Counting Point Mutations”).

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).

>>> s1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
>>> s2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
>>> round(problem(s1, s2), 11)
1.21428571429
"""


def problem(s1, s2):
    transitions = set([('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')])
    ratio = {True: 0.0, False: 0.0}
    for p in zip(s1, s2):
        if p[0] != p[1]:
            ratio[p in transitions] += 1
    return ratio[True] / ratio[False]


if __name__ == '__main__':
    import doctest
    from os.path import dirname
    from ..util import parse_fasta

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").read()
    dataset = parse_fasta(dataset)
    s1, s2 = dataset.values()
    print problem(s1, s2)
