def problem(dataset=None):
    """
    Given two strings s and t of equal length, the Hamming distance between s
    and t, denoted dH(s,t), is the number of corresponding symbols that differ
    in s and t. See Figure 2.

    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

    Return: The Hamming distance dH(s,t).

    """
    if not dataset:
        dataset = open("datasets/rosalind_hamm.txt").read()
    s, t = dataset.strip().splitlines()
    return len(filter(lambda pair: pair[0] != pair[1], zip(s, t)))


if __name__ == '__main__':
    print problem()
