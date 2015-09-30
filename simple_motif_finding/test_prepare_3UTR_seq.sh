#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -l s_vmem=4G
#$ -l mem_req=4
###files
GTF_FILE_NAME='./Refseq_gene_hg19_June_02_2014.gtf'

###Make_3UTR_BED_file
filename=`basename ${GTF_FILE_NAME} .gtf`
for file in ${filename} #Refseq_gene_hg19_June_02_2014
do
    perl ./gtf2bed.pl ${file}.gtf > ${file}.bed
    perl ./D_make_3UTR_bed_format_data.pl ${file}.bed ${file}_3UTR.bed ${file}_non-3UTR.bed
    bedtools getfasta -s -split -name -fi ~/database/genome/hg19.fa -bed ${file}_3UTR.bed -fo ${file}_3UTR.fa
done
