#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -soft -l ljob,lmem
#$ -l s_vmem=16G
#$ -l mem_req=16G

###Requisite###
##Software/Scripts##
#

##dataset##
#Refseq_gene_hg19_June_02_2014.gtf(Illumina iGenome)

###File PATH###
CuffdiffGeneResultData=${1} #'/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/cuffdiff_out_RNA-seq_HeLa_CFIm25_RefSeq/gene_exp_RefSeq_result_mRNA.diff'
CuffdiffIsoformData=${2} #'/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/cuffdiff_out_RNA-seq_HeLa_CFIm25_RefSeq/isoform_exp.diff'
DaparsResultFile=${3} #'/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/DaPars_result/DaPars_result_siCTRL_S_vs_siCFIm25_1_All_Prediction_Results.txt'
OutputFile=${4} #'/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/DaPars_result/DaPars_result_siCTRL_S_vs_siCFIm25_1_All_Prediction_Results_with_Anno.txt'

###Dapars scripts PATH###
ScriptDir='/home/akimitsu/Documents/software/dapars-master/src/scripts'

###Save directory PATH###
SaveDir='/home/akimitsu/Documents/data/CFIm25_study/RNA-seq'

###Define representative isoform from RNA-seq data(Cuffdiff results)###
CuffdiffGeneFilename=`basename ${CuffdiffGeneResultData} .diff`
#python3 ${ScriptDir}/A_define_Representative_isoform_from_RNA-seq.py ${CuffdiffIsoformData} ${CuffdiffGeneResultData} ./${savedir}/${CuffdiffGeneFilename}_rep_isoform_list.txt

###Merge DaPars result###
python3 ${ScriptDir}/merge_dapers_result.py ${DaparsResultFile} ${SaveDir}/${CuffdiffGeneFilename}_rep_isoform_list.txt ${OutputFile}
