#!/usr/bin/env python3

import sys

rep_isoform_file = open(sys.argv[1], 'r')
input_file = open(sys.argv[2], 'r')
output_file = open(sys.argv[3], 'w')

ref_dict = {}

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    refid_list = data[0].split('|')
    st = data[1]
    ed = data[2]
    if st == 'NA':
        continue
    for refid in refid_list:
        if not refid in ref_dict:
            ref_dict[refid] = [st]
        else:
            ref_dict[refid].append(st)

print('gr_id','symbol','refid','PUM_motifs #','start_site', sep="\t", end="\n", file=output_file)


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
        st_number = len(st_list)
        st = '|'.join(ref_dict[refid])
        print(gr_id,symbol,refid,st_number,st, sep="\t", end="\n", file=output_file)
    else:
        print(gr_id,symbol,refid,"0",'NA', sep="\t", end="\n", file=output_file)
