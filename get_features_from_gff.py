#!/usr/bin/env python3

import gffutils
import pyfaidx
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", help="GFF3 file", required=True)
parser.add_argument("-f", help="Fasta file", required=True)
parser.add_argument("-F", help="Feature type [cds, exon, gene]", required=True)
parser.add_argument("-o", help="Output file (or stdout if none)", required=False)
args = parser.parse_args()

gff_file = args.g
print(gff_file)
fasta_file = args.f
feature_type = args.F

db = gffutils.create_db(gff_file, ':memory:')
fasta = pyfaidx.Fasta(fasta_file)

for feature in db.features_of_type(feature_type, order_by='start'):
    breakpoint()
    print(f">{feature.id}, {feature.seqid} {feature.start}-{feature.end}[{feature.strand}]")
    print(feature.sequence(fasta))
