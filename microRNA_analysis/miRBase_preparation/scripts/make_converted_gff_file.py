#!/usr/bin/env python3

import sys
import re

input_file = open(sys.argv[1], 'r')
error_file = open(sys.argv[2], 'r')
output_file = open(sys.argv[3], 'w')

error_dict = {}

#ID=MI0026420;Alias=MI0026420;Name=hsa-mir-6859-2
regex_1 = r'ID=(?P<ID>.+);Alias=(?P<Alias>.+);Name=(?P<Name>.+)'
#ID=MIMAT0027619_1;Alias=MIMAT0027619;Name=hsa-miR-6859-3p;Derives_from=MI0026420
regex_2 = r'ID=(?P<ID>.+);Alias=(?P<Alias>.+);Name=(?P<Name>.+);Derives_from=(?P<Derives_from>.+)'
#decoded_seq = re.match(regex_1, 'ID=MI0026420;Alias=MI0026420;Name=hsa-mir-6859-2')    
#ID = decoded_seq.group('ID')
#Alias = decoded_seq.group('Alias')
#Name = decoded_seq.group('Name')

for line in error_file:
    line = line.rstrip()
    if re.match('^#', line):
        continue
    data = line.split("\t")
    
    infor = data[3].split('|')
    miRNA_type = infor[2]

    if miRNA_type == 'miRNA_primary_transcript':
        decoded_seq = re.match(regex_1, infor[8])
        ID = decoded_seq.group('ID')
        error_dict[ID] = 'NG'
    elif miRNA_type == 'miRNA':
        decoded_seq = re.match(regex_2, infor[8])
        ID = decoded_seq.group('Derives_from')
        error_dict[ID] = 'NG'
    else:
        print('ERROR: ',data[3], end="\n")

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    chrom = data[0]
    st = data[1]
    ed = data[2]
    infor = data[3].split('|')
    miRNA_type = infor[2]

    if miRNA_type == 'miRNA_primary_transcript':
        decoded_seq = re.match(regex_1, infor[8])
        ID = decoded_seq.group('ID')
        if ID in error_dict:
            continue
        else:
            print(chrom,infor[1],infor[2],st,ed,"\t".join(infor[5:]), sep="\t", end="\n", file=output_file)
    elif miRNA_type == 'miRNA':
        decoded_seq = re.match(regex_2, infor[8])
        ID = decoded_seq.group('Derives_from')
        if ID in error_dict:
            continue
        else:
            print(chrom,infor[1],infor[2],st,ed,"\t".join(infor[5:]), sep="\t", end="\n", file=output_file)
    else:
        print('ERROR: ',data[3], end="\n")
