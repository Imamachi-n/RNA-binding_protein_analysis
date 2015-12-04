#!/usr/bin/env python3

import re
import sys

input_file = sys.argv[1] #$Refseq_mRNA_3UTR.fa
motif_list = sys.argv[2] #TGTAAATA,TGTATATA,TGTAGATA,TGTACATA
output_file = open(sys.argv[3], 'w')

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
            trans_table = str.maketrans("ATGCatgcUu","AUGCAUGCUU")
            line_changed = line.translate(trans_table) #Translate DNA into RNA
            fasta_dict[name] += line_changed.upper()
    fasta_file.close()
    return fasta_dict

input_dict = load_fasta(input_file)
trans_table = str.maketrans("ATGCatgcUu","AUGCAUGCUU")
motif_list = motif_list.translate(trans_table)
motif_list = motif_list.split(',')

print("refid","motif_start_site",sep="\t",end="\n",file=output_file)

for name in input_dict.keys():
    seq = input_dict[name]
    #print(seq)
    st_site = []
    test = []
    for motif in motif_list:
        match_seq = re.finditer(motif, seq)
        
        if match_seq:
            test = [x.start() for x in match_seq]
            #print(test)
            if test:
                st_site.extend(test)
        else:
            print("Empty!!")
    if st_site:
        st_site = map(str, st_site)
        print(name,",".join(st_site), sep="\t", end="\n", file=output_file)
    else:
        print(name,"NA", sep="\t", end="\n", file=output_file)