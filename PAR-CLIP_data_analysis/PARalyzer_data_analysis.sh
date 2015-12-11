#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -soft -l ljob,lmem
#$ -l s_vmem=4G
#$ -l mem_req=4G

###Requisite###
##Software/Scripts##
#estimate_conversion_pattern.py
#csv2bed6.py

##dataset##
#SRR309285_4SU_DMEM_PAR-CLIP_HuR_clusters.csv(PARalyzer_v1.1 output data)

###File PATH###
BowtieOutput='SRR309285_4SU_DMEM_PAR-CLIP_HuR_4_result_ver3.bowtie'
PARalyzerCSVOutput='SRR309285_4SU_DMEM_PAR-CLIP_HuR_clusters.csv'

###Estimate Conversion pattern###
bowtiefile=`basename ${BowtieOutput} .bowtie`
python3 estimate_conversion_pattern.py ${bowtiefile}.bowtie ${bowtiefile}_conversion.result

###Convert CSV file into Bed6 file###
filename=`basename ${PARalyzerCSVOutput} .csv`
python3 ./scripts/csv2bed6.py ${filename}.csv ${filename}.bed ${filename}.fasta ${filename}.result
