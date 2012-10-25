# -*- coding: utf-8 -*-


def problem(dataset=None):
    """
    http://rosalind.info/problems/perm/

    Given: An array A containing at most 20 real numbers between 0 and 1,
    inclusively.

    Return: An array B in which B[i] represents the probability (to an accuracy
    of three decimal places) that for the GC-content in A[i], two randomly
    chosen symbols will be the same.

    >>> map(lambda x: round(x, 4), problem("0.23 0.31 0.75"))
    [0.3229, 0.2861, 0.3125]

    """
    if not dataset:
        dataset = open("datasets/rosalind_prob.txt").read()

    # Parse dataset
    A = map(float, dataset.split())

    # Return probabilities
    return [((x ** 2) + ((1 - x) ** 2)) / 2 for x in A]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print ' '.join(map(str, problem()))
