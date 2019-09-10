#!/usr/bin/env python3
"""
This will extract features from a gff+fasta file based on the type (such as cds, exon, gene).  It will output to STDOUT
"""

import gffutils
import pyfaidx
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", help="GFF3 file", required=True)
parser.add_argument("-f", help="Fasta file", required=True)
parser.add_argument("-F", help="Feature type [cds, exon, gene]", required=True)
args = parser.parse_args()

gff_file = args.g
fasta_file = args.f
feature_type = args.F

db = gffutils.create_db(gff_file, ':memory:')
fasta = pyfaidx.Fasta(fasta_file)

for feature in db.features_of_type(feature_type, order_by='start'):
    print(f">{feature.id}, {feature.seqid} {feature.start}-{feature.end}[{feature.strand}]")
    print(feature.sequence(fasta))
