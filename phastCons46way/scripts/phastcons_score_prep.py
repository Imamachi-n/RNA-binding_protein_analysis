#!usr/bin/env python

import os
import re

def main():
    for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,'X','Y']: #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,'X','Y']:
        input_s = 'chr' + str(x) + '.phastCons46way.wigFix'
        output_s = 'chr' + str(x) + '.phastCons46way.bed'
        phastcons_prep_input_file = open(input_s,'r')
        phastcons_prep_output_file = open(output_s,'w')

        chrom = ''
        start_site = 0
        step = 1

        for line in phastcons_prep_input_file:
            line = line.rstrip()
            if re.match(r'^fixedStep',line):
                regex = r'fixedStep chrom=(?P<chrom>.+) start=(?P<start>.+) step=(?P<step>.+)'
                seq = re.match(regex,line)
                chrom = seq.group('chrom')
                start_site = int(seq.group('start')) - 1
                step = int(seq.group('step'))
                continue
            score = line
            #end_site = start_site + step
            for x in range(step):
                print (start_site, score, file=phastcons_prep_output_file, sep="\t", end="\n")
                start_site += 1

        phastcons_prep_input_file.close()
        phastcons_prep_output_file.close()

if __name__ == '__main__':
    main()
