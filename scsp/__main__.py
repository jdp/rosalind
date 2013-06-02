"""
Given: Two DNA strings s and t.

Return: A shortest common supersequence of s and t. If multiple solutions
exist, you may output any one.

>>> problem('ATCTGAT', 'TGCATA')
'ATGCATGAT'
"""

from ..util import lcs


def problem(s, t):
    z = lcs(s, t)
    u = ""
    i = 0
    j = 0
    for c in z:
        if i < len(s):
            while s[i] != c:
                u += s[i]
                i += 1
            i += 1
        if j < len(t):
            while t[j] != c:
                u += t[j]
                j += 1
            j += 1
        u += c
    if i < len(s):
        u += s[i:]
    if j < len(t):
        u += t[j:]
    return u


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + '/data.txt').readlines()
    s, t = [line.strip() for line in dataset]
    print problem(s, t)
