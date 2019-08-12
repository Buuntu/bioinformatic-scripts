#!/usr/bin/env python3
# Author: Gabriel Abud
# Script will take two genbank files and concatenate the features. It will also add
# genbank qualifers to distinguish the features (like from two different annotation
# tools).
# It will set each contig name and description based on the first file given (-f)

import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser()
parser.add_argument("-f", description="First genbank file", help="First genbank file")
parser.add_argument("-F", help="Second genbank file")
parser.add_argument("-p", help="Qualifier for features in first genbank file")
parser.add_argument("-P", help="Qualifier for features in second genbank file")
parser.add_argument("-o", help="Merged genbank file")
args = parser.parse_args()

file_a = SeqIO.parse(args.f, "genbank")
file_b = SeqIO.parse(args.F, "genbank")

# Create a record
records = []

# Loop through records and assign qualifiers to features
for contig_a, contig_b in zip(file_a, file_b):
    total_features = []
    record = SeqRecord(contig_a.seq,
                       name=contig_a.name,
                       description=contig_a.description)
    for feature in contig_a.features:
        feature.qualifiers['annotation-type'] = args.p 

    for feature in contig_b.features:
        feature.qualifiers['annotation-type'] = args.P

    total_features = contig_a.features + contig_b.features
    record.features = total_features
    records.append(record)
    
# Save as GenBank file
output_file = open(args.o, 'w')
SeqIO.write(records, output_file, 'genbank')
