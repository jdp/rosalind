"""
Given: A collection of n trees (n≤40) in Newick format, with each tree
containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk
and yk in Tk.

Return: A collection of n positive integers, for which the kth integer
represents the distance between xk and yk in Tk.

>>> data = parse("(cat)dog;\\ndog cat\\n\\n(dog,cat);\\ndog cat")
>>> format(problem(t, k) for t, k in data)
1 2
"""


def parse(text):
    from ..util import parse_newick

    lines = filter(None, text.split("\n"))
    pairs = [lines[i:i+2] for i in range(0, len(lines)-1, 2)]
    return [(parse_newick(p[0]), p[1].split()) for p in pairs]


def problem(tree, ks):
    tree, labels = tree
    kx = labels[ks[0]]
    ky = labels[ks[1]]
    kx_depths = dict(kx.ancestors())
    ky_depths = dict(ky.ancestors())
    common = set([x[0] for x in kx.ancestors()]) & set([y[0] for y in ky.ancestors()])
    best = sorted(common, key=lambda k: kx_depths[k] + ky_depths[k])[0]
    return kx_depths[best] + ky_depths[best]


def format(results):
    print ' '.join(map(str, results))


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/data.txt").read()
    dataset = parse(dataset)
    format(problem(t, k) for t, k in dataset)
