#!/usr/bin/env python3

import sys
import re

miR_family_info = open(sys.argv[1], 'r')
HTSeq_output = open(sys.argv[2], 'r')
miRNA_position = open(sys.argv[3], 'r')
output_file = open(sys.argv[4], 'w')

miR_family_info_dict = {}

for line in miR_family_info:
    line = line.rstrip()
    data = line.split("\t")
    species = data[2]
    if species != '9606':
        continue
    miR_family = data[0]
    symbol = data[3]
    seq = data[4]
    miR_ID = ''
    if not len(data) == 7:
        miR_ID = 'NA'
    else:
        miR_ID = data[6]

    infor = symbol + '|' + seq + '|' + miR_ID
    if not miR_family in miR_family_info_dict:
        miR_family_info_dict[miR_family] = [infor]
    else:
        miR_family_info_dict[miR_family].append(infor)

HTSeq_dict = {}

for line in HTSeq_output:
    line = line.rstrip()
    data = line.split("\t")
    if re.match('^__', line):
        continue
    symbol = data[0]
    expression = data[1]
    HTSeq_dict[symbol] = expression

for line in miRNA_position:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == 'gr_id':
        print(line,"miR_symbol","miR_seq","miR_ID","miR_count", sep="\t",end="\n",file=output_file)
        continue
    miR_list = data[5].split('|')
    if miR_list[0] == 'NA':
        print(line,"NA","NA","NA","NA",sep="\t",end="\n",file=output_file)
        continue

    trx_miR_symbol = []
    trx_miR_seq = []
    trx_miR_miR_ID = []
    trx_miR_exp = []
    for miR_list_index in range(len(miR_list)):
        miR_family = miR_list[miR_list_index]
        if miR_family in miR_family_info_dict:
            infor = miR_family_info_dict[miR_family]

            miR_family_symbol = []
            miR_family_seq = []
            miR_family_miR_ID = []
            miR_family_exp = []
            for infor_index in range(len(infor)):
                each_miR_family_infor = infor[infor_index].split('|')
                symbol = each_miR_family_infor[0]
                seq = each_miR_family_infor[1]
                miR_ID = each_miR_family_infor[2]

                if symbol in HTSeq_dict:
                    expression = HTSeq_dict[symbol]

                    miR_family_symbol.extend([str(symbol)])
                    miR_family_seq.extend([str(seq)])
                    miR_family_miR_ID.extend([str(miR_ID)])
                    miR_family_exp.extend([str(expression)])
                else:
                    #print('ERROR_HTSeq_OUTPUT: ',symbol)
                    pass

            #test_list = list(map(int,miR_family_exp))
            #total_count = sum(test_list)

            #if total_count >= 5:
            miR_family_symbol_line = '/'.join(miR_family_symbol)
            miR_family_seq_line = '/'.join(miR_family_seq)
            miR_family_miR_ID_line = '/'.join(miR_family_miR_ID)
            miR_family_exp_line = '/'.join(miR_family_exp)
        else:
            #print('ERROR_TS_MIR_FAMILY: ',miR_family)
            pass

        #if miR_family_symbol_line != '':
        trx_miR_symbol.extend([miR_family_symbol_line])
        trx_miR_seq.extend([miR_family_seq_line])
        trx_miR_miR_ID.extend([miR_family_miR_ID_line])
        trx_miR_exp.extend([miR_family_exp_line])

    trx_miR_symbol_line = '|'.join(trx_miR_symbol)
    trx_miR_seq = '|'.join(trx_miR_seq)
    trx_miR_miR_ID = '|'.join(trx_miR_miR_ID)
    trx_miR_exp = '|'.join(trx_miR_exp)

    if trx_miR_symbol_line != '':
        print(line,trx_miR_symbol_line,trx_miR_seq,trx_miR_miR_ID,trx_miR_exp, sep="\t",end="\n",file=output_file)
    else:
        print(line,"NA","NA","NA","NA", sep="\t",end="\n",file=output_file)
