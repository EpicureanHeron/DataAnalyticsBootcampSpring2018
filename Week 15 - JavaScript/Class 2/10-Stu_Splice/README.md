# DNA Splice

## Instructions

* In strands of human DNA, **exons** are DNA sequences that code for proteins. **Introns**, on the other hand, are DNA sequences that do not code for any proteins.

* Introns are represented by a sequence of the letters A, C, G, and T, the four nitrogenous bases.

* In this activity, exons are represented by the string "_." Your task is to remove all instances of "_" from the DNA.

* Hint: You may wish to use the `split` and `join` methods.


## BONUS

* Calculate the reverse complement for a DNA sequence. DNA sequences are comprised of the Nucleobases A, T, C, G. The reverse complement will convert A to T, T to A, C to G, and G to C for the original sequence. For example, `AATC` has the reverse complement `TTAG`.

## Ultimate Challenge

* Use the codons map to convert the DNA sequence to proteins. Note that 3 amino acids make up one codon `GCT`. You can then use the `codons_map` object to map each codon to a protein. For example, `GCT` becomes `A`.

* Hint: Try using `splice` to get 3 amino acid values at a time.
