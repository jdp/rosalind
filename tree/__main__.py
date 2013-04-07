"""
http://rosalind.info/problems/tree/

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a
graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce
a tree.

>>> problem(10, [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)])
3
"""


def problem(n, edges):
    return n - len(edges) - 1

if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_tree.txt").readlines()
    n = int(dataset[0])
    edges = []
    for i in range(1, len(dataset)):
        edges.append(map(int, dataset[i].split()))
    print problem(n, edges)
