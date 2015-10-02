#!/usr/bin/env python3
 
#Usage: DNA2RNA_for_fasta.py <input_file> <output_file>

import sys

def load_fasta(fasta_path):
    fasta_file = open(fasta_path,'r')
    fasta_dict = {}
    name = ''
    for line in fasta_file:
        line = line.rstrip()
        if line.startswith('#'):
            continue
        if line.startswith('>'):
            name = line[1:].strip()
            fasta_dict[name] = ''
        else:
            trans_table = str.maketrans("ATGCatgcUu","AUGCAUGCUU")
            line_changed = line.translate(trans_table) #Translate DNA into RNA
            fasta_dict[name] += line_changed.upper()
    fasta_file.close()
    return fasta_dict

input_file = load_fasta(sys.argv[1])
output_file = open(sys.argv[2],'w')

for key in input_file.keys():
    seq = input_file[key]
    print('>',key,sep='',end="\n",file=output_file)
    print(seq,end="\n",file=output_file)
