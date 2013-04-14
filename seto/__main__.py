"""
Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are
taken with respect to {1,2,…,n}).

>>> r = problem(10, {1, 2, 3, 4, 5}, {2, 8, 5, 10})
>>> format(r)
{1, 2, 3, 4, 5, 8, 10}
{2, 5}
{1, 3, 4}
{8, 10}
{8, 9, 10, 6, 7}
{1, 3, 4, 6, 7, 9}
"""


def problem(n, a, b):
    return [
        a | b,
        a & b,
        a - b,
        b - a,
        set(range(1, n + 1)) - a,
        set(range(1, n + 1)) - b
    ]


def format(result):
    for r in result:
        print "{" + ', '.join(map(str, r)) + "}"


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    def parse(line):
        return [s.strip() for s in line.strip()[1:-1].split(",")]

    n, a, b = open(dirname(__file__) + "/rosalind_seto.txt").readlines()
    n = int(n.strip())
    a = set(map(int, parse(a)))
    b = set(map(int, parse(b)))
    format(problem(n, a, b))
