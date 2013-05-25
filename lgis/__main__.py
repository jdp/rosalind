"""
>>> problem(5, [5, 1, 4, 2, 3])
([1, 2, 3], [5, 4, 2])
"""

from ..util import lcs


def problem(n, pi):
    incr = lcs(pi, sorted(pi))
    decr = lcs(pi, sorted(pi, reverse=True))
    return (incr, decr)


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").readlines()
    n, pi = [l.strip() for l in dataset]
    n = int(n)
    pi = map(int, pi.split())

    for seq in problem(n, pi):
        print ' '.join(map(str, seq))
