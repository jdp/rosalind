"""
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin
with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children
in the 1st generation, each of whom has two children, and so on. Each organism
always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th
generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.

>>> round(problem(2, 1), 3)
0.684
"""

from ..util import binomial


def P(n, k):
    """
    Return the probability that there are exactly n Aa Bb offspring after
    k generations.

    This can be modeled as a Bernoulli trial, where success is an organism
    has genotype Aa Bb and failure is any other genotype. Doing a Punnett
    square with Aa Bb and Aa Bb shows that probability of any offspring having
    that genotype is 0.25, so we use that as our p value.
    """
    return binomial(2**k, n) * 0.25**n * 0.75**(2**k - n)


def problem(k, N):
    """
    Return the answer to the problem.

    The trick is the "at least N" part of the problem description. Asking for
    "at least 1" is actually asking for the sum of all probabilities except
    for the probability that the number of Aa Bb offspring is 0, and we can
    handle that like this:

        1 - P(X=0)

    Where X is the random variable representing the number of offspring with
    the genotype Aa Bb. Following from this, if we want "at least 2", we should
    actually solve for this:

        1 - P(X=0) - P(X=1)

    Because we want "at least N", we need a general solution with N:

        1 - P(X=0) - P(X=1) - ... - P(X=N-1)
    """
    return 1 - sum([P(n, k) for n in range(N)])


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + '/data.txt').read().strip().split()
    k, N = map(int, dataset)
    print problem(k, N)
