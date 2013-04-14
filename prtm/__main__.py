"""
Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

>>> round(problem("SKADYEK"), 3)
821.392
"""

from ..util import monoisotopic_mass


def problem(protein):
    return sum([monoisotopic_mass(c) for c in protein])

if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_prtm.txt").read().strip()
    print problem(dataset)
