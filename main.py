def DNA_strand(dna):
    replacement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([replacement[ch] for ch in dna])


print(DNA_strand('ATTGC'))
