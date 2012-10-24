# -*- coding: utf-8 -*-


def problem(dataset=None):
    """
    http://rosalind.info/problems/perm/

    Given: An array A containing at most 20 real numbers between 0 and 1,
    inclusively.

    Return: An array B in which B[i] represents the probability (to an accuracy
    of three decimal places) that for the GC-content in A[i], two randomly
    chosen symbols will be the same.

    """
    if not dataset:
        dataset = open("datasets/rosalind_prob.txt").read()
    A = map(float, dataset.split())
    return [((x ** 2) + ((1 - x) ** 2)) / 2 for x in A]

if __name__ == '__main__':
    print ' '.join(map(str, problem()))
