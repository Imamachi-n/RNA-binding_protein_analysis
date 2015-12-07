#!usr/bin/env python

import sys
import re
import shelve

def main():
    for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,'X','Y']:
    #for x in ['Y']:
        ref_file = open(sys.argv[1],'r') #mirBase, Refseq etc...

        input_s = 'chr' + str(x) + '.phyloP46way.bed'
        output_s = 'chr' + str(x) + '.phyloP46way_' + sys.argv[1] + '.db' #phastCons46way_miRBase_v21_hg38Tohg19.db
        phylop_sizedown_input_file = open(input_s,'r')

        score_dict = {}
        chrom_name = 'chr' + str(x)

        for line in ref_file:
            line = line.rstrip()
            data = line.split("\t")
            chrom = data[0]
            if not chrom_name == chrom:
                continue
            if len(data) >= 12: #12bed format
                exon_block = data[10].split(',')
                exon_block.pop() #Remove the last item ''
                exon_st = data[11].split(',')
                exon_st.pop() #Remove the last item ''
                #name = data[3]
                for y in range(len(exon_block)):
                    st = int(data[1]) + int(exon_st[y])
                    ed = int(data[1]) + int(exon_st[y]) + int(exon_block[y])
                    length = ed - st
                    for z in range(length):
                        score_dict[str(st)] = 0
                        st += 1
            elif len(data) >= 3: #6bed format
                st = int(data[1])
                ed = int(data[2])
                length = ed - st
                for z in range(length):
                    score_dict[str(st)] = 0
                    st += 1
            else:
                print('ERROR: Your BED format file have less than three column.')
                print ('BED format file need to have at least three column [chr, st, ed]...')
                sys.exit(1)

        for line in phylop_sizedown_input_file:
            line = line.rstrip()
            data = line.split("\t")
            st_site = 0
            score = 0
            if re.match(r'^chr',data[0]):
                st_site = data[1] #
                score = data[2] #
            else:
                st_site = data[0] #
                score = data[1] #
            if st_site in score_dict:
                score_dict[str(st_site)] = score

        shelve_db = shelve.open(output_s)
        shelve_db.update(score_dict)
            
        phylop_sizedown_input_file.close()
        shelve_db.close()


if __name__ == '__main__':
    main()
