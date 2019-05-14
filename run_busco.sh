#!/bin/bash

# Run docker container with busco on whole genome assemblies
# Getting all the dependencies for BUSCO installed is a hassle and takes way longer than it should, so I found a Docker image that does it for you
# Assumes your fasta file and the lineage folder downloaded from BUSCO are in the current directory

function display_format {
    echo "Usage: run_busco.sh -f [input fasta file] -o [output directory] -l [lineage] -m [transcriptome|genome]"
    exit 1
}

while getopts ":f:o:l:m:" opt; do
  case ${opt} in
    f ) # process option f
        input_fasta_file=${OPTARG}
        ;;
    o ) # process option o
        output_directory=${OPTARG}
        ;;
    l ) # process option l
        lineage=${OPTARG}
        ;;
    m ) # process option m
        mode=${OPTARG}
        ;;
    \? ) display_format
        ;;
  esac
done

shift $((OPTIND-1))

if [ -z ${input_fasta_file} ] || [ -z ${output_directory} ] || [ -z ${lineage} ] || [ -z ${mode} ]; then
    display_format
fi

docker container run -d -v $(pwd):/data vera/busco -i ${input_fasta_file} -o ${output_directory} -l ${lineage} -m ${mode} 


