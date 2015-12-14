#!/usr/bin/env python3

import sys

clip_seq_pos = open(sys.argv[1], 'r')
cluster_result = open(sys.argv[2], 'r')
rep_infor = open(sys.argv[3], 'r')

output_file = open(sys.argv[4], 'w')
fasta_file = open(sys.argv[5], 'w')

seq_dict = {}

for line in cluster_result:
    line = line.rstrip()
    data = line.split("\t")
    seq = data[6]
    name = data[3]
    seq_dict[name] = seq

clip_dict = {}

for line in clip_seq_pos:
    line = line.rstrip()
    data = line.split("\t")
    refid = data[0]
    name = data[1]
    st = data[2]
    if int(st) < 0:
        continue
    seq = seq_dict[name]
    infor = st + '|' + seq
    if not refid in clip_dict:
        clip_dict[refid] = [infor]
    else:
        clip_dict[refid].append(infor)

for line in rep_infor:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'gr_id':
        print(line,'st_site','seq','motif #', sep="\t",end="\n",file=output_file)
        continue
    refid = data[2]
    if refid in clip_dict:
        infor = clip_dict[refid]
        st_infor = [str(x.split('|')[0]) for x in infor]
        st_line = '|'.join(st_infor)
        seq_infor = [str(x.split('|')[1]) for x in infor]
        seq_line = '|'.join(seq_infor)
        motif_num = len(infor)
        print(line,st_line,seq_line,motif_num, sep="\t", end="\n", file=output_file)

        for index in range(len(st_infor)):
            st_index = st_infor[index]
            name_index = data[1] + '|' + refid + '|' + str(st_index)
            seq_index = seq_infor[index]
            print('>',name_index, sep="",end="\n",file=fasta_file)
            print(seq_index, sep="\t",end="\n",file=fasta_file)
        continue
    else:
        print(line,'NA','NA','NA', sep="\t",end="\n",file=output_file)
