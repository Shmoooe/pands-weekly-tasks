# This program reads in a text file and outputs the number of "e's" it contains.
# The program should take the filename from an argument on the command line.
# Author: Joanna Kelly

# reference for learning about sys.argv: 
#https://www.youtube.com/watch?v=ZQ9JO0e9468

import sys

print(sys.argv)

#must type "mobydick.txt" after file name each time
moby_dick = sys.argv[1]  #my mobydick.txt file will be argument 1

num_e = 0  #creating this variable and setting it first to 0

with open(moby_dick, "r") as f:  #this will open the txt file and read it
    for line in f:              #this iterates over every line in the file and stores them as variable "line"
        for char in line:       #this iterates over every character in the lines
            if char == "e" or char == "E":     #check if the character is "e"
                num_e += 1      #For every count of letter "e", 1 is added to cariable num_e
              

print(num_e)  #prints the numbers of "e"s in the txt file
