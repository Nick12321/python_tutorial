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

num_rows=2
num_columns=3
twoD_array=[[0 for i in range(num_columns)]for j in range(num_rows)]
print(twoD_array)

