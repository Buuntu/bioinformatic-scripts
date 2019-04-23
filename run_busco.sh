#!/bin/bash

# Run docker container with busco
# Getting all the dependencies for BUSCO installed is a hassle and takes way longer than it should, so I found a Docker image that does it for you

input_fasta_file=$1
output_directory=$2
lineage=$3 

docker container run -d -v $(pwd):/data --name ${output_directory} vera/busco -i ${input_fasta_file} -o ${output_directory} -l ${lineage} -m genome


