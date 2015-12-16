#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -soft -l ljob,lmem
#$ -l s_vmem=16G
#$ -l mem_req=16G

###Requisite###
##Software/Scripts##
#gtf2bed.pl
#Extract_RefSeq_NM.py
#make_symbol_map.py
#DaPars_Extract_Anno.py

#Bedtools

##dataset##
#Refseq_gene_hg19_June_02_2014.gtf(Illumina iGenome)

###File PATH###
GTFFile='/home/akimitsu/Documents/database/annotation_file/Refseq_gene_hg19_June_02_2014.gtf'

###Dapars scripts PATH###
ScriptDir='/home/akimitsu/Documents/software/dapars-master/src/scripts'

###Save directory PATH###
AnnoDir='/home/akimitsu/Documents/database/annotation_file'
DaParsDir='/home/akimitsu/Documents/software/dapars-master/src'

###Run Dapars###
python ${DaParsDir}/DaPars_main.py DaPars_configure2.txt
