#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'gr_id':
        print(line, sep="\t",end="\n",file=output_file)
        continue
    if data[6] == 'NA':
        print(line, sep="\t",end="\n",file=output_file)
        continue

    start_site = data[4].split('|')
    miRNA = data[5].split('|')
    miRNA_symbol = data[6].split('|')
    miR_seq = data[7].split('|')
    miR_ID = data[8].split('|')
    miR_count = data[9].split('|')

    start_site_list = []
    miRNA_list = []
    miRNA_symbol_list = []
    miR_seq_list = []
    miR_ID_list = []
    miR_count_list = []
    for index in range(len(miR_count)):
        start_site_s = start_site[index]
        miRNA_s = miRNA[index]
        miRNA_symbol_s = miRNA_symbol[index]
        miR_seq_s = miR_seq[index]
        miR_ID_s = miR_ID[index]
        miR_count_s = miR_count[index]
        if not miR_count_s == '':
            miR_count_each = miR_count_s.split('/')
            miR_count_each = map(int, miR_count_each)
            test_sum = sum(miR_count_each)

            if test_sum >= 5:
                start_site_list.append(start_site_s)
                miRNA_list.append(miRNA_s)
                miRNA_symbol_list.append(miRNA_symbol_s)
                miR_seq_list.append(miR_seq_s)
                miR_ID_list.append(miR_ID_s)
                miR_count_list.append(miR_count_s)
        else:
            pass

    start_site_line = '|'.join(start_site_list)
    miRNA_line = '|'.join(miRNA_list)
    miRNA_symbol_line = '|'.join(miRNA_symbol_list)
    miR_seq_line = '|'.join(miR_seq_list)
    miR_ID_line = '|'.join(miR_ID_list)
    miR_count_line = '|'.join(miR_count_list)
    number = len(miR_count_list)

    if miR_count_line != '':
        print("\t".join(data[0:3]),number,start_site_line,miRNA_line,miRNA_symbol_line,miR_seq_line,miR_ID_line,miR_count_line,sep="\t",end="\n",file=output_file)
    else:
        print("\t".join(data[0:3]),"0","NA","NA","NA","NA","NA","NA",sep="\t",end="\n",file=output_file)
