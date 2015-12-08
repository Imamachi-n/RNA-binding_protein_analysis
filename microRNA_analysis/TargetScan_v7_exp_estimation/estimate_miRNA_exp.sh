#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -soft -l ljob,lmem
#$ -l s_vmem=4G
#$ -l mem_req=4G

###Requisite###
##Software/Scripts##

##dataset##
#Predicted_Targets.hg19_trx_sites_for_NGS_dataset.txt(SimpleMotifFinding output data)
#htseq_count_result_SRR309288_sRNAseq_Mock_miRBase_v21.txt(htseq-count output data)

###File PATH###
HTseqOutput='htseq_count_result_SRR309288_sRNAseq_Mock_miRBase_v21.txt'
MirPosition='Predicted_Targets.hg19_trx_sites_for_NGS_dataset.txt'

###Download_miR_Family_Info_from_TargetScan_v7###
wget http://www.targetscan.org/vert_70/vert_70_data_download/miR_Family_Info.txt.zip
unzip miR_Family_Info.txt.zip
miRFamilyInfo='miR_Family_Info.txt'

###Estimate_TargetScan_v7.0_miRNA_expression###
python3 ./scripts/estimate_targetscan_v7_miRNA_exp.py ${miRFamilyInfo} ${HTseqOutput} ${MirPosition} Predicted_Targets.hg19_trx_sites_for_NGS_dataset_exp_plus.txt
python3 ./scripts/estimate_targetscan_v7_miRNA_exp2.py Predicted_Targets.hg19_trx_sites_for_NGS_dataset_exp_plus.txt Predicted_Targets.hg19_trx_sites_for_NGS_dataset_exp_mod.txt
