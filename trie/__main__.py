# -*- coding: utf-8 -*-

"""
http://rosalind.info/problems/trie/

Given: A list of at most 100 DNA strings of length at most 100 bp, none of
which is a prefix of another.

Return: The adjacency list corresponding to the trie T for these patterns, in
the following format. If T has n nodes, first label the root with 1 and then
label the remaining nodes with the integers 2 through n in any order you like.
Each edge of the adjacency list of T will be encoded by a triple containing the
integer representing the edge's parent node, followed by the integer
representing the edge's child node, and finally the symbol labeling the edge.

>>> trie = problem(['ATAGA', 'ATC', 'GAT'])
>>> format(trie)
1 2 A
2 3 T
3 4 A
4 5 G
5 6 A
3 7 C
1 8 G
8 9 A
9 10 T
"""

from itertools import count


class NumberedTrie(object):
    def __init__(self):
        self.counter = count(start=1)
        self.root = [next(self.counter), {}]

    def insert(self, bp):
        node = self.root
        for ch in bp:
            if ch not in node[1]:
                node[1][ch] = [next(self.counter), {}]
            node = node[1][ch]


def problem(bps):
    trie = NumberedTrie()
    for bp in bps:
        trie.insert(bp)
    return trie.root


def format(node):
    for ch, node2 in node[1].iteritems():
        print node[0], node2[0], ch
        format(node2)


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_trie.txt").readlines()
    dataset = [l.strip() for l in dataset if l.strip()]
    format(problem(dataset))
