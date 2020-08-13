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
f.write("I kkkkkkkk")
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

#write lines to end of file
f=open('test.txt', 'a')
f.write('I like Python')
f.write('\n')
f.close()

#Open the file for read
f=open('test.txt')
#read one line at a time until empty
for line in f.readlines():
    print(line)
f.close()

#Write to a csv file
#write lines to end of file
f=open('test.csv', 'w')
f.write('one,two,three,four')
f.write('\n')
f.close()

#read from a CSV file
#strip method removes end of line character
#split function seperate words between commas
f=open('test.csv')
line=f.readline()
while line:
    #strip removes '\n'
    #split seperates line into tokens
    print('here! ------------------')
    tokens=line.strip().split(",")
    print(tokens)
    #printing out individual token
    for t in tokens:
        print(t)
    line=f.readline()
f.close()
print('now here ----------------')

#try - except block will catch file error
try:
    f=open('test.txt', 'r')
    for line in f.readlines():
        print(line)
    f.close()
except IOError:
    print('cannot open file test.txt')
    
#write object to file using pickle
class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        
    def __str__(self):
        return "Book: "+self.title+ " written by: " + self.author
    
b=Book("Wizard of Oz","L. Frank Baum")

#use pickle to create the file and write the object
import pickle

f=open("book.p", "wb")
pickle.dump(b,f)
f.close()

#use pickle to read the file
f=open("book.p", "rb")
book=pickle.load(f)
f.close()
#print the book
print(book)