#!/usr/bin/env python3

import sys
import re


input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

test_dir = {}

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    infor = data[8].split(';')
    if infor[-1] == '':
        infor.pop()
    refid = ''
    symbol = ''
    if len(infor) == 4:
        symbol_infor = infor[1].replace(' gene_name "','')
        symbol_infor = symbol_infor.replace('"','')
        symbol = symbol_infor
        refid_infor = infor[2].replace(' transcript_id "','')
        refid_infor = refid_infor.replace('"','')
        refid = refid_infor
    elif len(infor) == 5:
        symbol_infor = infor[1].replace(' gene_name "','')
        symbol_infor = symbol_infor.replace('"','')
        symbol = symbol_infor
        refid_infor = infor[3].replace(' transcript_id "','')
        refid_infor = refid_infor.replace('"','')
        refid = refid_infor
    test_dir[refid] = symbol

for index in test_dir.keys():
    refid = index
    symbol = test_dir[refid]
    print(refid, symbol, sep="\t",end="\n",file=output_file)

