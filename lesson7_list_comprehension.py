#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:20:56 2020

@author: nick
"""
#List Comprehension
new_list=[i for i in range(10)]
print(new_list)

new_list=[i*i for i in range(10)]
print(new_list)

even_squares=[x*x for x in range(10) if x%2==0]
print(even_squares)

#to do - list comprehension to print odd number squares
odd_squares=[x*x for x in range(10) if x%2!=0]
print(odd_squares)

old_list=[1,2,3,4,5]
new_list=[x*2 for x in old_list]
print(new_list)

new_list=[x*2 for x in old_list if x%2==0]
print(new_list)

new_list=[x*2 for x in old_list if x%2!=0]
print(new_list)

new_list=[(x,x*2) for x in old_list]
print(new_list)

new_list=[(x,x*2) for x in old_list if x%2==0]
print(new_list)

#create one dimensional array with 3 0 values
oneD_array=[0 for i in range(3)]
print(oneD_array)

#create two dimensional array with preset values
num_rows=2
num_columns=3
twoD_array=[[0 for i in range(num_columns)]for j in range(num_rows)]
print(twoD_array)

#use list comprehension to sort values
mixed_list=['a', 3, 'b', 5]
sorted_list=sorted([str(x) for x in mixed_list])
print(sorted_list)

#use list comprehension to remove '\n' from a list of strings
list1=['cat\n', 'dog\n', 'lion\n']
print(list1)
list2=[x.replace('\n',"") for x in list1]
print(list2)

#Iterator below does not work. Have asked Ed for clarification
"""
class Squares:
    def __iter__(self):
        self.x=1
        return self

def __next__(self):
    if self.x<=10:
        x=self.x
        self.x+=1
        return x*x
    else:
        raise StopIteration
        
itr=iter(Squares())
for x in itr:
    print(x)
"""
#simple Generator
def simpleGenerator():
    yield 1200
    
result=simpleGenerator()

for x in result:
    print(x)

#Square generator
def squareGenerator():
    for x in range(10):
        yield x*x

result=squareGenerator()

for x in result:
    print(x)

#Zip compress values together from seperate lists
#uneven elements get dropped
numbers=[1,2,3,4,5]
letters=['a', 'b', 'c', 'Gerry', 'Tom', 'Karen']
zipped=zip(numbers, letters)
zipped=list(zipped)
print(zipped)

for x in zipped:
    print(x)
    
list1=[i for i,j in zipped]
list2=[j for i,j in zipped]
print(list1)
print(list2)

print(*zipped)
unzipped=zip(*zipped)
unzipped=list(unzipped)
print(unzipped)

#Higher order functions
list1=[1,2,3,4,5]

def f(x):
    return x + 1

#map function returns an iterator of the function and the list
itr = map(f, list1)
list2=list(itr)
print(list2)

#same result as following for loop
list1=[1,2,3,4,5]
list2=[]
for i in list1:
    list2.append(f(i))
print(list2)

#To Do: make a square function and use map to square the numbers

list1=[1,2,3,4,5,6,7,8,9]
def f(x):
    return x*x
itr=map(f, list1)
list2=list(itr)
print(list2)
