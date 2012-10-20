# -*- coding: utf-8 -*-


def problem(dataset=None):
    """
    Given two strings s=s1s2⋯sn and t=t1t2⋯tm where m≤n, t is a substring of s
    if t is contained as a contiguous collection of symbols in s.

    The position of a symbol in a string is the total number of symbols found
    to its left, including itself (e.g., the positions of all occurrences of U
    in AUGCUUCAGAAAGGUCUUACG are 2, 5, 6, 15, 17, and 18). The symbol at
    position i of s is denoted by s[i]. For that matter, a substring of s can
    be represented as s[j:k], where j and k represent the starting and ending
    positions of the substring in s.

    The location of a substring is its beginning position; note that t will
    have multiple locations in s if it occurs more than once as a substring of
    s (see the Sample sections below).

    Given: Two DNA strings s and t (each of length at most 1 kbp).

    Return: All locations of t as a substring of s.

    """
    if not dataset:
        dataset = open("datasets/rosalind_subs.txt").read()
    s, t = dataset.strip().splitlines()
    acids = [(s[i:i + len(t)], i + 1) for i in range(0, len(s) - len(t) + 1, 1)]
    return [acid[1] for acid in acids if acid[0] == t]

if __name__ == '__main__':
    print ' '.join(map(str, problem()))
