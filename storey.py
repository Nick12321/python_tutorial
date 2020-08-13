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
    for line in f.readlines():
        story.append(line)
    f.close()
except IOError:
    print('cannot open file story.txt')
    
print(story)

lines = 0
convert=[]

for line in story:
    
        
