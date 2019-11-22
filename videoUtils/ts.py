#!/usr/bin/python
# -*- coding=utf-8 -*-
import glob
import os
import sys
import getopt


def printUsage():
    print 'ts.py -i <inputdir> -o <outputfile>'


def generate(argv):
    inputdir = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["inputdir=", "outputfile="])
    except getopt.GetoptError:
        printUsage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printUsage()
            sys.exit()
        elif opt in ("-i", "--inputdir"):
            inputdir = arg
        elif opt in ("-o", "--outputfile"):
            outputfile = arg
    if inputdir == '' or outputfile == '':
        printUsage()
        sys.exit()

    index = []
    os.chdir(inputdir)
    for file in glob.glob("*.ts"):
        arr = os.path.splitext(file)
        index.append(int(arr[0]))

    index.sort()

    cmd = 'cat '
    for num in index:
        cmd += str(num)
        cmd += ".ts "
    cmd += " > output.ts"
    cmd += '&& mv output.ts ' + outputfile
    os.system(cmd)

if __name__ == "__main__":
    generate(sys.argv[1:])
