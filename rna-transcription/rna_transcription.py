def to_rna(dna_strand):

    # dna = ["G", "C", "T", "A"]
    # rna = ["C", "G", "A", "U"]

    # res = ""
    # for i in dna_strand:
    #     if i in dna:
    #         idx = dna.index(i)
    #         res += rna[idx]
    # return res

    # return dna_strand.translate(str.maketrans("GCTA", "CGAU"))

    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}

    res = ""
    for i in dna_strand:
        res += dna_to_rna[i]

    return res
