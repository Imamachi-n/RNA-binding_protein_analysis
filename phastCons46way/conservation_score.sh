#!/bin/sh
#$ -S /bin/bash
#$ -cwd
#$ -l s_vmem=16G
#$ -l mem_req=16G

###Requisite###
##Software/Scripts##
#phastcons_score_prep.py
#phastcons_sizedown.py

##dataset##
#chrXX.phastCons46way.wigFix.gz
#Refseq_gene_hg19_June_02_2014_3UTR.bed

###Download phastCons46way(hg19) datasets###
#for chr in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y
#do
#    wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/phastCons46way/vertebrate/chr${chr}.phastCons46way.wigFix.gz
#    gunzip chr${chr}.phastCons46way.wigFix.gz
#done

###Convert wigfix file into bed file###
#python3 ./scripts/phastcons_score_prep.py

###Make the shelve db of the conservation in 3'UTR region of mRNAs###
#python3 ./scripts/phastcons_sizedown.py Refseq_gene_hg19_June_02_2014_3UTR.bed
for ChrNumber in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y
do
    cp chr${ChrNumber}.phastCons46way_Refseq_gene_hg19_June_02_2014_3UTR.bed.db.db chr${ChrNumber}.phastCons46way_Refseq_gene_hg19_June_02_2014_3UTR.bed.db
done
