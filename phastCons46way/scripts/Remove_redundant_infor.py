#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

rep_dict = {}

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")

    name = data[3]

    chrom = data[12]
    st = data[13]
    ed = data[14]
    exon_length_block = data[22]
    exon_start_block = data[23]
    infor = name + '|' + chrom + '|' + st + '|' + ed + '|' + exon_length_block + '|' + exon_start_block
    
    if not infor in rep_dict:
        rep_dict[infor] = 1
        print(line, end="\n", file=output_file)
    else:
        pass