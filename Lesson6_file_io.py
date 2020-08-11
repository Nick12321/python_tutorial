#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:33:21 2020

@author: nick
"""

#write lines to a file

f=open("test.txt", "w")
f.write("I like programming")
f.write("\n")
f.write("I like programming")
f.write("\n")
f.write("I like programming")
f.write("\n")
f.close()

#open the file for read
f = open("test.txt", "r")
#read all lines in the file to a list
lines=f.readlines()
print(lines)
#close the file
f.close()

#read line one at a time, till the file is empty
f=open('test.txt')
#read the first line
line=f.readline()
#read line one at a time, till the file is empty
while line:
    print(line)
    line=f.readline()
f.close() # close the file

#use a for loop to read each line, traversing using the readlines function
f = open('test.txt')
for line in f.readlines():
    print(line)
f.close() #close the file