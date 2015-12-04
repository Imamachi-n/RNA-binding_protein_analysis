#!/usr/bin/env python3

import sys

rep_isoform_file = open(sys.argv[1], 'r')
input_file = open(sys.argv[2], 'r')
output_file = open(sys.argv[3], 'w')

ref_dict = {}
ref_dict_mir = {}

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    refid_list = data[0].split('|')
    miRNA_list = data[1].split(':')[1]
    st = data[2]
    ed = data[3]
    if st == 'NA':
        continue
    for refid in refid_list:
        if not refid in ref_dict:
            ref_dict[refid] = [st]
            ref_dict_mir[refid] = [miRNA_list]
        else:
            ref_dict[refid].append(st)
            ref_dict_mir[refid].append(miRNA_list)

print('gr_id','symbol','refid','miRNA-binding sites #','start_site','miRNA', sep="\t", end="\n", file=output_file)

for line in rep_isoform_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'gr_id':
        continue
    gr_id = data[0]
    symbol = data[1]
    refid = data[2]
    if refid in ref_dict:
        st_list = ref_dict[refid]
        miRNA_list = ref_dict_mir[refid]
        st_number = len(st_list)
        st = '|'.join(ref_dict[refid])
        miRNA = '|'.join(ref_dict_mir[refid])
        print(gr_id,symbol,refid,st_number,st,miRNA, sep="\t", end="\n", file=output_file)
    else:
        print(gr_id,symbol,refid,"0",'NA','NA', sep="\t", end="\n", file=output_file)
