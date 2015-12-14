#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    st = data[1]
    ed = data[2]
    length = int(ed) - int(st)
    print(line,ed,ed,'0','1',str(length),'0', sep="\t",end="\n",file=output_file)
