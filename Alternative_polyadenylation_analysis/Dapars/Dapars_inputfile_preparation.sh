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
BamFileArray=('/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/RNA-seq_NoCTRL_131210_140107_merged_out/accepted_hits.bam' \
			  '/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/RNA-seq_siCFlm25-1_131210_140107_merged_out/accepted_hits.bam' \
			  '/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/RNA-seq_siCFlm25-2_131210_140107_merged_out/accepted_hits.bam' \
			  '/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/RNA-seq_siCTRL_S_131210_140107_merged_out/accepted_hits.bam')

###Dapars scripts PATH###
ScriptDir='/home/akimitsu/Documents/software/dapars-master/src/scripts'
DaParsDir='/home/akimitsu/Documents/software/dapars-master/src'

###Save directory PATH###
AnnoDir='/home/akimitsu/Documents/database/annotation_file'
mkdir /home/akimitsu/Documents/data/CFIm25_study/RNA-seq/DaPars_result
SaveDir='/home/akimitsu/Documents/data/CFIm25_study/RNA-seq/DaPars_result'

###Convert gtf to bed file###
AnnoFile=`basename ${GTFFile} .gtf`
#perl ${ScriptDir}/gtf2bed.pl ${AnnoDir}/${AnnoFile}.gtf > ${AnnoDir}/${AnnoFile}.bed

###Extract RefSeq NM(mRNA) data###
#python3 ${ScriptDir}/Extract_RefSeq_NM.py ${AnnoDir}/${AnnoFile}.bed ${AnnoDir}/${AnnoFile}_NM_only.bed

###Make GeneID - GeneSymbol dictionary###
#python3 ${ScriptDir}/make_symbol_map.py ${AnnoDir}/${AnnoFile}.gtf ${AnnoDir}/${AnnoFile}_symbol_map_for_DaPars.txt

###Generate region annotation###
#python ${DaParsDir}/DaPars_Extract_Anno.py -b ${AnnoDir}/${AnnoFile}.bed -s ${AnnoDir}/${AnnoFile}_symbol_map_for_DaPars.txt -o ${AnnoDir}/${AnnoFile}_extracted_3UTR_for_DaPars.bed
#python ${DaParsDir}/DaPars_Extract_Anno.py -b ${AnnoDir}/${AnnoFile}_NM_only.bed -s ${AnnoDir}/${AnnoFile}_symbol_map_for_DaPars.txt -o ${AnnoDir}/${AnnoFile}_NM_only_extracted_3UTR_for_DaPars.bed

###Prepare DaPars input file###
for file in ${BamFileArray[@]}
do
    filename=`basename ${file} .bam`
	samtools index ${file}
	bedtools genomecov -ibam ${file} -bg -split > ${file}.wig
done
