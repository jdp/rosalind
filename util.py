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


def parse_newick(text):
    import operator
    from parcon import Alpha, Digit, ZeroOrMore, Optional, Forward, OneOrMore, Longest, flatten, InfixExpr, CharIn

    labels = {}

    class ZNode(object):
        def __init__(self, label=None, length=None):
            self.label = label
            self.length = length
            self.children = []
            self.parent = None

        def add_child(self, node):
            node.parent = self
            self.children.append(node)

        def ancestors(self):
            pairs = [(self, 0)]
            node = self
            while node.parent:
                pairs.append((node.parent, pairs[-1][1] + 1))
                node = node.parent
            return pairs

        def __str__(self):
            return "{}[{}]:{}".format(
                self.label,
                ''.join(map(str, self.children)),
                self.length
            )

        def __repr__(self):
            s = "<%s" % (self.label or "?",)
            if self.children:
                s += " " + ", ".join(map(repr, self.children))
            s += ">"
            return s

    def make_leaf(ast):
        # print "leaf ast", ast
        label = ast
        node = ZNode(label=label)
        if label:
            labels[label] = node
        return node

    def make_internal(ast):
        # print "internal ast", ast
        if isinstance(ast[0], ZNode):
            node = ZNode()
            children = ast
        else:
            label = ast[-1]
            node = ZNode(label=label)
            if label:
                labels[label] = node
            children = ast[-2]
        for n in children:
            node.add_child(n)
        return node

    def test(args):
        # print "matched:", args
        return args

    Name = ZeroOrMore(Alpha() | CharIn("_"))[''.join]
    Leaf = Name
    Node = Forward()
    Internal = ("(" + InfixExpr(Node[lambda x: [x]], [(",", operator.add)]) + ")") + Optional(Name)
    Node << (Internal[make_internal] | Leaf[make_leaf])
    Tree = Node + ";"

    return Tree.parse_string(text), labels


def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = [a[x-1]] + result
            x -= 1
            y -= 1
    return result
