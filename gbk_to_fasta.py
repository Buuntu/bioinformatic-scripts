#!/usr/bin/env python3
from Bio import SeqIO
import sys

gbk_filename = sys.argv[1]
fasta_filename = sys.argv[2]
input_handle  = open(gbk_filename, "r")
output_handle = open(fasta_filename, "w")

for seq_record in SeqIO.parse(input_handle, "genbank") :
    print("Dealing with GenBank record %s" % seq_record.id)
    output_handle.write(">%s %s\n%s\n" % (
           seq_record.id,
           seq_record.description,
           seq_record.seq))

output_handle.close()
input_handle.close()
