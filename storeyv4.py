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


#open file with error handling
try:
    f=open('story.txt', 'r')
except IOError:
    print('cannot open file story.txt')
    
#set main variables
num_lines = 0
num_words = 0
num_letters = 0
num_sentences = 0
word_dict = {}
story_lines=[]
char_replace=[",",":","(",")","+", "..", '"']
line_end=[".", "!", "?"]

#add to dictionary, key = word, value = number of words
def word_count(word):
    if word not in word_dict.keys():
        word_dict[word] = 0
    word_dict[word] += 1

#break up sentences, discard irrelevant characters
def purify(line):
    num_sentences = 0
    num_letters = 0
    num_words = 0
    for word in line:
        num_words += 1
        new_word=''
        for letter in word:
            for char in char_replace:
                if char == letter:
                    letter = ""
            for end in line_end:
                if end == letter:
                    num_sentences += 1
            new_word=new_word+letter
            num_letters+=1
        word_count(new_word)
    values=(num_sentences, num_words, num_letters)
    return values

line=f.readline()
while line:
    line_tokens=line.strip().split(" ")
    num_lines+=1
    if len(line_tokens)>1:
        print(line_tokens)
        purified=purify(line_tokens)
        num_sentences+=purified[0]
        num_words+=purified[1]
        num_letters+=purified[2]
    line=f.readline()
print(word_dict)
print("Number of letters: " + str(num_letters))
print("Number of words: " + str(num_words))
print("Number of sentences: " + str(num_sentences))
print("Number of lines: " + str(num_lines))

f.close()
