#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:53:09 2020

@author: nick
"""

#read story.txt and report number of lines, sentences, words, and letters
#keep track of each word count in a dictionary

story_lines=[]
char_replace=[",",":","(",")","+"]

try:
    f=open('story.txt', 'r')
except IOError:
    print('cannot open file story.txt')
    
num_lines = 0

line=f.readline()

while line:
    line_tokens=line.strip().split(" ")
    #story_lines.append(line_tokens)
    num_lines+=1
    print(line_tokens)
    length=len(line_tokens)
    if length>1:
        print('USEFUL!!!!!!!!!!!!!!!!')
    
    """
    for word in line_tokens:
        word=line_tokens.split(" ")
        print(word)
        
        for char in char_replace:
            word=word.replace(char_replace[char],"")
            print('here! ------------------')
        story_lines.append(word)
        """
    print(str(len(line_tokens)))    
    line=f.readline()

print(str(num_lines))
f.close()


"""
for file_line in f.readlines():
        story.append(file_line)
    f.close()
    
"""