#!/bin/bash

# Run docker container with busco on whole genome assemblies
# Getting all the dependencies for BUSCO installed is a hassle and takes way longer than it should, so I found a Docker image that does it for you
# Assumes your fasta file and the lineage folder downloaded from BUSCO are in the current directory

input_fasta_file=$1
output_directory=$2
lineage=$3 

function display_format {
    echo "Usage: run_busco.sh [input fasta file] [output directory] [lineage]"
    exit 1
}

if [ -z ${input_fasta_file} ] || [ -z ${output_directory} ] || [ -z ${lineage} ]; then
    display_format
fi

docker container run -d -v $(pwd):/data --name ${output_directory} vera/busco -i ${input_fasta_file} -o ${output_directory} -l ${lineage} -m genome


