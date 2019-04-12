#!/usr/bin/env python3
from Bio import SeqIO
import argparse

def main():
    parser = argparse.ArgumentParser(description='Extract gene or annotation from genbank file')
    parser.add_argument('gbk_file', help='Genbank file to read from')
    parser.add_argument('gene_name', help='Gene name')
    args = parser.parse_args()

    for record in SeqIO.parse(args.gbk_file, "genbank"):
        for f in record.features:
            if f.type == "CDS" and "gene" in f.qualifiers:
                gene = f.qualifiers["gene"][0]
                gene_seq = f.extract(record.seq)
                if gene in args.gene_name:
                    out1 = '>' + f.qualifiers["gene"][0] + "\n"
                    print(out1)
                    print(gene_seq)

if __name__ == "__main__":
    main()
