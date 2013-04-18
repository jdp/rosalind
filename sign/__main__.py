"""
Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list
of all such permutations (you may list the signed permutations in any order).

>>> format(problem(2))
8
-1 -2
1 -2
-1 2
1 2
-2 -1
2 -1
-2 1
2 1
"""

from itertools import combinations, permutations


def problem(n):
    l = range(1, n + 1)
    for p in permutations(l):
        for i in range(len(p) + 1):
            for c in combinations(range(len(p)), i):
                yield map(lambda t: t[1] if t[0] in c else -t[1], enumerate(p))


def format(results):
    results = list(results)
    print len(results)
    for r in results:
        print " ".join(map(str, r))


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    n = int(open(dirname(__file__) + '/data.txt').read())
    format(problem(n))
