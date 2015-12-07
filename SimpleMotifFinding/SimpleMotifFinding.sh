#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -soft -l ljob,lmem
#$ -l s_vmem=4G
#$ -l mem_req=4G

###Requisite###
##Software/Scripts##
#gtf2bed.pl
#D_make_3UTR_bed_format_data.pl
#Integrate_same_regions.py
#motif_finding_from_fasta.py
#Define_motif_sites_on_genome.py
#Define_motif_sites_on_transcriptome.py
#A_define_Representative_isoform_from_RNA-seq.py
#bedtools

##dataset##
#Refseq_gene_hg19_June_02_2014.gtf
#hg19.fa
#Predicted_Targets.hg19.bed (Predicted miRNA-binding sites by TargetScan v7.0)
#PUM1KD_isoform_exp.diff
#PUM1KD_gene_exp_RefSeq_result_mRNA.diff

###File_information###
GTFFile='Refseq_gene_hg19_June_02_2014.gtf'
GenomeFastaFile='/home/akimitsu/database/bowtie1_index/hg19.fa'
Motif='TGTAAATA,TGTATATA,TGTAGATA,TGTACATA'
MotifFinal='TGTAAATA,TGTATATA,TGTACATA'
Motif1='TGTAAATA'
Motif2='TGTATATA'
Motif3='TGTAGATA'
Motif4='TGTACATA'
MotifName='PUM_motif'
MotifLength='8'
miRNABedFile='Predicted_Targets.hg19.bed'

CuffdiffGeneResultData='./PUM1KD_gene_exp_RefSeq_result_mRNA.diff'
CuffdiffIsoformData='./PUM1KD_isoform_exp.diff'

###Change gtf to bed file###
Filename=`basename ${GTFFile} .gtf`
#./scripts/gtf2bed.pl ${Filename}.gtf > ${Filename}.bed

###Extract 3UTR region from bed12 file###
#perl ./scripts/D_make_3UTR_bed_format_data.pl ${Filename}.bed ${Filename}_3UTR.bed ${Filename}_non-3UTR.bed

###Convert bed12 file into fasta file using bedtools getfasta command###
#python3 ./scripts/Integrate_same_regions.py ${Filename}_3UTR.bed ${Filename}_3UTR_merged.bed
#bedtools getfasta -name -s -split -fi ${GenomeFastaFile} -bed ${Filename}_3UTR_merged.bed -fo ${Filename}_3UTR_merged.fa

###Find your motif from fasta file###
##Motif='TGTAAATA,TGTATATA,TGTAGATA,TGTACATA'
#python3 ./scripts/motif_finding_from_fasta.py ${Filename}_3UTR_merged.fa ${Motif} ${Filename}_3UTR_merged_${MotifName}.result
#python3 ./scripts/Divide_motif_finding_data.py ${Filename}_3UTR_merged_${MotifName}.result ${Filename}_3UTR_merged_${MotifName}.txt 8
##Motif1='TGTAAATA'
#python3 ./scripts/motif_finding_from_fasta.py ${Filename}_3UTR_merged.fa ${Motif1} ${Filename}_3UTR_merged_${MotifName}_${Motif1}.result
#python3 ./scripts/Divide_motif_finding_data.py ${Filename}_3UTR_merged_${MotifName}_${Motif1}.result ${Filename}_3UTR_merged_${MotifName}_${Motif1}.txt 8
##Motif2='TGTATATA'
#python3 ./scripts/motif_finding_from_fasta.py ${Filename}_3UTR_merged.fa ${Motif2} ${Filename}_3UTR_merged_${MotifName}_${Motif2}.result
#python3 ./scripts/Divide_motif_finding_data.py ${Filename}_3UTR_merged_${MotifName}_${Motif2}.result ${Filename}_3UTR_merged_${MotifName}_${Motif2}.txt 8
##Motif3='TGTAGATA'
#python3 ./scripts/motif_finding_from_fasta.py ${Filename}_3UTR_merged.fa ${Motif3} ${Filename}_3UTR_merged_${MotifName}_${Motif3}.result
#python3 ./scripts/Divide_motif_finding_data.py ${Filename}_3UTR_merged_${MotifName}_${Motif3}.result ${Filename}_3UTR_merged_${MotifName}_${Motif3}.txt 8
##Motif4='TGTACATA'
#python3 ./scripts/motif_finding_from_fasta.py ${Filename}_3UTR_merged.fa ${Motif4} ${Filename}_3UTR_merged_${MotifName}_${Motif4}.result
#python3 ./scripts/Divide_motif_finding_data.py ${Filename}_3UTR_merged_${MotifName}_${Motif4}.result ${Filename}_3UTR_merged_${MotifName}_${Motif4}.txt 8
##MotifFinal='TGTAAATA,TGTATATA,TGTACATA'
#python3 ./scripts/motif_finding_from_fasta.py ${Filename}_3UTR_merged.fa ${MotifFinal} ${Filename}_3UTR_merged_${MotifName}_FINAL.result
#python3 ./scripts/Divide_motif_finding_data.py ${Filename}_3UTR_merged_${MotifName}_FINAL.result ${Filename}_3UTR_merged_${MotifName}_FINAL.txt 8

###Define motif sites on your genome###
##Motif='TGTAAATA,TGTATATA,TGTAGATA,TGTACATA'
#python3 ./scripts/Define_motif_sites_on_genome.py ${Filename}_3UTR_merged_${MotifName}.result ${MotifLength} ${Filename}_3UTR_merged.bed ${Filename}_3UTR_merged_${MotifName}.bed
##Motif1='TGTAAATA'
#python3 ./scripts/Define_motif_sites_on_genome.py ${Filename}_3UTR_merged_${MotifName}_${Motif1}.result ${MotifLength} ${Filename}_3UTR_merged.bed ${Filename}_3UTR_merged_${Motif1}.bed
##Motif2='TGTATATA'
#python3 ./scripts/Define_motif_sites_on_genome.py ${Filename}_3UTR_merged_${MotifName}_${Motif2}.result ${MotifLength} ${Filename}_3UTR_merged.bed ${Filename}_3UTR_merged_${Motif2}.bed
##Motif3='TGTAGATA'
#python3 ./scripts/Define_motif_sites_on_genome.py ${Filename}_3UTR_merged_${MotifName}_${Motif3}.result ${MotifLength} ${Filename}_3UTR_merged.bed ${Filename}_3UTR_merged_${Motif3}.bed
##Motif4='TGTACATA'
#python3 ./scripts/Define_motif_sites_on_genome.py ${Filename}_3UTR_merged_${MotifName}_${Motif4}.result ${MotifLength} ${Filename}_3UTR_merged.bed ${Filename}_3UTR_merged_${Motif4}.bed
##MotifFinal='TGTAAATA,TGTATATA,TGTACATA'
#python3 ./scripts/Define_motif_sites_on_genome.py ${Filename}_3UTR_merged_${MotifName}_FINAL.result ${MotifLength} ${Filename}_3UTR_merged.bed ${Filename}_3UTR_merged_FINAL.bed

###Define miRNA-binding sites on your transcriptome###
miRNAFilename=`basename ${miRNABedFile} .bed`
#bedtools intersect -a ${Filename}_3UTR_merged.bed -b ${miRNAFilename}.bed -wa -wb -split -s > ${miRNAFilename}_vs_${Filename}.txt
#python3 ./scripts/Define_motif_sites_on_transcriptome.py ${miRNAFilename}_vs_${Filename}.txt ${miRNAFilename}_trx_sites.txt

###Define representative isoform from RNA-seq data(Cuffdiff results)###
CuffdiffGeneFilename=`basename ${CuffdiffGeneResultData} .diff`
#python3 ./scripts/A_define_Representative_isoform_from_RNA-seq.py ${CuffdiffIsoformData} ${CuffdiffGeneFilename}.diff ${CuffdiffGeneFilename}_rep_isoform_list.txt

###Compare representative isoform with PUM motifs/miRNA-binding sites###
##miRNA-binding sites
#python3 ./scripts/Compare_annotation_infor_with_miRNA_infor.py ${CuffdiffGeneFilename}_rep_isoform_list.txt ${miRNAFilename}_trx_sites.txt ${miRNAFilename}_trx_sites_for_NGS_dataset.txt
##Motif='TGTAAATA,TGTATATA,TGTAGATA,TGTACATA'
#python3 ./scripts/Compare_annotation_infor_with_motif_infor.py ${CuffdiffGeneFilename}_rep_isoform_list.txt ${Filename}_3UTR_merged_${MotifName}.txt ${Filename}_3UTR_merged_${MotifName}_for_NGS_dataset.txt
##Motif1='TGTAAATA'
#python3 ./scripts/Compare_annotation_infor_with_motif_infor.py ${CuffdiffGeneFilename}_rep_isoform_list.txt ${Filename}_3UTR_merged_${MotifName}_${Motif1}.txt ${Filename}_3UTR_merged_${MotifName}_${Motif1}_for_NGS_dataset.txt
##Motif2='TGTATATA'
#python3 ./scripts/Compare_annotation_infor_with_motif_infor.py ${CuffdiffGeneFilename}_rep_isoform_list.txt ${Filename}_3UTR_merged_${MotifName}_${Motif2}.txt ${Filename}_3UTR_merged_${MotifName}_${Motif2}_for_NGS_dataset.txt
##Motif3='TGTAGATA'
#python3 ./scripts/Compare_annotation_infor_with_motif_infor.py ${CuffdiffGeneFilename}_rep_isoform_list.txt ${Filename}_3UTR_merged_${MotifName}_${Motif3}.txt ${Filename}_3UTR_merged_${MotifName}_${Motif3}_for_NGS_dataset.txt
##Motif4='TGTACATA'
#python3 ./scripts/Compare_annotation_infor_with_motif_infor.py ${CuffdiffGeneFilename}_rep_isoform_list.txt ${Filename}_3UTR_merged_${MotifName}_${Motif4}.txt ${Filename}_3UTR_merged_${MotifName}_${Motif4}_for_NGS_dataset.txt
##MotifFinal='TGTAAATA,TGTATATA,TGTACATA'
#python3 ./scripts/Compare_annotation_infor_with_motif_infor.py ${CuffdiffGeneFilename}_rep_isoform_list.txt ${Filename}_3UTR_merged_${MotifName}_FINAL.txt ${Filename}_3UTR_merged_${MotifName}_FINAL_for_NGS_dataset.txt

###Define 3'UTR length###
#python3 ./scripts/Calc_3UTR_length.py ${Filename}_3UTR.bed ${CuffdiffGeneFilename}_rep_isoform_list.txt ${CuffdiffGeneFilename}_rep_isoform_list_3UTR_length.txt

###Count miRNA-binding sites in the 3'UTR region of PUM1 targets###
#python3 ./scripts/miRNA_number_counting.py PUM1_targets_miRNA.txt PUM1_targets_miRNA_count.txt 91
#python3 ./scripts/miRNA_number_counting.py all_genes_miRNA.txt all_genes_miRNA_count.txt 12143

