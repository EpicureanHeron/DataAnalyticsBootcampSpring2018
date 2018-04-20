// remove the `_` from the string
var seq = "CGAT_TACG__AAATA_TATCA___TAATCATAA_TCATAATTATAC_ATACCACTCTTACTCTCA";
// YOUR CODE HERE




// BONUS
// calculate the reverse complement
var base_complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"}

// YOUR CODE HERE





// Ultimate Challenge
// loop through 3 items at a time and
// use the codon_map to convert
// to a protein
var codons_map = {
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TGT': 'C', 'TGC': 'C', 'GAT': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E', 'TTT': 'F', 'TTC': 'F',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        'CAT': 'H', 'CAC': 'H', 'ATT': 'I', 'ATC': 'I',
        'ATA': 'I', 'AAA': 'K', 'AAG': 'K', 'TTA': 'L',
        'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L',
        'CTG': 'L', 'ATG': 'M', 'AAT': 'N', 'AAC': 'N',
        'TAA': 'P', 'TAG': 'P', 'TGA': 'P', 'CCT': 'P',
        'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAA': 'Q',
        'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R',
        'CGG': 'R', 'AGA': 'R', 'AGG': 'R', 'TCT': 'S',
        'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S',
        'AGC': 'S', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T',
        'ACG': 'T', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V',
        'GTG': 'V', 'TGG': 'W', 'TAT': 'Y', 'TAC': 'Y'};

// YOUR CODE HERE
