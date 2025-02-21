#!/usr/bin/env python

import re
from sequence import sequence
from fasta import fasta
from fastq import fastq

#### will have to figure out the way to make the path not matter when inputing a file
#ask user to input a file
file_name = input("please enter a fastq or fasta file: ")
#deliniate between a fasta and fastq file with regular expression
pattern = re.compile(r'.fastq$')
pattern2 = re.compile(r'.fasta$')
pattern3 = re.compile(r'.faa$')
match = re.findall(pattern,file_name)
match2 = re.findall(pattern2,file_name)
match3 = re.findall(pattern3,file_name)
#try:
if len(match) == 1:
        #open the file and use the fasq module to print the required data
        fastq.file = open(f"c:/Users/andre/OneDrive/Documents/BINF690/project 2/{file_name}")
        fastq.read(None)
        fastq.count(None)
        fastq.avg_length(None)
        #asks user if they want to extract data, and if so uses the fastq write method to store in a new file
        data = input('Do you want to extract data from the file?(yes or no): ')
        if data == 'yes':
            fastq.write(None)
        elif data == 'no':
            print('Have a nice day!')
        else:
            print("That wasn't yes or no! Goodbye!")
    #if fasta
elif len(match2) == 1 or len(match3) == 1:
        #open the file and use the fasq module to print the required data
        fasta.file = open(f"c:/Users/andre/OneDrive/Documents/BINF690/project 2/{file_name}")
        fasta.read(None)
        fasta.count(None)
        fasta.avg_length(None)
        #asks user if they want to extract data, and if so uses the fastq write method to store in a new file
        data = input('Do you want to extract data from the file?(yes or no): ')
        if data == 'yes':
            fasta.write(None)
        elif data == 'no':
            print('Have a nice day!')
        else:
            print("That wasn't yes or no! Goodbye!")
else:
        print('not a valid file')
#except:
    #print("Invalid file Type")
