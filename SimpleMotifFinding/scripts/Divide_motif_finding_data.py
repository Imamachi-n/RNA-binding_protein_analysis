#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')
motif_length = int(sys.argv[3])

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    refid = data[0]
    st_site = data[1].split(',')
    if refid == 'refid':
        continue
    if st_site[0] == 'NA':
        print(refid, data[1], data[1], sep="\t", end="\n", file=output_file)
        continue
    for index in st_site:
        st = int(index)
        ed = st + motif_length
        print(refid, st, ed, sep="\t", end="\n", file=output_file)
