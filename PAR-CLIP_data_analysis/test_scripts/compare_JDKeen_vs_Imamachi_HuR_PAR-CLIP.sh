#!/bin/bash
bedtools intersect -a SRR309285_4SU_DMEM_PAR-CLIP_HuR_clusters.bed -b Lebedeva.DMEM.clusters.bed -loj > PAR-CLIP_HuR_Comp_Imamachi_vs_JDKeen.bed
bedtools intersect -a Lebedeva.DMEM.clusters.bed -b SRR309285_4SU_DMEM_PAR-CLIP_HuR_clusters.bed -loj > PAR-CLIP_HuR_Comp_JDKeen_vs_Imamachi.bed
