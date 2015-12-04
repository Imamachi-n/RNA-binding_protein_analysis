#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r') #BED file
rep_isoform_file = open(sys.argv[2], 'r')
output_file = open(sys.argv[3], 'w')

ref_dict = {}

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    refid = data[3]
    exon_length_block = data[10].split(',')
    exon_length_block.pop()
    exon_length = 0
    for x in exon_length_block:
        exon_length += int(x)
    ref_dict[refid] = exon_length

print('gr_id','symbol','refid','3UTR length', sep="\t", end="\n", file=output_file)

for line in rep_isoform_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'gr_id':
        continue
    refid = data[2]
    if refid in ref_dict:
        exon_length = ref_dict[refid]
        print(line,exon_length, sep="\t", end="\n", file=output_file)
    else:
        print(line,'0', sep="\t", end="\n", file=output_file)
