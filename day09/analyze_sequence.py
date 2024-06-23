import argparse
import re 
from Bio import SeqIO

def find_longest_duplicate(sequence):
    length = 1
    result = ''
    while True:
        regex = r'([GATC]{' + str(length) + r'}).*\1'
        match = re.search(regex, sequence)
        if match:
            result = match.group(1)
            length += 1
        else:
            break
    return result

def count_pam_sequences(sequence):
    pam_pattern = r'(?=(.{2}GG))'  # Lookahead to find overlapping NGG patterns
    matches = re.findall(pam_pattern, sequence)
    return len(matches)

def main():
    parser = argparse.ArgumentParser(description="Sequence Analysis Tool - find longest duplications and PAM sequences")
    parser.add_argument('--path', help="Path to FASTA/GeneBank file", required=True)
    parser.add_argument('--duplicate', '-dp', action="store_true", help="Find the longest duplicated sub-sequence")
    parser.add_argument('--pam', action="store_true", help="Find how many PAM sequences are in the sequence")
    args = parser.parse_args()
    
    if not args.duplicate and not args.pam:
        parser.error("Please choose: --duplicate or --pam")

    if args.path.endswith(".gb") or args.path.endswith(".gbk"):
        file_format = "genbank"
    elif args.path.endswith(".fasta") or args.path.endswith(".fa"):
        file_format = "fasta"
    else:
        raise ValueError("Unsupported file format. Please provide a FASTA or GeneBank file.")
    
    for sequence_record in SeqIO.parse(args.path, file_format):
        sequence = str(sequence_record.seq)
        if args.duplicate:
            longest_dup = find_longest_duplicate(sequence)
            print(f"Longest duplicate subsequence: {longest_dup}")
        
        if args.pam:
            pam_count = count_pam_sequences(sequence)
            print(f"Number of PAM sequences: {pam_count}")

if __name__ == "__main__":
    main()
