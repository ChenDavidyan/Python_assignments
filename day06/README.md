# Day06

Over 170 chemical modifications in RNA post-transcription have been identified across diverse RNA types and all four RNA bases. Many of these modifications play an essential role in various biological processes. Among them, N6-methyladenosine (m6A) is the most abundant internal mRNA modification and plays diverse roles in RNA regulation.


The file modifications.csv represents a comparative analysis of m6A modification sites identified by five distinct detection methods:

* DART-seq
* GLORI
* M6A-CLIP
* M6A-REF-seq
* miCLIP

The script modified_position.py calculates the sum of modifications at each genomic locus and prints the loci that were found in the most methods.