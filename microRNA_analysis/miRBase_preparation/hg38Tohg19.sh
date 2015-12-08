#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -soft -l ljob,lmem
#$ -l s_vmem=4G
#$ -l mem_req=4G

###Download###
wget ftp://mirbase.org/pub/mirbase/CURRENT/genomes/hsa.gff3
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/liftOver
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/liftOver/hg38ToHg19.over.chain.gz

###Preparation###
gunzip hg38ToHg19.over.chain.gz
chmod 755 liftOver
mv hsa.gff3 miRBase_v21_hsa_hg38.gff3
python3 ./scripts/make_bed_file_from_gff_file.py miRBase_v21_hsa_hg38.gff3 miRBase_v21_hsa_hg38.bed

###Convert hg38 to hg19###
./liftOver miRBase_v21_hsa_hg38.bed hg38ToHg19.over.chain miRBase_v21_hsa_hg19.bed miRBase_v21_hsa_hg19_Error.bed
python3 ./scripts/make_converted_gff_file.py miRBase_v21_hsa_hg19.bed miRBase_v21_hsa_hg19_Error.bed miRBase_v21_hsa_hg19.gff3
