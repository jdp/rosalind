# -*- coding: utf-8 -*-
from collections import Counter, defaultdict


def problem(dataset=None):
    """
    http://rosalind.info/problems/gc/

    Given: At most 10 DNA strings in FASTA format of length at most 1 kbp each.

    Return: The ID of the string having the highest GC-content, followed by the
    GC-content of that string. The GC-content should have a precision of at
    least 2 decimal places.

    """
    if not dataset:
        dataset = open("datasets/rosalind_gc.txt").read()
    records = defaultdict(str)
    record_id = None
    for line in [l.strip() for l in dataset.splitlines()]:
        if line.startswith('>'):
            record_id = line[1:]
        else:
            records[record_id] += line

    def gc_count(dna):
        c = Counter(dna)
        return (c.get('G', 0) + c.get('C', 0)) / float(sum(c.values())) * 100

    ids_gccounts = [(k, gc_count(v)) for k, v in records.iteritems()]
    return sorted(ids_gccounts, key=lambda x: x[1])[-1]

if __name__ == '__main__':
    record_id, gc_count = problem()
    print record_id
    print "%f%%" % gc_count
