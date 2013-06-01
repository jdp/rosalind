"""
Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA
string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as
s are constructed with GC-content x (see “Introduction to Random Strings”),
then at least one of the strings equals s. We allow for the same random string
to be created more than once.

>>> round(problem(90000, 0.6, 'ATAGCCGA'), 3)
0.689
"""

from ..util import binomial_pmf, gc_p


def problem(N, x, s):
    return 1 - binomial_pmf(N, 0, gc_p(x, s))


if __name__ == '__main__':
    import doctest
    from os.path import dirname
    doctest.testmod()

    dataset = open(dirname(__file__) + '/data.txt').readlines()
    dataset = [line.strip() for line in dataset]
    N, x = int(dataset[0].split()[0]), float(dataset[0].split()[1])
    s = dataset[1]
    print problem(N, x, s)
