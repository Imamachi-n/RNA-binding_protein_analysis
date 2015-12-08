#!/usr/bin/env python3

import sys
import re

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

for line in input_file:
    line = line.rstrip()
    if re.match('^#', line):
        continue
    data = line.split("\t")
    chrom = data[0]
    st = data[3]
    ed = data[4]
    infor = data[8]
    print(chrom,st,ed,'|'.join(data), sep="\t", end="\n", file=output_file)
