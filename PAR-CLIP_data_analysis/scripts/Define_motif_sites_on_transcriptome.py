#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

counter_1_1 = 0
counter_2_1 = 0
counter_2_2 = 0
counter_1_1_real = 0
counter_2_1_real = 0
counter_2_2_real = 0

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    st_mRNA = int(data[1])
    ed_mRNA = int(data[2])
    st_miRNA = int(data[13])
    ed_miRNA = int(data[14])

    strand = data[5]
    mRNA_name = data[3]
    miRNA_name = data[15]
    rep_name = miRNA_name + '||' + mRNA_name

    exon_number_mRNA = int(data[9])
    exon_number_miRNA = int(data[21])

    exon_length_block_mRNA = data[10].split(',')
    if exon_length_block_mRNA[-1] == '':
        exon_length_block_mRNA.pop()
    exon_length_block_mRNA = list(map(int, exon_length_block_mRNA))
    exon_st_block_mRNA = data[11].split(',')
    if exon_st_block_mRNA[-1] == '':
        exon_st_block_mRNA.pop()
    exon_st_block_mRNA = list(map(int, exon_st_block_mRNA))

    exon_length_block_miRNA = data[22].split(',')
    if exon_length_block_miRNA[-1] == '':
        exon_length_block_miRNA.pop()
    exon_length_block_miRNA = list(map(int, exon_length_block_miRNA))
    exon_st_block_miRNA = data[23].split(',')
    if exon_st_block_miRNA[-1] == '':
        exon_st_block_miRNA.pop()
    exon_st_block_miRNA = list(map(int, exon_st_block_miRNA))

    if exon_number_mRNA == 1 and exon_number_miRNA >= 2: #Wrong sets
        continue
    if exon_number_mRNA == 1 and exon_number_miRNA == 1: #Simple pairs
        counter_1_1 += 1
        if strand == '+':
            st_trx = st_miRNA - st_mRNA
            ed_trx = ed_miRNA - st_mRNA
            print(mRNA_name,miRNA_name,st_trx,ed_trx, sep="\t", end="\n", file=output_file)
            counter_1_1_real += 1
            continue
        elif strand == '-':
            st_trx = ed_mRNA - ed_miRNA
            ed_trx = ed_mRNA - st_miRNA
            print(mRNA_name,miRNA_name,st_trx,ed_trx, sep="\t", end="\n", file=output_file)
            counter_1_1_real += 1
            continue
    elif exon_number_mRNA >= 2 and exon_number_miRNA == 1:
        counter_2_1 += 1
        exon_sites_chrom_mRNA = [[exon_st_block_mRNA[i],exon_st_block_mRNA[i]+exon_length_block_mRNA[i]] for i in range(len(exon_st_block_mRNA))]
        exon_sites_trx_mRNA = []

        exon_length_block_mRNA_test = [0] + exon_length_block_mRNA
        exon_site_now = exon_length_block_mRNA_test[0]
        for index in range(len(exon_length_block_mRNA_test)-1):
            exon_sites_trx_mRNA.extend([[exon_site_now, exon_site_now+exon_length_block_mRNA_test[index+1]]])
            exon_site_now += exon_length_block_mRNA_test[index+1]

        exon_st_trx_miRNA = 0
        exon_ed_trx_miRNA = 0
        end_point = exon_sites_trx_mRNA[-1][1]
        flg = 0
        for index in range(len(exon_sites_chrom_mRNA)):
            exon_st_chrom_mRNA = st_mRNA + exon_sites_chrom_mRNA[index][0]
            exon_ed_chrom_mRNA = st_mRNA + exon_sites_chrom_mRNA[index][1]
            if exon_st_chrom_mRNA <= st_miRNA and ed_miRNA <= exon_ed_chrom_mRNA:
                st_miRNA_sub = st_miRNA - exon_st_chrom_mRNA
                ed_miRNA_sub = ed_miRNA - exon_st_chrom_mRNA
                if strand == '+':
                    exon_st_trx_miRNA = exon_sites_trx_mRNA[index][0] + st_miRNA_sub
                    exon_ed_trx_miRNA = exon_sites_trx_mRNA[index][0] + ed_miRNA_sub
                elif strand == '-':
                    exon_st_trx_miRNA = end_point - (exon_sites_trx_mRNA[index][0] + ed_miRNA_sub)
                    exon_ed_trx_miRNA = end_point - (exon_sites_trx_mRNA[index][0] + st_miRNA_sub)
                print(mRNA_name,miRNA_name,exon_st_trx_miRNA,exon_ed_trx_miRNA, sep="\t", end="\n", file=output_file)
                counter_2_1_real += 1
                flg = 1
                break
        if flg == 0:
            print("Mismatched sets: ",rep_name)

    elif exon_number_mRNA >= 2 and exon_number_miRNA >= 2:
        counter_2_2 += 1
        exon_sites_chrom_mRNA = [[exon_st_block_mRNA[i],exon_st_block_mRNA[i]+exon_length_block_mRNA[i]] for i in range(len(exon_st_block_mRNA))]
        exon_sites_trx_mRNA = []

        exon_length_block_mRNA_test = [0] + exon_length_block_mRNA
        exon_site_now = exon_length_block_mRNA_test[0]
        for index in range(len(exon_length_block_mRNA_test)-1):
            exon_sites_trx_mRNA.extend([[exon_site_now, exon_site_now+exon_length_block_mRNA_test[index+1]]])
            exon_site_now += exon_length_block_mRNA_test[index+1]

        exon_sites_chrom_miRNA = [[exon_st_block_miRNA[i],exon_st_block_miRNA[i]+exon_length_block_miRNA[i]] for i in range(len(exon_st_block_miRNA))]
        
        exon_st_trx_miRNA = 0
        exon_ed_trx_miRNA = 0
        end_point = exon_sites_trx_mRNA[-1][1]
        flg = 0
        for index in range(len(exon_sites_chrom_mRNA)):
            exon_st_chrom_mRNA = st_mRNA + exon_sites_chrom_mRNA[index][0]
            exon_ed_chrom_mRNA = st_mRNA + exon_sites_chrom_mRNA[index][1]

            exon_st_chrom_miRNA = 0
            exon_ed_chrom_miRNA = 0
            
            for index_miRNA in range(len(exon_sites_chrom_miRNA)):
                exon_st_chrom_miRNA = st_miRNA + exon_sites_chrom_miRNA[index_miRNA][0]
                exon_ed_chrom_miRNA = st_miRNA + exon_sites_chrom_miRNA[index_miRNA][1]
                
                if exon_st_chrom_miRNA < exon_st_chrom_mRNA and exon_ed_chrom_mRNA < exon_ed_chrom_miRNA:
                    print('WARNING: ' + rep_name)
                elif exon_st_chrom_mRNA <= exon_ed_chrom_miRNA and exon_ed_chrom_miRNA == exon_ed_chrom_mRNA:
                    st_miRNA_sub = exon_st_chrom_miRNA - exon_st_chrom_mRNA
                    ed_miRNA_sub = exon_ed_chrom_miRNA - exon_st_chrom_mRNA

                    if strand == '+':
                        exon_st_trx_miRNA = exon_sites_trx_mRNA[index][0] + st_miRNA_sub
                        #exon_ed_trx_miRNA = exon_sites_trx_mRNA[index][0] + ed_miRNA_sub
                        flg += 1
                    elif strand == '-':
                        exon_ed_trx_miRNA = end_point - (exon_sites_trx_mRNA[index][0] + st_miRNA_sub)
                        flg += 1

                elif exon_st_chrom_miRNA == exon_st_chrom_mRNA and exon_st_chrom_mRNA <= exon_ed_chrom_miRNA:
                    st_miRNA_sub = exon_st_chrom_miRNA - exon_st_chrom_mRNA
                    ed_miRNA_sub = exon_ed_chrom_miRNA - exon_st_chrom_mRNA

                    if strand == '+':
                        #exon_st_trx_miRNA = exon_sites_trx_mRNA[index][0] + st_miRNA_sub
                        exon_ed_trx_miRNA = exon_sites_trx_mRNA[index][0] + ed_miRNA_sub
                        flg += 1
                    elif strand == '-':
                        exon_st_trx_miRNA = end_point - (exon_sites_trx_mRNA[index][0] + ed_miRNA_sub)
                        flg += 1
        if flg == 2:
            print(mRNA_name,miRNA_name,exon_st_trx_miRNA,exon_ed_trx_miRNA, sep="\t", end="\n", file=output_file)
            counter_2_2_real += 1


print("1_1: ",str(counter_1_1))
print("2_1: ",str(counter_2_1))
print("2_2: ",str(counter_2_2))
print("1_1_real: ",str(counter_1_1_real))
print("2_1_real: ",str(counter_2_1_real))
print("2_2_real: ",str(counter_2_2_real))
