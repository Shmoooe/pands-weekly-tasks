# This program reads in a text file and outputs the number of "e's" it contains.
# The program should take the filename from an argument on the command line.
# Author: Joanna Kelly

# First I need to create the file:
'''
file = open("moby_dick.txt", "x")  # Created file, cancelled this code.
'''
'''
import os
import sys


def count_es(filename):     # creating function and parameter
    with open(filename, "r") as file:
        text = file.read()
        return text.count("e")
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python es.py <moby_dick.txt>")
        sys.exit(1)

    filename = sys.argv[1]

count = count_es("moby_dick.txt")
if count != -1:
    print(count)

'''
 # TOTALLY LOST