#!/usr/bin/env python3

import sys
import shelve

output_s = sys.argv[1] + '_conservation.bed'
output_file = open(output_s, 'w')

for index in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,'X','Y']:
    ref_s = sys.argv[1] + '.bed'
    ref_file = open(ref_s, 'r')

    input_s = 'chr' + str(index) + '.phastCons46way_' + sys.argv[2] +  '.bed.db'

    input_phastcons_file = shelve.open(input_s)

    for line in ref_file:
        line = line.rstrip()
        data = line.split("\t")

        chrom = data[0]
        chrom_file = 'chr' + str(index)
        if chrom_file != chrom:
            continue

        st = int(data[1])
        ed = int(data[2])
        name = data[3]

        exon_length_block = data[10].split(",")
        if exon_length_block[-1] == '':
            exon_length_block.pop()
        exon_length_block = list(map(int,exon_length_block))

        exon_start_block = data[11].split(",")
        if exon_start_block[-1] == '':
            exon_start_block.pop()
        exon_start_block = list(map(int,exon_start_block))

        index_list = []
        for x in range(len(exon_length_block)):
            for number in range(exon_length_block[x]):
                st_index = st + 1 + exon_start_block[x] + number
                index_list.append(st_index)
        index_list = list(map(str,index_list))

        index_score = []
        for x in index_list:
            if x in input_phastcons_file:
                cons_score = input_phastcons_file[x]
                index_score.append(cons_score)
            else:
                printout = "WARNINGS: " + data[3] + " - " + str(x)
                print(printout)
                index_score.append('0')
        index_score = list(map(float,index_score))

        index_score_mean = sum(index_score)/len(index_score)

        print(line,index_score_mean, sep="\t", end="\n", file=output_file)

output_file.close()
