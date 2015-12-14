#!/usr/bin/env python3

import re
import sys

PATH_REF_FILE = sys.argv[1]
PATH_INPUT_FILE = sys.argv[2]
PATH_OUTPUT_FILE = sys.argv[3]

#ref_file = open('/mnt/hgfs/github/HuR_study/2015-08-17_define_Representative_isoform_from_RNA-seq/raw_data/isoform_exp.diff','r')
ref_file = open(PATH_REF_FILE,'r')

ref_dict = {}

for line in ref_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'test_id':
        continue
    refid = data[0]
    symbol = data[1]
    RPKM_kd = data[8]
    if not symbol in ref_dict:
        ref_dict[symbol] = [[refid,float(RPKM_kd)]]
    else:
        ref_dict[symbol].append([refid,float(RPKM_kd)])

ref_file.close()

#input_file = open('/mnt/hgfs/github/HuR_study/2015-08-17_define_Representative_isoform_from_RNA-seq/raw_data/gene_exp_RefSeq_result_mRNA.diff','r')
#output_file = open('/mnt/hgfs/github/HuR_study/2015-08-17_define_Representative_isoform_from_RNA-seq/result/gene_exp_RefSeq_result_mRNA_rep_isoform_list.txt','w')
input_file = open(PATH_INPUT_FILE,'r')
output_file = open(PATH_OUTPUT_FILE,'w')

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'gr_id':
        print(data[0],data[1],'refid_representative',sep="\t",end="\n",file=output_file)
        continue
    gr_id = data[0]
    symbol = data[1]
    RPKM_list = ref_dict[symbol]
    RPKM_dict = {x: y for x, y in RPKM_list if not re.match('^NR',x)}
    #print(gr_id,RPKM_dict)
    RPKM_list_sorted = sorted(RPKM_dict.items(),key=lambda x:float(x[1]),reverse=True)
    rep_refid = ''
    if RPKM_list_sorted:
        rep_refid = RPKM_list_sorted[0][0]
    else:
        rep_refid = 'NA'
    print(gr_id,symbol,rep_refid,sep="\t",end="\n",file=output_file)

input_file.close()
output_file.close()
