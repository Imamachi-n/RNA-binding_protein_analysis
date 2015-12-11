#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[6] == '.':
        continue
    name = '|'.join([data[0],data[1],data[2]])
    seq = data[9]
    print('>',name, sep="",end="\n",file=output_file)
    print(seq, sep="\t",end="\n",file=output_file)
