#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:53:09 2020

@author: nick
"""

#read story.txt and report number of lines, sentences, words, and letters
#keep track of each word count in a dictionary

#break the words into letters, removing unwanted and counting.
#Count end of sentence char and letters. Return whole words
#while words are still 'whole' in an array,
#count the number of words, and put them in a dictionary while counting.

story_lines=[]
char_replace=[",",":","(",")","+", "..", '"']
line_end=[".", "!", "?"]

try:
    f=open('story.txt', 'r')
except IOError:
    print('cannot open file story.txt')
    
num_lines = 0
num_sentences = 0
num_words = 0
num_letters = 0
word_count = {}

line=f.readline()

while line:
    line_tokens=line.strip().split(" ")
    num_lines+=1
    if len(line_tokens)>1:
        #print(line_tokens)
        for word in line_tokens:
            if word not in word_count.keys():
                word_count[word] = 0
            word_count[word] += 1
    line=f.readline()
print(word_count)
print(str(num_lines))
f.close()
