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
    st = data[2]
    ed = data[3]
    cons_score = data[4]
    infor = st + '||' + cons_score
    if st == 'NA':
        continue
    for refid in refid_list:
        if not refid in ref_dict:
            ref_dict[refid] = [infor]
        else:
            ref_dict[refid].append(infor)

print('gr_id','symbol','refid','miRNA-binding sites #','start_site','Conservation_score', sep="\t", end="\n", file=output_file)

for line in rep_isoform_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'gr_id':
        continue
    gr_id = data[0]
    symbol = data[1]
    refid = data[2]
    if refid in ref_dict:
        infor = ref_dict[refid]
        number = len(infor)
        st_list = []
        cons_list = []
        for index in range(len(infor)):
            infor_list = infor[index].split('||')
            st_list.append(str(infor_list[0]))
            cons_list.append(str(infor_list[1]))
        st_line = '|'.join(st_list)
        cons_line = '|'.join(cons_list)
        print(gr_id,symbol,refid,number,st_line,cons_line, sep="\t", end="\n", file=output_file)
    else:
        print(gr_id,symbol,refid,"0",'NA','NA', sep="\t", end="\n", file=output_file)
