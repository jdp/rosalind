"""
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a
subsequence of s. If multiple solutions exist, you may return any one.

>>> problem('ACGTACGTGACG', 'GTA')
[3, 4, 5]
"""


def problem(s, t):
    offset = 0
    result = []
    for c in t:
        i = s.index(c) + 1
        offset += i
        result.append(offset)
        s = s[i:]
    return result


if __name__ == '__main__':
    import doctest
    from os.path import dirname
    from ..util import parse_fasta

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").read()
    dataset = parse_fasta(dataset)
    s, t = dataset.values()
    print ' '.join(map(str, problem(s, t)))
