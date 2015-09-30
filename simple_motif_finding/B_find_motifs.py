#!/usr/bin/env python3

import re
import sys

PATH_REF_FILE = sys.argv[1]
PATH_INPUT_FILE = sys.argv[2]
PATH_OUTPUT_FILE = sys.argv[3]
MOTIFS = sys.argv[4]

def load_fasta(fasta_path):
    fasta_file = open(fasta_path,'r')
    fasta_dict = {}
    checker = []
    name = ''
    for line in fasta_file:
        line = line.rstrip()
        if line.startswith('#'):
            continue
        if line.startswith('>'):
            name = line[1:].strip()
            if not name in checker:
                checker.append(name)
            else:
                print ('ERROR: The same name exists =>' + name)
                sys.exit(1)
                continue
            fasta_dict[name] = ''
        else:
            trans_table = str.maketrans("ATGCatgcUu","ATGCATGCTT")
            line_changed = line.translate(trans_table) #Translate DNA into RNA
            fasta_dict[name] += line_changed.upper()
    fasta_file.close()
    return fasta_dict

sequence_data = load_fasta(PATH_REF_FILE)

input_file = open(PATH_INPUT_FILE,'r')
output_file = open(PATH_OUTPUT_FILE,'w')
error_log = open('./error.log','w')

motif_list = MOTIFS.split(',')

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'RESULT_FILE':
        print(line,'length','motifs',sep="\t",end="\n",file=output_file)
        continue
    acc_id = data[2]
    motif_count = 0
    if re.search('_[0-9]',acc_id):
        acc_id = re.sub('_[0-9]$','',acc_id)
    if acc_id in sequence_data:
        seq = sequence_data[acc_id]
        seq_length = len(seq)
        motif_length = len(motif_list[0])
        for i in range(0,seq_length-motif_length):
            test_seq = seq[i:i+motif_length]
            for motif_seq in motif_list:
                #print(motif_seq,test_seq)
                if motif_seq == test_seq:
                    motif_count += 1
                    continue
        print(line,seq_length,motif_count,sep="\t",end="\n",file=output_file)
    else:
        print("ERROR: ",acc_id," does not exist in fasta file...",file=error_log)
        continue


input_file.close()
output_file.close()
