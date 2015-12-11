#!/usr/bin/env python3

import sys

csv_input_file = open(sys.argv[1], 'r')
bed_output_file = open(sys.argv[2], 'w')
fasta_output_file = open(sys.argv[3], 'w')
all_output_file = open(sys.argv[4], 'w')

for line in csv_input_file:
    line = line.rstrip()
    data = line.split(',')
    if data[0] == 'Chromosome':
        continue
    chrom = data[0]
    st = data[2]
    ed = data[3]
    strand = data[1]
    name = data[4]
    score = '0'
    seq = data[5]
    print(chrom,st,ed,name,score,strand, sep="\t",end="\n",file=bed_output_file)
    print(chrom,st,ed,name,score,strand,seq, sep="\t",end="\n",file=all_output_file)
    print('>',name, sep="",end="\n",file=fasta_output_file)
    print(seq, sep="\t",end="\n",file=fasta_output_file)
