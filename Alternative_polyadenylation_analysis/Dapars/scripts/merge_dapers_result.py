#!/usr/bin/env python3

import sys

dapars_file = open(sys.argv[1], 'r')
gr_id_file = open(sys.argv[2], 'r')
output_file = open(sys.argv[3], 'w')

dapars_dict = {}
header = ''
col_number = 0

for line in dapars_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'Gene':
        header = "\t".join(data[1:])
        col_number = len(data[1:])
        continue
    symbol = data[0].split('|')[1]
    infor = "\t".join(data[1:])
    dapars_dict[symbol] = infor

for line in gr_id_file:
    line = line.rstrip()
    data = line.split("\t")
    symbol = data[1]
    if data[0] == 'gr_id':
        print(line, header, sep="\t",end="\n",file=output_file)
        continue
    if symbol in dapars_dict:
        infor = dapars_dict[symbol]
        print(line, infor, sep="\t",end="\n",file=output_file)
    else:
        print(line, "\t".join(['NA']*col_number), sep="\t",end="\n",file=output_file)
