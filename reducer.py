#!/usr/bin/python3.6
'''
Updated on Apr 27, 2017
'''
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)

    for col, group in groupby(data, itemgetter(0)):
        for line in group:
            print("%s" % (line[1]))

if __name__ == "__main__":
    main()