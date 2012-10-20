from collections import Counter


def problem(dataset=None):
    """
    A string is simply an ordered collection of symbols selected from some
    alphabet and formed into a word; the length of a string is the number of
    symbols that it contains.

    An example of a DNA string (whose alphabet contains the symbols A, C, G,
    and T) is "ATGCTTCAGAAAGGTCTTACG".

    Given: A DNA string s of length at most 1000 nt.

    Return: Four integers separated by space corresponding to the number of
    times that the symbols A, C, G, and T occur in s.

    """
    freq = Counter()
    if not dataset:
        dataset = open("datasets/rosalind_dna.txt").read()
    for acid in dataset:
        freq.update([acid])
    return "%(A)s %(C)s %(G)s %(T)s" % freq


if __name__ == '__main__':
    print problem()
