# -*- coding: utf-8 -*-


def problem(dataset=None):
    """
    http://rosalind.info/problems/eval/

    Given: A positive integer m (m≤10), a positive integer n (n≤10,000), and an
    array A of length at most 20 containing real numbers between 0 and 1,
    inclusively.

    Return: An array B in which B[i] represents the expected number of
    substring matches of a random string of length m inside a random string of
    length n, where both are formed from GC-content A[i] (see “Introduction to
    Probability”). Each value in B should have be accurate to three decimal
    places.

    >>> map(lambda x: round(x, 6), problem('2 10\\n0.32 0.42 0.81'))
    [0.717748, 0.591669, 1.078067]

    """
    def probsum(gc_content):
        # equivalent P(G)^2 + P(C)^2 + P(A)^2 + P(T)^2
        return ((gc_content ** 2) + ((1 - gc_content) ** 2)) / 2

    if not dataset:
        dataset = open("datasets/rosalind_eval.txt").read()

    # Parse input from dataset
    lines = dataset.strip().splitlines()
    m, n = map(int, lines[0].split())
    A = map(float, lines[1].split())

    # Find expected value for each GC-content in A
    return [(n - m + 1) * probsum(gc_content) ** m for gc_content in A]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print ' '.join(map(str, problem()))
