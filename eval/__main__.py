"""
>>> [round(x, 3) for x in problem(10, 'AG', [0.25, 0.5, 0.75])]
[0.422, 0.563, 0.422]
"""

from ..util import gc_p


def problem(n, s, A):
    return [gc_p(a, s) * (n - 1) for a in A]


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + '/data.txt').readlines()
    dataset = [line.strip() for line in dataset]
    n, s, A = dataset
    n = int(n)
    A = map(float, A.split())
    print ' '.join(map(str, problem(n, s, A)))
