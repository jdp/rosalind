# -*- coding: utf-8 -*-
from collections import Callable, OrderedDict
from os.path import dirname


class DefaultOrderedDict(OrderedDict):
    def __init__(self, default_factory=None, *args, **kwargs):
        if (default_factory is not None and
                not isinstance(default_factory, Callable)):
            raise TypeError('first argument must be callable')
        OrderedDict.__init__(self, *args, **kwargs)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return OrderedDict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __reduce__(self):
        if self.default_factory is None:
            args = tuple()
        else:
            args = self.default_factory,
        return type(self), args, None, None, self.items()

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        return type(self)(self.default_factory, self)

    def __deepcopy__(self, memo):
        import copy
        return type(self)(self.default_factory,
                          copy.deepcopy(self.items()))

    def __repr__(self):
        return 'OrderedDefaultDict(%s, %s)' % (
            self.default_factory, OrderedDict.__repr__(self))


def parse_fasta(dataset):
    "Parses data in FASTA format, returning a dictionary of ID's and values"
    records = DefaultOrderedDict(str)
    record_id = None
    for line in [l.strip() for l in dataset.splitlines()]:
        if line.startswith('>'):
            record_id = line[1:]
        else:
            records[record_id] += line
    return records


def parse_set(text):
    return [s.strip() for s in text[1:-1].split(",")]


def binomial(n, k):
    """Compute n factorial by a direct multiplicative method."""
    if k > n - k:
        k = n - k  # Use symmetry of Pascal's triangle
    accum = 1
    for i in range(1, k + 1):
        accum *= (n - (k - i))
        accum /= i
    return accum


def reshape(l, n):
    return zip(*[iter(l)] * n)


def get_codon_map():
    mapping = {}
    for line in open(dirname(__file__) + "/codons.txt"):
        if not line.strip():
            continue
        codon, acid = line.strip().split()
        if acid == 'Stop':
            mapping[codon] = None
        else:
            mapping[codon] = acid
    return mapping


def monoisotopic_mass(acid):
    return {'A': 71.03711,
            'C': 103.00919,
            'D': 115.02694,
            'E': 129.04259,
            'F': 147.06841,
            'G': 57.02146,
            'H': 137.05891,
            'I': 113.08406,
            'K': 128.09496,
            'L': 113.08406,
            'M': 131.04049,
            'N': 114.04293,
            'P': 97.05276,
            'Q': 128.05858,
            'R': 156.10111,
            'S': 87.03203,
            'T': 101.04768,
            'V': 99.06841,
            'W': 186.07931,
            'Y': 163.06333}.get(acid)


def reverse_complement(dna):
    from string import maketrans
    return dna[::-1].translate(maketrans('ATCG', 'TAGC'))
