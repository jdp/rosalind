def problem(dataset=None):
    """
    The 20 commonly occurring amino acids are abbreviated by using the majority
    of symbols from the Roman alphabet (except for B, J, O, U, X, and Z).
    Protein strings are constructed from these 20 symbols. Henceforth, the
    term genetic string will incorporate protein strings with DNA strings and
    RNA strings.

    The RNA codon table dictates specific details regarding the encoding of
    specific codons into the amino acid alphabet.

    Given: An RNA string s corresponding to a strand of mRNA (of length at most
    10 kbp).

    Return: The protein string encoded by s.

    """
    if not dataset:
        dataset = open("datasets/rosalind_prot.txt").read()
    mapping = {}
    with open("codons.txt") as f:
        for line in f:
            if not line.strip():
                continue
            codon, acid = line.strip().split()
            if acid == 'Stop':
                mapping[codon] = None
            else:
                mapping[codon] = acid
    codons = [dataset[i:i + 3] for i in range(0, len(dataset), 3)]
    translated = ""
    for codon in codons:
        acid = mapping[codon]
        if not acid:
            break
        translated += acid
    return translated


if __name__ == '__main__':
    print problem()
