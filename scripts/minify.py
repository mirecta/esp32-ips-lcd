#!/usr/bin/python3
import sys



file1 = open('code.js', 'r')
for line in file1.readlines():

    line = line[:-1].strip().replace('"','\'')
    if line:
        print('"%s"' % line)

