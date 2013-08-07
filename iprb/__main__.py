"""
Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms: k individuals are homozygous dominant for a factor,
m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will
produce an individual possessing a dominant allele (and thus displaying the
dominant phenotype). Assume that any two organisms can mate.

>>> round(problem(2, 2, 2), 5)
0.78333
"""

def problem(k, m, n):
    k, m, n = map(float, (k, m, n))
    p = [
        k * (k - 1),  # AA, AA pairs
        k * m,  # AA, Aa pairs
        k * n,  # AA, aa pairs
        m * k,  # Aa, AA pairs
        m * (m - 1) * 0.75, # Aa, Aa pairs
        m * n * 0.5, # Aa, aa pairs
        n * k,  # aa, AA pairs
        n * m * 0.5,  # aa, Aa pairs
        0,  # aa, aa pairs
    ]
    t = k + m + n
    return sum(p) / t / (t - 1)


if __name__ == '__main__':
    import doctest
    import os
    doctest.testmod()

    dataset = open(os.path.dirname(__file__) + "/rosalind_iprb.txt").read()
    k, m, n = map(float, dataset.strip().split())
    print problem(k, m, n)
