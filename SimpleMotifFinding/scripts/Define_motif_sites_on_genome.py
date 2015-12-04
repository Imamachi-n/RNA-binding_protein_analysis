#!/usr/bin/env python3

import re
import sys

motif_file = open(sys.argv[1], 'r') #$Refseq_mRNA_3UTR_PUM_study.result
motif_length = int(sys.argv[2]) #8nt
anno_bed_list = open(sys.argv[3], 'r') #Refseq_mRNA_3UTR.bed
output_file = open(sys.argv[4], 'w')

motif_dict = {}

for line in motif_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == "refid":
        continue
    refid = data[0]
    if data[1] != "NA":
        motif_st_sites = data[1].split(',')
        motif_dict[refid] = motif_st_sites
    else:
        continue

counter = 0

for line in anno_bed_list:
    line = line.rstrip()
    data = line.split("\t")
    refid = data[3]
    if refid in motif_dict:
        motif_st_sites = motif_dict[refid] #list(st)
        motif_sites = [[int(x), int(x)+int(motif_length)] for x in motif_st_sites] #[[st1,ed1], [st2,ed2]...]

        chrom = data[0]
        st = int(data[1])
        ed = int(data[2])
        strand = data[5]

        exon_block = data[10].split(',')
        exon_block.pop()
        exon_block = list(map(int,exon_block))
        exon_st_block = data[11].split(',')
        exon_st_block.pop()
        exon_st_block = list(map(int,exon_st_block))

        for x in range(len(motif_sites)):
            #Define the start/end site of one of motifs
            st_motif = motif_sites[x][0]
            ed_motif = motif_sites[x][1]
            if len(exon_block) == 1:
                if strand == '+':
                    chrom_st_motif = st + st_motif
                    chrom_ed_motif = st + ed_motif
                    length = str(chrom_ed_motif - chrom_st_motif) + ','
                    print(chrom,str(chrom_st_motif),str(chrom_ed_motif),refid,'0',strand,str(chrom_ed_motif),str(chrom_ed_motif),'0','1',length,'0,', sep="\t", end="\n", file=output_file)
                elif strand == '-':
                    chrom_st_motif = ed - ed_motif
                    chrom_ed_motif = ed - st_motif
                    length = str(chrom_ed_motif - chrom_st_motif) + ','
                    print(chrom,str(chrom_st_motif),str(chrom_ed_motif),refid,'0',strand,str(chrom_ed_motif),str(chrom_ed_motif),'0','1',length,'0,', sep="\t", end="\n", file=output_file)
                else:
                    print("ERROR: Strand is not defined...")
                    sys.exit(1)
            else:
                #print(refid)
                #print(exon_st_block)
                #print(exon_block)
                #exon_sites_real: Define the start/end sites for each exon based on 'genome' position
                exon_sites_real = [[exon_st_block[i],exon_st_block[i]+exon_block[i]] for i in range(len(exon_block))] #[[exon_st1,exon_ed1], [exon_st2,exon_ed2]...]

                #exon_sites: Define the start/end sites for each exon based on 'transcript' position
                #exon_block = [200,100,50]
                exon_block_test = [0] + exon_block
                exon_site_now = exon_block_test[0]
                exon_sites = [] #[[exon_st1,exon_ed1], [exon_st2,exon_ed2]...]
                for index in range(len(exon_block_test)-1):
                    exon_sites.extend([[exon_site_now, exon_site_now+exon_block_test[index+1]]])
                    exon_site_now += exon_block_test[index+1]

                if strand == '+':
                    chrom_st_ed_list = []
                    for exon_index in range(len(exon_st_block)):
                        exon_st = exon_sites[exon_index][0]
                        exon_ed = exon_sites[exon_index][1]
                        if exon_st <= st_motif and ed_motif <= exon_ed:
                            st_motif_sub = st_motif - exon_st
                            ed_motif_sub = ed_motif - exon_st
                            exon_st_real = exon_sites_real[exon_index][0]
                            #exon_ed_real = exon_sites_real[exon_index][1]
                            chrom_st_motif = st + (exon_st_real + st_motif_sub)
                            chrom_ed_motif = st + (exon_st_real + ed_motif_sub)
                            length = str(chrom_ed_motif - chrom_st_motif) + ','
                            print(chrom,str(chrom_st_motif),str(chrom_ed_motif),refid,'0',strand,str(chrom_ed_motif),str(chrom_ed_motif),'0','1',length,'0,', sep="\t", end="\n", file=output_file)
                            break
                        elif st_motif < exon_ed and exon_ed < ed_motif:
                            #print(refid)
                            st_motif_sub = st_motif - exon_st
                            ed_motif_sub = exon_ed
                            
                            exon_st_real = exon_sites_real[exon_index][0]
                            #exon_ed_real = exon_sites_real[exon_index][1]

                            chrom_st_motif = st + (exon_st_real + st_motif_sub)
                            chrom_ed_motif = st + (exon_st_real + ed_motif_sub)
                            chrom_st_ed_list.extend([[chrom_st_motif, chrom_ed_motif]])
                            counter += 1
                        elif st_motif < exon_st and exon_st <= ed_motif:
                            st_motif_sub = exon_st
                            ed_motif_sub = ed_motif - exon_st

                            exon_st_real = exon_sites_real[exon_index][0]

                            chrom_st_motif = st + (exon_st_real + st_motif_sub)
                            chrom_ed_motif = st + (exon_st_real + ed_motif_sub)
                            chrom_st_ed_list.extend([[chrom_st_motif, chrom_ed_motif]])

                            chrom_st_motif_final = chrom_st_ed_list[0][0]
                            chrom_ed_motif_final = chrom_st_ed_list[-1][1]
                            chrom_exon_block_motif = [a[1]-a[0] for a in chrom_st_ed_list]
                            chrom_exon_st_block_motif = [a[0]-chrom_st_motif_final for a in chrom_st_ed_list]
                            counter += 1
                            print_chrom_exon_block_motif = ','.join(chrom_exon_block_motif) + ','
                            print_chrom_exon_st_block_motif = ','.join(chrom_exon_st_block_motif) + ','
                            print(chrom,str(chrom_st_motif_final),str(chrom_ed_motif_final),refid,'0',strand,str(chrom_ed_motif),str(chrom_ed_motif),'0',str(len(chrom_exon_block_motif)),print_chrom_exon_block_motif,print_chrom_exon_st_block_motif, sep="\t", end="\n", file=output_file)
                elif strand == '-':
                    #print(refid)
                    chrom_st_ed_list = []
                    exon_sites_end = exon_sites[-1][1]
                    for exon_index in range(len(exon_st_block)):
                        exon_st = exon_sites[exon_index][0]
                        exon_ed = exon_sites[exon_index][1]
                        motif_st_rev = exon_sites_end - ed_motif
                        motif_ed_rev = exon_sites_end - st_motif
                        if exon_st <= motif_st_rev and motif_ed_rev <= exon_ed:
                            st_motif_sub = motif_st_rev - exon_st
                            ed_motif_sub = motif_ed_rev - exon_st
                            exon_st_real = exon_sites_real[exon_index][0]
                            #exon_ed_real = exon_sites_real[exon_index][1]
                            chrom_st_motif = st + (exon_st_real + st_motif_sub)
                            chrom_ed_motif = st + (exon_st_real + ed_motif_sub)
                            length = str(chrom_ed_motif - chrom_st_motif) + ','
                            print(chrom,str(chrom_st_motif),str(chrom_ed_motif),refid,'0',strand,str(chrom_ed_motif),str(chrom_ed_motif),'0','1',length,'0,', sep="\t", end="\n", file=output_file)
                            break
                        elif motif_st_rev < exon_ed and exon_ed < motif_ed_rev:
                            #print(refid)
                            st_motif_sub = motif_st_rev - exon_st
                            ed_motif_sub = exon_ed
                            
                            exon_st_real = exon_sites_real[exon_index][0]
                            #exon_ed_real = exon_sites_real[exon_index][1]

                            chrom_st_motif = st + (exon_st_real + st_motif_sub)
                            chrom_ed_motif = st + (exon_st_real + ed_motif_sub)
                            chrom_st_ed_list.extend([[chrom_st_motif, chrom_ed_motif]])
                            counter += 1
                        elif motif_st_rev < exon_st and exon_st <= motif_ed_rev:
                            st_motif_sub = exon_st
                            ed_motif_sub = motif_ed_rev - exon_st

                            exon_st_real = exon_sites_real[exon_index][0]

                            chrom_st_motif = st + (exon_st_real + st_motif_sub)
                            chrom_ed_motif = st + (exon_st_real + ed_motif_sub)
                            chrom_st_ed_list.extend([[chrom_st_motif, chrom_ed_motif]])

                            chrom_st_motif_final = chrom_st_ed_list[0][0]
                            chrom_ed_motif_final = chrom_st_ed_list[-1][1]
                            chrom_exon_block_motif = [a[1]-a[0] for a in chrom_st_ed_list]
                            chrom_exon_st_block_motif = [a[0]-chrom_st_motif_final for a in chrom_st_ed_list]
                            counter += 1
                            print_chrom_exon_block_motif = ','.join(chrom_exon_block_motif) + ','
                            print_chrom_exon_st_block_motif = ','.join(chrom_exon_st_block_motif) + ','
                            print(chrom,str(chrom_st_motif_final),str(chrom_ed_motif_final),refid,'0',strand,str(chrom_ed_motif),str(chrom_ed_motif),'0',str(len(chrom_exon_block_motif)),print_chrom_exon_block_motif,print_chrom_exon_st_block_motif, sep="\t", end="\n", file=output_file)

                else:
                    print("ERROR: Strand is not defined...")
                    sys.exit(1)

    else:
        continue

print(str(counter))