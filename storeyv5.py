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
replaced_char=[]
num_lines = 0
num_words = 0
num_letters = 0
num_sentences = 0
word_dict = {}
story_lines=[]
char_replace=[",",":","(",")","+", "..", '"', "'"]
line_end=[".", "!", "?"]

#add to dictionary, key = word, value = number of words
def word_count(word):
    if word not in word_dict.keys():
        word_dict[word] = 0
    word_dict[word] += 1

#break up sentences, discard irrelevant characters, return num sentences/words/letters
def purify_count(line):
    num_sentences = 0
    num_letters = 0
    num_words = 0
    for word in line:
        word=word.lower()
        num_words += 1
        for char in char_replace:
            word=word.replace(char, '')
        for end in line_end:
            if word.find(end) != -1:
                num_sentences += 1
                word=word.replace(end, '')
        for letter in word:
            num_letters+=1
        word_count(word)
    values=(num_sentences, num_words, num_letters)
    return values

#main logic. opens and reads file, calls purify_count function
line=f.readline()
while line:
    line_tokens=line.strip().split(" ")
    num_lines+=1
    if len(line_tokens)>1:
        purified=purify_count(line_tokens)
        num_sentences+=purified[0]
        num_words+=purified[1]
        num_letters+=purified[2]
    line=f.readline()
#print(word_dict)
#print("Number of letters: " + str(num_letters))
#print("Number of words: " + str(num_words))
#print("Number of sentences: " + str(num_sentences))
#print("Number of lines: " + str(num_lines))
f.close()

#write numbers to a file 'storey_report.txt'
f=open("storey_report.txt", "w")
let=f'Number of letters: {num_letters}\n'
w=f'Number of words: {num_words}\n'
s=f'Number of sentences: {num_sentences}\n'
lin=f'Number of lines: {num_lines}\n'
t=let+w+s+lin
f.write(t)
sorted_words=sorted(word_dict.items(), key=lambda x:x[1], reverse=True)
f.write(str(sorted_words))
f.close()

#open storey_report.txt, and print to screen
f=open('storey_report.txt')
for line in f.readlines():
    print(line)
f.close()
# whitespace_chars = " \t\n\r\f" - space, tab, newline, return, formfeed
#list_of_words = mystring.split( \t\n\r\f,.;!?'\"()")
#if word in list_of_words:
#    print 'success'
