#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:53:09 2020

@author: nick
"""

#read story.txt and report number of lines, sentences, words, and letters
#keep track of each word count in a dictionary

story=[]

try:
    f=open('story.txt', 'r')
    for file_line in f.readlines():
        story.append(file_line)
    f.close()
except IOError:
    print('cannot open file story.txt')
    
print(story)


#num_lines = 0

story_lines=[]
line=f.readline()

while line:
    tokens=line.strip()
    story_lines.append(tokens)

l=len(story_lines)

f.close()

