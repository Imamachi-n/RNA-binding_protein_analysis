#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -l s_vmem=4G
#$ -l mem_req=4
###files
CUFFDIFF_ISOFORM_FILE='./raw_data/PUM1KD_isoform_exp.diff'
CUFFDIFF_GENE_RESULT_FILE='./raw_data/PUM1KD_gene_exp_RefSeq_result_mRNA.diff'
RESULT_FILE='./result/PUM1KD_gene_exp_RefSeq_rep_isoform.result'
FASTA_FILE='./Refseq_gene_hg19_June_02_2014_3UTR.fa'
MOTIFS='TGTAAATA,TGTATATA,TGTAGATA,TGTACATA'

###Define_representative_isoform
python3 A_define_Representative_isoform_from_RNA-seq.py ${CUFFDIFF_ISOFORM_FILE} ${CUFFDIFF_GENE_RESULT_FILE} ${RESULT_FILE}
python3 B_find_motifs.py ${FASTA_FILE} ${RESULT_FILE} ${RESULT_FILE}.seq ${MOTIFS}