#!/usr/bin/env python

"""Convert between sequence formats using Biopython's SeqIO.
Usage:
    seq_convert from_format to_format < infile > outfile
Valid sequence formats:
    ace     - Reads the contig sequences from an ACE assembly file.
    embl    - The EMBL flat file format. Uses Bio.GenBank internally.
    fasta   - The generic sequence file format where each record starts with
              an identifer line starting with a ">" character, followed by
              lines of sequence.
    fastq   - A "FASTA like" format used by Sanger which also stores PHRED
              sequence quality values (with an ASCII offset of 33).
    fastq-sanger - An alias for "fastq" for consistency with BioPerl and EMBOSS
    fastq-solexa - Original Solexa/Illumnia variant of the FASTQ format which
              encodes Solexa quality scores (not PHRED quality scores) with an
              ASCII offset of 64.
    fastq-illumina - Solexa/Illumnia 1.3+ variant of the FASTQ format which
              encodes PHRED quality scores with an ASCII offset of 64 (not 33).
    genbank - The GenBank or GenPept flat file format.
    gb      - An alias for "genbank", for consistency with NCBI Entrez Utilities
    ig      - The IntelliGenetics file format, apparently the same as the
              MASE alignment format.
    phd     - Output from PHRED, used by PHRAP and CONSED for input.
    pir     - A "FASTA like" format introduced by the National Biomedical
              Research Foundation (NBRF) for the Protein Information Resource
              (PIR) database, now part of UniProt.
    swiss   - Plain text Swiss-Prot aka UniProt format.
    tab     - Simple two column tab separated sequence files, where each
              line holds a record's identifier and sequence. For example,
              this is used as by Aligent's eArray software when saving
              microarray probes in a minimal tab delimited text file.
    qual    - A "FASTA like" format holding PHRED quality values from
               sequencing DNA, but no actual sequences (usually provided
               in separate FASTA files).
Alignment formats also allowed:
    clustal   - Ouput from Clustal W or X, see also the module Bio.Clustalw
                which can be used to run the command line tool from Biopython.
    emboss    - EMBOSS tools' "pairs" and "simple" alignment formats.
    fasta     - The generic sequence file format where each record starts with
                an identifer line starting with a ">" character, followed by
                lines of sequence.
    fasta-m10 - For the pairswise alignments output by Bill Pearson's FASTA
                tools when used with the -m 10 command line option for machine
                readable output.
    ig        - The IntelliGenetics file format, apparently the same as the
                MASE alignment format.
    nexus     - Output from NEXUS, see also the module Bio.Nexus which can also
                read any phylogenetic trees in these files.
    phylip    - Used by the PHLIP tools.
    stockholm - A richly annotated alignment file format used by PFAM.
"""
import os, sys
from Bio import SeqIO

if len(sys.argv) != 3:
    sys.exit(__doc__)

count = SeqIO.convert(sys.stdin, sys.argv[1], sys.stdout, sys.argv[2])
print("SeqIO: Converted %d sequences" % count, file=sys.stderr)
