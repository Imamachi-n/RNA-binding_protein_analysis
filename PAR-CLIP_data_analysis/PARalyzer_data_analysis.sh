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
flg=${7} #take2

###PARalyzer scripts PATH###
ScriptDir='/home/akimitsu/software/PARalyzer_v1_1/scripts'

###PARalyzer Result Directory###
bowtiefile=`basename ${BowtieOutput} .bowtie`
savedir=PARalyzer_result_${bowtiefile}_${flg}
#mkdir ${savedir} 

###Estimate Conversion pattern###
#python3 ${ScriptDir}/estimate_conversion_pattern.py ${bowtiefile}.bowtie ./${savedir}/${bowtiefile}_conversion.result

###Make .ini file for PARalyzer###
python3 ${ScriptDir}/make_ini_file_for_PARalyzer.py ${bowtiefile} ${Genome2bitFile} ${MinConversionLocations} 5 ./${savedir}/${bowtiefile}

###Run PARalyzer###
#echo ./${savedir}/${bowtiefile}.ini
#PARalyzer ./${savedir}/${bowtiefile}.ini

###Convert CSV file into Bed6 file###
python3 ${ScriptDir}/csv2bed6.py ./${savedir}/${bowtiefile}_clusters.csv ./${savedir}/${bowtiefile}_clusters.bed ./${savedir}/${bowtiefile}_clusters.fasta ./${savedir}/${bowtiefile}_clusters.result

###Convert Bed6 into Bed12 file###
python3 ${ScriptDir}/bed6tobed12.py ./${savedir}/${bowtiefile}_clusters.bed ./${savedir}/${bowtiefile}_clusters_B12.bed

###Define representative isoform from RNA-seq data(Cuffdiff results)###
CuffdiffGeneFilename=`basename ${CuffdiffGeneResultData} .diff`
python3 ${ScriptDir}/A_define_Representative_isoform_from_RNA-seq.py ${CuffdiffIsoformData} ${CuffdiffGeneResultData} ./${savedir}/${CuffdiffGeneFilename}_rep_isoform_list.txt

###Extract CLIP-seq peaks in 3'UTR region of RefSeq transcripts###
intersectBed -a ${Refseq3UTR} -b ./${savedir}/${bowtiefile}_clusters_B12.bed -wa -wb > ./${savedir}/${bowtiefile}_vs_RefSeq_3UTR.bed
python3 ${ScriptDir}/Define_motif_sites_on_transcriptome.py ./${savedir}/${bowtiefile}_vs_RefSeq_3UTR.bed ./${savedir}/${bowtiefile}_trx_sites.txt
python3 ${ScriptDir}/Compare_annotation_infor_with_CLIP-seq_peaks.py ./${savedir}/${bowtiefile}_trx_sites.txt ./${savedir}/${bowtiefile}_clusters.result ./${savedir}/${CuffdiffGeneFilename}_rep_isoform_list.txt ./${savedir}/${bowtiefile}_trx_sites_for_NGS_dataset.txt ./${savedir}/${bowtiefile}_trx_sites_for_NGS_dataset.fasta
