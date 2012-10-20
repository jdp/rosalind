# -*- coding: utf-8 -*-
from collections import defaultdict


def parse_fasta(dataset):
    "Parses data in FASTA format, returning a dictionary of ID's and values"
    records = defaultdict(str)
    record_id = None
    for line in [l.strip() for l in dataset.splitlines()]:
        if line.startswith('>'):
            record_id = line[1:]
        else:
            records[record_id] += line
    return records
