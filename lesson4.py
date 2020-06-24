#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:07:59 2020

@author: nick
"""


# To create an empty list
list1=[]
print(list1)

list_a=[]

# To create a list with pre-initialized values
list2=[1,2,3,4,5]
print(list2)
list_b=['dog', 'cat', 'horse', 'hyperion', 'raccoon']

# To get the number of elements in a list
x=len(list2)
print(x)
y=len(list_b)
print(y)

#Create a list pre-initialized with one value of a specified length
#a list of 10 zero's (0)s created
list3=[0]*10
print(list3)
list_c=['a']*10
print(list_c)

#Add a value to a list
list1.append(5)
print(list1)
list_a.append('roach')
print(list_a)

#Print a list
print(list2)
print(list_b)

#Get a value from a list at a specified location
x=list2[0]
print(x)
y=list_b[2]
print(y)
y=1
print(type(y))

#Get part of a list
#[start index=0: end index=len()-1: (optional step=1)]
#(defaults are start and end index)
#[:] would therefore be the whole list using defaults

list3=list2[1:3]
print(list3)
list_c=list_b[0:4]
print(list_c)


#Get last value of list
list3=list2[-1:]
print(list3)
list_c=list_b[-1:]
print(list_c)
#print('------------')

#Get last 2 values of list
list3=list2[-2:]
print(list3)
#get all values except last value
list3=list2[:-1]
print(list3)

#Get all values except last 2 values
list3=list2[:-2]
print(list3)
list_c=list_b[:-2]
print(list_c)

#Reverse a list
list3=list2[::-1]
print(list3)
list_c=list_b[::-1]
print(list_c)


#sort a list in place
list3.sort()
print(list3)
list_c.sort()
print(list_c)


#return a sorted list
list4=sorted(list3)
print(list4)
list_d=sorted(list_b)
print(list_d)
print(list_b)

#join two lists together
list3=list1 + list2
print(list3)
list_c=list_b+list_d
print(list_c)

#remove a value from a list
list2.remove(3)
print(list2)
list_c.remove('cat')
print(list_c)

#remove a list item by index
del list2[0]
print(list2)
del list_c[4]
print(list_c)

#test if a value is in  a list returns True or False
x=2 in list2
print(x)
x=1 in list2
print(x)
y='cat' in list_c
print(y)
z='dog' in list_c
print(z)

#put a list inside another list
list1.append(list2)
print(list1)
list_c.append(list_a)
print(list_c)

# convert a string to a list
s='happy days are here again'
list1=s.split(' ')
print(list1)

#convert a list to a string
s=' '.join(list1)
print(s)

list_c=list_c[:-2]
#t=' '.join(list_c)
print(list_c)

#convert list_c from a list into a string
s_c=' '.join(list_c)
print(s_c)

# convert string s_c into a list
s_c=s_c.split(' ')
print(s_c)

#convert a list of integers to a string of numbers
#note join alone will not work, as it takes only one argument
#map converts each number to a string, and passes it to join
list1=[1,2,3,4,5]
print(list1)
s=''.join(map(str,list1))
print(s)

#list contains a function
def fsq(x):
    return x*x

list1=[1,2,fsq(3)]
print(list1)

#execute a function stored in a list
list1=[1,2,fsq]
print(list1[2](5))

#Sets 
s=set('tomorrow')
print(s)
s1={'tomorrow', 'today', 'tomorrow'}
print(s1)

#To create an empty set
s1=set()
print(s1)

#To create a list with pre-initialized values
s2={1,2,3,4,5}
print(s2)

# get the number of elements in a set
x=len(s2)
print(x)

#Add a value to a set
s1.add(5)
print(s1)

#Remove a value from a set
s2.remove(3)
print(s2)

#Test if a value is in a set
x=2 in s2
print(x)

s1.add(4)
s1.add(6)
s1.add(7)
print(s1)

list4=[s1,8,9,10]
print(list4)
s3=s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)

#create two sets of favourite animals and try union / intersection functions
sa1 = {'dog', 'cat', 'rabbit', 'hen'}
sa2 = {'hen', 'rabbit', 'dragon', 'sphinx'}
sa3=sa1.union(sa2)
print(sa3)
sa4=sa1.intersection(sa2)
print(sa4)


#Dictionary work
# Create two dictionaries, one with name / animal type, and the other with animal type / sound
# Get user to input animal name, and provide a sentence describing the animal type and sound.


d1={'Harley':'dog'}
d1["Chleo"] = 'lion'
d1['Tigress'] = 'tiger'
d2={'dog':'barks', 'lion':'roars', 'tiger':'grunts'}
print(d2.keys())
print(d1.values())


def get_name():
    animal_name="Chleo"
    #animal_name=input("Name of the animal you would like to know about? ")
    return(animal_name)

def print_info(animal_name, animal_type, animal_sound):
    print(animal_name + " is a " + animal_type + " that " + animal_sound + ".")
    #following line creates a list from d1 keys, and the ordinal comes from 'index'.
    #print(list(d1.keys())[list(d1.values()).index(animal_type)])

def get_type(animal_name):
    animal_type=d1[animal_name]
    return animal_type

def get_sound(animal_type):
    animal_sound=d2[animal_type]
    return(animal_sound)
       
animal_name=get_name()
animal_type=get_type(animal_name)
animal_sound=get_sound(animal_type)
print_info(animal_name, animal_type, animal_sound)

print(list(d1.values()).index('tiger'))
 


