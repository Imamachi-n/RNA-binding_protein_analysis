#!/usr/bin/erv python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

ref_dict = {}
data_dict = {}

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    chrom = data[0]
    st = data[1]
    ed = data[2]
    exon_size_block = data[10]
    exon_st_block = data[11]
    infor = chrom + '|' + st + '|' + ed + '|' + exon_size_block + '|' + exon_size_block
    refid = data[3]
    if not infor in ref_dict:
        ref_dict[infor] = [refid]
    else:
        ref_dict[infor].append(refid)
    data_dict[infor] = line

for infor in ref_dict.keys():
    refid_list = ref_dict[infor]
    refids = '|'.join(refid_list)
    all_data = data_dict[infor].split("\t")
    print("\t".join(all_data[0:3]),refids,"\t".join(all_data[4:]),sep="\t",end="\n",file=output_file)
