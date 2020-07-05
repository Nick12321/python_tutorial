#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:42:22 2020

@author: nick
"""

#Branch control statements

x=4

if x == 5:
    print(" x = 5!")
else:
    print(" x is not 5!!")
    


#for loop using range

for i in range(1,40,6):
    print(i)

print('-----------')    

for i in range(5,0,-1):
    print(i)
    
print('-----------')

#nested for loop

for r in range(1,5+1):
    print(r, ':', end="")
    for c in range(1,5+1):
        print("",c,end="")
    print("")

print('-----------')
    
s='Hello'

for c in s:
    print(c)
for c in s:
    print("",c,end="")
print("")
    
print('-----------')
# print out values in a list
list1=[1,2,3,4,5]
for x in list1:
    print(x)

print('-----------')

#print out two dimensional list
list2=[[1,2,3],[4,5,6],[7,8,9]]
for r in list2:
    for c in r:
        print(c,end="")
    print("")
    
print('-----------')

#print out values in a set
set1 = {1,2,3,4,5}
for x in set1:
    print(x)
#print("")

print('-----------')

#Put all letters from a string into a set
s="tommorow"
print(s)

set1=set()
for c in s:
    set1.add(c)
for x in set1:
    print(x)
    
print('-----------')

# print dictionary values

d={"name":"Bob", "age":24, "idnum":"S1234"}
for key, value in d.items():
    print(key, value)
    

#print dictionary by key
for key in d.keys():
    print(key)

#print dictionary by value
for value in d.values():
    print(value)

