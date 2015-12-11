#!/usr/bin/env python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

counter = {}

for line in input_file:
    line = line.rstrip()
    data = line.split("\t")
    conversion = ''
    try:
        conversion = data[7]
    except IndexError:
        conversion = 'NA'
    if conversion == 'NA':
        if not 'NA' in counter:
            counter['NA'] = 1
        else:
            counter['NA'] += 1
        continue
    else:
        conversion_location = conversion.split(':')[1]
        if not conversion_location in counter:
            counter[conversion_location] = 1
        else:
            counter[conversion_location] += 1
        continue

sum_count = 0

for index in counter.values():
    count = int(index)
    sum_count += count

print('Total count: ',str(sum_count))
print('Conversion','Count #','count %', sep="\t",end="\n",file=output_file)

for index in counter.keys():
    count = int(counter[index])
    percent = count/sum_count
    conversion = index
    print(conversion, str(count),str(percent), sep="\t",end="\n",file=output_file)
