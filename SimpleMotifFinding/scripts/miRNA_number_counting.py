#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')
total_count = int(sys.argv[3])

mir_dict = {}

for line in input_file:
    line = line.rstrip()
    data = line.split("|")
    miRNA_list = []
    
    for x in data:
        x = x.replace('miR-','')
        mir_data = x.split("/")
        miRNA_list.extend(mir_data)
    miRNA_list = list(set(miRNA_list))
    for x in miRNA_list:
        if x == 'NA':
            continue
        if not x in mir_dict:
            mir_dict[x] = 1
        else:
            mir_dict[x] += 1

for x in mir_dict.keys():
    miRNA_name = 'miR-' + x
    count = mir_dict[x]
    div = count / total_count
    print(miRNA_name,str(count),str(div),sep="\t",end="\n",file=output_file)
