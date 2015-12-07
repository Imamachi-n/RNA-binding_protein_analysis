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

RefseqBedFile='Refseq_gene_hg19_June_02_2014_3UTR.bed'
RefseqBedFile=`basename ${RefseqBedFile} .bed`
MotifBedFile='Refseq_gene_hg19_June_02_2014_3UTR_merged_PUM_motif.bed'
MotifBedFile=`basename ${MotifBedFile} .bed`
Motif1='Refseq_gene_hg19_June_02_2014_3UTR_merged_TGTAAATA.bed'
Motif2='Refseq_gene_hg19_June_02_2014_3UTR_merged_TGTATATA.bed'
Motif3='Refseq_gene_hg19_June_02_2014_3UTR_merged_TGTAGATA.bed'
Motif4='Refseq_gene_hg19_June_02_2014_3UTR_merged_TGTACATA.bed'
Motif5='Refseq_gene_hg19_June_02_2014_3UTR_merged_FINAL.bed'
Motif1=`basename ${Motif1} .bed`
Motif2=`basename ${Motif2} .bed`
Motif3=`basename ${Motif3} .bed`
Motif4=`basename ${Motif4} .bed`
Motif5=`basename ${Motif5} .bed`

RepIsoform='PUM1KD_gene_exp_RefSeq_result_mRNA_rep_isoform_list.txt'

###Download phastCons46way(hg19) datasets###
#for chr in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y
#do
#    wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/phastCons46way/vertebrate/chr${chr}.phastCons46way.wigFix.gz
#    gunzip chr${chr}.phastCons46way.wigFix.gz
#done

###Convert wigfix file into bed file###
#python3 ./scripts/phastcons_score_prep.py

###Make the shelve db of the conservation in 3'UTR region of mRNAs###
#python3 ./scripts/phastcons_sizedown.py ${RefseqBedFile}.bed
#for ChrNumber in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y
#do
#    cp chr${ChrNumber}.phastCons46way_${RefseqBedFile}.bed.db.db chr${ChrNumber}.phastCons46way_${RefseqBedFile}.bed.db
#done

###Estimate the conservation score of motif sequence###
##Motif='TGTAAATA,TGTATATA,TGTAGATA,TGTACATA'
#python3 ./scripts/estimate_motif_conservation.py ${MotifBedFile} ${RefseqBedFile}
##Motif1='TGTAAATA'
#python3 ./scripts/estimate_motif_conservation.py ${Motif1} ${RefseqBedFile}
##Motif2='TGTATATA'
#python3 ./scripts/estimate_motif_conservation.py ${Motif2} ${RefseqBedFile}
##Motif3='TGTAGATA'
#python3 ./scripts/estimate_motif_conservation.py ${Motif3} ${RefseqBedFile}
##Motif4='TGTACATA'
#python3 ./scripts/estimate_motif_conservation.py ${Motif4} ${RefseqBedFile}
##MotifFinal='TGTAAATA,TGTATATA,TGTACATA'
#python3 ./scripts/estimate_motif_conservation.py ${Motif5} ${RefseqBedFile}

###Define PUM motif sites on your transcriptome###
##Motif='TGTAAATA,TGTATATA,TGTAGATA,TGTACATA'
#bedtools intersect -a ${RefseqBedFile}_merged.bed -b ${MotifBedFile}_conservation.bed -wa -wb -split -s > ${MotifBedFile}_vs_${RefseqBedFile}.txt
#python3 ./scripts/Remove_redundant_infor.py ${MotifBedFile}_vs_${RefseqBedFile}.txt ${MotifBedFile}_vs_${RefseqBedFile}_removed.txt
#python3 ./scripts/Define_motif_sites_on_transcriptome_for_conservation.py ${MotifBedFile}_vs_${RefseqBedFile}_removed.txt ${MotifBedFile}_trx_sites.txt
##Motif1='TGTAAATA'
#bedtools intersect -a ${RefseqBedFile}_merged.bed -b ${Motif1}_conservation.bed -wa -wb -split -s > ${Motif1}_vs_${RefseqBedFile}.txt
#python3 ./scripts/Remove_redundant_infor.py ${Motif1}_vs_${RefseqBedFile}.txt ${Motif1}_vs_${RefseqBedFile}_removed.txt
#python3 ./scripts/Define_motif_sites_on_transcriptome_for_conservation.py ${Motif1}_vs_${RefseqBedFile}_removed.txt ${Motif1}_trx_sites.txt
##Motif2='TGTATATA'
#bedtools intersect -a ${RefseqBedFile}_merged.bed -b ${Motif2}_conservation.bed -wa -wb -split -s > ${Motif2}_vs_${RefseqBedFile}.txt
#python3 ./scripts/Remove_redundant_infor.py ${Motif2}_vs_${RefseqBedFile}.txt ${Motif2}_vs_${RefseqBedFile}_removed.txt
#python3 ./scripts/Define_motif_sites_on_transcriptome_for_conservation.py ${Motif2}_vs_${RefseqBedFile}_removed.txt ${Motif2}_trx_sites.txt
##Motif3='TGTAGATA'
#bedtools intersect -a ${RefseqBedFile}_merged.bed -b ${Motif3}_conservation.bed -wa -wb -split -s > ${Motif3}_vs_${RefseqBedFile}.txt
#python3 ./scripts/Remove_redundant_infor.py ${Motif3}_vs_${RefseqBedFile}.txt ${Motif3}_vs_${RefseqBedFile}_removed.txt
#python3 ./scripts/Define_motif_sites_on_transcriptome_for_conservation.py ${Motif3}_vs_${RefseqBedFile}_removed.txt ${Motif3}_trx_sites.txt
##Motif4='TGTACATA'
#bedtools intersect -a ${RefseqBedFile}_merged.bed -b ${Motif4}_conservation.bed -wa -wb -split -s > ${Motif4}_vs_${RefseqBedFile}.txt
#python3 ./scripts/Remove_redundant_infor.py ${Motif4}_vs_${RefseqBedFile}.txt ${Motif4}_vs_${RefseqBedFile}_removed.txt
#python3 ./scripts/Define_motif_sites_on_transcriptome_for_conservation.py ${Motif4}_vs_${RefseqBedFile}_removed.txt ${Motif4}_trx_sites.txt
##MotifFinal='TGTAAATA,TGTATATA,TGTACATA'
#bedtools intersect -a ${RefseqBedFile}_merged.bed -b ${Motif5}_conservation.bed -wa -wb -split -s > ${Motif5}_vs_${RefseqBedFile}.txt
#python3 ./scripts/Remove_redundant_infor.py ${Motif5}_vs_${RefseqBedFile}.txt ${Motif5}_vs_${RefseqBedFile}_removed.txt
#python3 ./scripts/Define_motif_sites_on_transcriptome_for_conservation.py ${Motif5}_vs_${RefseqBedFile}_removed.txt ${Motif5}_trx_sites.txt

###Compare representative isoform with PUM motifs/miRNA-binding sites###
##PUM motif
#python3 ./scripts/Compare_annotation_infor_with_conservation_infor.py ${RepIsoform} ${MotifBedFile}_trx_sites.txt ${MotifBedFile}_trx_sites_for_NGS_dataset.txt
##Motif1='TGTAAATA'
#python3 ./scripts/Compare_annotation_infor_with_conservation_infor.py ${RepIsoform} ${Motif1}_trx_sites.txt ${Motif1}_trx_sites_for_NGS_dataset.txt
##Motif2='TGTATATA'
#python3 ./scripts/Compare_annotation_infor_with_conservation_infor.py ${RepIsoform} ${Motif2}_trx_sites.txt ${Motif2}_trx_sites_for_NGS_dataset.txt
##Motif3='TGTAGATA'
#python3 ./scripts/Compare_annotation_infor_with_conservation_infor.py ${RepIsoform} ${Motif3}_trx_sites.txt ${Motif3}_trx_sites_for_NGS_dataset.txt
##Motif4='TGTACATA'
#python3 ./scripts/Compare_annotation_infor_with_conservation_infor.py ${RepIsoform} ${Motif4}_trx_sites.txt ${Motif4}_trx_sites_for_NGS_dataset.txt
##MotifFinal='TGTAAATA,TGTATATA,TGTACATA'
#python3 ./scripts/Compare_annotation_infor_with_conservation_infor.py ${RepIsoform} ${Motif5}_trx_sites.txt ${Motif5}_trx_sites_for_NGS_dataset.txt
