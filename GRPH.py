# -*- coding: utf-8 -*-
from collections import defaultdict
from util import parse_fasta


def problem(dataset=None):
    """
    http://rosalind.info/problems/grph/

    Given: A collection of DNA strings in FASTA format having total length at
    most 10 kbp.

    Return: The adjacency list corresponding to O3.

    """
    if not dataset:
        dataset = open("datasets/rosalind_grph.txt").read()
    records = parse_fasta(dataset)
    suffixes = defaultdict(list)
    for record_id, bps in records.iteritems():
        suffixes[bps[-3:]].append(record_id)
    graph = defaultdict(list)
    for w_record_id, bps in records.iteritems():
        for v_record_id in suffixes[bps[:3]]:
            graph[v_record_id].append(w_record_id)
    return graph

if __name__ == '__main__':
    graph = problem()
    for v, ws in graph.iteritems():
        for w in ws:
            if w == v:
                continue
            print v, w
