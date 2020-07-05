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

print('-----------')
#print dictionary sorted by key
for key in sorted(d.keys()):
    print(key, d[key])
    
print('-----------')
#print dictionary sorted by value
for value in sorted(d.values(), key=str):
    for key in d.keys():
        if d[key]==value:
            print(key, value)
            break

print('-----------')

def fcmp(x):
    return str(x[1])

sort_by_value=sorted(d.items(), key=fcmp)
print(sort_by_value)

# below doesnt work as an inline function, I think because x isnt defined???
# print(sorted(d.items(), key=str(x[1])))

print('-----------')

x=lambda a,b:a*b
print(type(x))
y=x(3,4)
print(y)

sort_by_value=sorted(d.items(), key=lambda x:str(x[1]))
print(sort_by_value)

print('-----------')
#make a dictionary using animal type as key and name as value
#print sorted by name.
# make dictionary using animal name as key and type as the value
#print sorted by animal type

animal_dict1 = {'dog':'Harley', ''}





