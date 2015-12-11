#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -soft -l ljob,lmem
#$ -l s_vmem=4G
#$ -l mem_req=4G

###Requisite###
##Software/Scripts##
#estimate_conversion_pattern.py
#make_ini_file_for_PARalyzer.py
#csv2bed6.py

##dataset##
#SRR309285_4SU_DMEM_PAR-CLIP_HuR_4_result_ver3.bowtie(Default bowtie output)

###File PATH###
BowtieOutput=${1} #'SRR309285_4SU_DMEM_PAR-CLIP_HuR_4_result_ver3.bowtie'
Genome2bitFile=${2} #'/home/akimitsu/database/genome/hg19.2bit'
MinConversionLocations=${3}

###PARalyzer scripts PATH###
ScriptDir='/home/akimitsu/software/PARalyzer_v1_1/scripts'

###Estimate Conversion pattern###
bowtiefile=`basename ${BowtieOutput} .bowtie`
python3 ${ScriptDir}/estimate_conversion_pattern.py ${bowtiefile}.bowtie ${bowtiefile}_conversion.result

###Make .ini file for PARalyzer###
python3 ${ScriptDir}/make_ini_file_for_PARalyzer.py ${bowtiefile} ${Genome2bitFile} ${MinConversionLocations} 5

###Run PARalyzer###
echo ${bowtiefile}.ini
PARalyzer ${bowtiefile}.ini

###Convert CSV file into Bed6 file###
python3 ${ScriptDir}/csv2bed6.py ${BowtieOutput}_clusters.csv ${BowtieOutput}_clusters.bed ${BowtieOutput}_clusters.fasta ${BowtieOutput}_clusters.result
