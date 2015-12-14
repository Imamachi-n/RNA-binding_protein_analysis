#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -soft -l ljob,lmem
#$ -l s_vmem=16G
#$ -l mem_req=16G

###Requisite###
##Software/Scripts##
#estimate_conversion_pattern.py
#make_ini_file_for_PARalyzer.py
#csv2bed6.py
#bed6tobed12.py
#A_define_Representative_isoform_from_RNA-seq.py

##dataset##
#SRR309285_4SU_DMEM_PAR-CLIP_HuR_4_result_ver3.bowtie(Default bowtie output)

###File PATH###
BowtieOutput=${1} #'SRR309285_4SU_DMEM_PAR-CLIP_HuR_4_result_ver3.bowtie'
Genome2bitFile=${2} #'/home/akimitsu/database/genome/hg19.2bit'
MinConversionLocations=${3} #1 or 2
Refseq3UTR=${4} #'Refseq_gene_hg19_June_02_2014_3UTR.bed'
CuffdiffGeneResultData=${5} #'/home/akimitsu/data/HuR_study/RNA-seq/cuffnorm_out_RNA-seq_HeLa_HuRKD_RefSeq/gene_exp_RefSeq_result_mRNA.diff'
CuffdiffIsoformData=${6} #'/home/akimitsu/data/HuR_study/RNA-seq/cuffnorm_out_RNA-seq_HeLa_HuRKD_RefSeq/isoform_exp.diff'

###PARalyzer scripts PATH###
ScriptDir='/home/akimitsu/software/PARalyzer_v1_1/scripts'

###Estimate Conversion pattern###
bowtiefile=`basename ${BowtieOutput} .bowtie`
#python3 ${ScriptDir}/estimate_conversion_pattern.py ${bowtiefile}.bowtie ${bowtiefile}_conversion.result

###Make .ini file for PARalyzer###
python3 ${ScriptDir}/make_ini_file_for_PARalyzer.py ${bowtiefile}.take2 ${Genome2bitFile} ${MinConversionLocations} 5

###Run PARalyzer###
#echo ${bowtiefile}.ini
PARalyzer ${bowtiefile}.ini.take2

###Convert CSV file into Bed6 file###
#python3 ${ScriptDir}/csv2bed6.py ${bowtiefile}_clusters_take2.csv ${bowtiefile}_clusters_take2.bed ${bowtiefile}_clusters_take2.fasta ${bowtiefile}_clusters_take2.result

###Convert Bed6 into Bed12 file###
python3 ${ScriptDir}/bed6tobed12.py ${bowtiefile}_clusters_take2.bed ${bowtiefile}_clusters_take2_B12.bed

###Define representative isoform from RNA-seq data(Cuffdiff results)###
#CuffdiffGeneFilename=`basename ${CuffdiffGeneResultData} .diff`
#python3 ${ScriptDir}/A_define_Representative_isoform_from_RNA-seq.py ${CuffdiffIsoformData} ${CuffdiffGeneFilename}.diff ${CuffdiffGeneFilename}_rep_isoform_list.txt

###Extract CLIP-seq peaks in 3'UTR region of RefSeq transcripts###
intersectBed -a ${Refseq3UTR} -b ${bowtiefile}_clusters_take2_B12.bed -wa -wb > ${bowtiefile}_take2_vs_RefSeq_3UTR.bed
#python3 select_PAR-CLIP_peaks_on_3UTR_region.py ${CuffdiffGeneFilename}_rep_isoform_list.txt ${bowtiefile}_vs_RefSeq_3UTR.bed ${bowtiefile}_vs_RefSeq_3UTR_list.txt
