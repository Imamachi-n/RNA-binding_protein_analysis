#!/usr/bin/env python3

import sys

bowtie_file = sys.argv[1]
genome_2bit = sys.argv[2]
min_conversion_locations = sys.argv[3]
min_read_count = sys.argv[4]

output_path = bowtie_file + '.ini'
ini_file = open(output_path, 'w')

infor1 = 'BANDWIDTH=3'
infor2 = 'CONVERSION=T>C'
infor3 = 'MINIMUM_READ_COUNT_PER_GROUP=5'
infor4 = 'MINIMUM_READ_COUNT_PER_CLUSTER=5'
infor5 = 'MINIMUM_READ_COUNT_FOR_KDE=5'
infor6 = 'MINIMUM_CLUSTER_SIZE=10'
infor7 = 'MINIMUM_CONVERSION_LOCATIONS_FOR_CLUSTER=' + min_conversion_locations
infor8 = 'MINIMUM_CONVERSION_COUNT_FOR_CLUSTER=1'
infor9 = 'MINIMUM_READ_COUNT_FOR_CLUSTER_INCLUSION=' + min_read_count
infor10 = 'MINIMUM_READ_LENGTH=13'
infor11 = 'MAXIMUM_NUMBER_OF_NON_CONVERSION_MISMATCHES=0'

infor12 = 'ADDITIONAL_NUCLEOTIDES_BEYOND_SIGNAL=5'

infor13 = 'BOWTIE_FILE=' + bowtie_file + '.bowtie'
infor14 = 'GENOME_2BIT_FILE=' + genome_2bit

infor15 = '#FILTER_FILE=./RepeatMasker/DNA.txt=DNA'
infor16 = '#FILTER_FILE=./RepeatMasker/LINE.txt=LINE'
infor17 = '#FILTER_FILE=./RepeatMasker/Low_complexity.txt=Low_complexity'
infor18 = '#FILTER_FILE=./RepeatMasker/LTR.txt=LTR'
infor19 = '#FILTER_FILE=./RepeatMasker/Other.txt=Other'
infor20 = '#FILTER_FILE=./RepeatMasker/RC.txt=RC'
infor21 = '#FILTER_FILE=./RepeatMasker/RNA.txt=RNA'
infor22 = '#FILTER_FILE=./RepeatMasker/Satellite.txt=Satallite'
infor23 = '#FILTER_FILE=./RepeatMasker/SINE.txt=SINE'
infor24 = '#FILTER_FILE=./RepeatMasker/Unknown.txt=Unknown'

infor25 = 'OUTPUT_DISTRIBUTIONS_FILE=' + bowtie_file + '_distribution.csv'
infor26 = 'OUTPUT_GROUPS_FILE=' + bowtie_file + '_groups.csv'
infor27 = 'OUTPUT_CLUSTERS_FILE=' + bowtie_file + '_clusters.csv'

print(infor1, end="\n", file=ini_file)
print(infor2, end="\n", file=ini_file)
print(infor3, end="\n", file=ini_file)
print(infor4, end="\n", file=ini_file)
print(infor5, end="\n", file=ini_file)
print(infor6, end="\n", file=ini_file)
print(infor7, end="\n", file=ini_file)
print(infor8, end="\n", file=ini_file)
print(infor9, end="\n", file=ini_file)
print(infor10, end="\n", file=ini_file)
print(infor11, end="\n", file=ini_file)
print("\n", end="", file=ini_file)
print(infor12, end="\n", file=ini_file)
print("\n", end="", file=ini_file)
print(infor13, end="\n", file=ini_file)
print(infor14, end="\n", file=ini_file)
print("\n", end="", file=ini_file)
print(infor15, end="\n", file=ini_file)
print(infor16, end="\n", file=ini_file)
print(infor17, end="\n", file=ini_file)
print(infor18, end="\n", file=ini_file)
print(infor19, end="\n", file=ini_file)
print(infor20, end="\n", file=ini_file)
print(infor21, end="\n", file=ini_file)
print(infor22, end="\n", file=ini_file)
print(infor23, end="\n", file=ini_file)
print(infor24, end="\n", file=ini_file)
print("\n", end="", file=ini_file)
print(infor25, end="\n", file=ini_file)
print(infor26, end="\n", file=ini_file)
print(infor27, end="\n", file=ini_file)
