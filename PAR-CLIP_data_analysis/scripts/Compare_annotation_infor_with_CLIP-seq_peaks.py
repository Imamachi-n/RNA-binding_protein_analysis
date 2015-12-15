#!/usr/bin/env python3

import sys

clip_seq_pos = open(sys.argv[1], 'r') #${bowtiefile}_trx_sites.txt
cluster_result = open(sys.argv[2], 'r') #${bowtiefile}_clusters.result
rep_infor = open(sys.argv[3], 'r') #${CuffdiffGeneFilename}_rep_isoform_list.txt

output_file = open(sys.argv[4], 'w') #${bowtiefile}_trx_sites_for_NGS_dataset.txt
fasta_file = open(sys.argv[5], 'w') #${bowtiefile}_trx_sites_for_NGS_dataset.fasta
bed_file = open(sys.argv[6], 'w') #./${savedir}/${bowtiefile}_rep_trx_3UTR.bed

seq_dict = {}
seq_bed_dict = {}

for line in cluster_result:
    line = line.rstrip()
    data = line.split("\t")
    seq = data[6]
    name = data[3]
    seq_dict[name] = seq
    seq_bed_dict[name] = data[0:6]

clip_dict = {}
clip_bed_dict = {}

for line in clip_seq_pos:
    line = line.rstrip()
    data = line.split("\t")
    refid = data[0]
    name = data[1]
    st = data[2]
    if int(st) < 0:
        continue
    seq = seq_dict[name]
    seq_bed_infor = seq_bed_dict[name]
    infor = st + '|' + seq
    if not refid in clip_dict:
        clip_dict[refid] = [infor]
        clip_bed_dict[refid] = [seq_bed_infor]
    else:
        clip_dict[refid].append(infor)
        clip_bed_dict[refid].append(seq_bed_infor)

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

        bed_infor = clip_bed_dict[refid]

        for index in range(len(st_infor)):
            ###For fasta file###
            st_index = st_infor[index]
            name_index = data[1] + '|' + refid + '|' + str(st_index)
            seq_index = seq_infor[index]
            print('>',name_index, sep="",end="\n",file=fasta_file)
            print(seq_index, sep="\t",end="\n",file=fasta_file)

            ###For bed file###
            bed_index = bed_infor[index]
            print("\t".join(bed_index), sep="\t",end="\n",file=bed_file)
        continue
    else:
        print(line,'NA','NA','NA', sep="\t",end="\n",file=output_file)
