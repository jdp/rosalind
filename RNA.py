def problem(dataset=None):
    """
    An RNA string is formed from the alphabet containing A, C, G, and U.

    Given a DNA string t corresponding to a coding strand, its transcribed RNA
    string u is formed by replacing all occurrences of T with U.

    Given: A DNA string t of length at most 1000 nucleotides.

    Return: The transcribed RNA string of t.

    """
    if not dataset:
        dataset = open("datasets/rosalind_rna.txt").read()
    return dataset.replace('T', 'U')

if __name__ == '__main__':
    print problem()
