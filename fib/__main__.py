"""
http://rosalind.info/problems/fib/

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months if
each pair of reproduction-age rabbits produces a litter of k rabbit pairs in
each generation (instead of only 1 pair).

>>> problem(5, 3)
19
"""

import itertools
import os


def problem(n, k):
    def rabbits(k):
        xs = [1, 1]
        for x in xs:
            yield x
        while True:
            xs.append(xs[-1] + xs[-2] * k)
            # print xs
            yield xs[-1]
    return next(itertools.islice(rabbits(k), n - 1, None), None)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    dataset = open(os.path.dirname(__file__) + "/rosalind_fib.txt").read()
    n, k = map(int, dataset.strip().split())
    print n, k, problem(n, k)
