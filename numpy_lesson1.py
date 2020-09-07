#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:27:30 2020

@author: nick
"""

import numpy as np

a=np.array([1,2,3,4,5])
print(np.shape(a))

b=np.array([[1,2,3,4], [4,5,6,7]])
print(np.shape(b))
print(b)
print(b.shape)

#address numpy ordinals with comma seperating 'set' then 'position'
b[0,0]=10
print(b)

x=b[1,-2]
print(x)

x=b[1,-1] # same as x=b[1,2] and x=b[1][2]
print(x)

x=b[1][2]
print(x)

#create 2 X 2 arrays of all zeros and all ones
#numbers are floats
a=np.zeros((2,2))
print(a)

a[0,1]=8
print(a)

c=np.ones((3,3))
print(c)
c[2,1]=9
print(c[2,1])
print(c)

#create 2 X 2 array with a particular value
a=np.full((2,2),5)
print(a)

#create an array with random values 0 to 1
a=np.random.random((2,2))
print(a)

#create an arra with sequence of 0 to 18 by step 2
a=np.arange(0,20,2)
print(a)

#create an array of even space bet/ a given range of values
#(divides 0 to 1 evenly by 5)
a=np.linspace(0,1,5)
print(a)

#create a 3 X 3 array with mean o and standard deviation 1
#for a specified array dimension
a=np.random.normal(0,1,(3,3))
print(a)

#concatenate 1 dimensional arrays together
x=np.array([1,2,3])
y=np.array([4,5,6])
a=np.concatenate([x,y])
print(a)

#Concatenate two dimensional arrays together
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[1,2,3],[4,5,6]])
b=np.concatenate([x,y])
print(b)

#Concatenate 2 dimensional arrays together (column wise)
#x=np.array([[1,2,3],[4,5,6]])
#y=np.array([[1,2,3],[4,5,6]])
#b=np.concatenate([x,y],axes=1)
#print(b)

#combining 2d array with 1d array w vstack
a=np.array([1,2,3])
b=np.array([[4,5,6],[7,8,9]])
x=np.vstack([b,a])
print(x)

#stack 1d array on left side of a 2d array w hstack
a=np.array([[1],[2]])
b=np.array([[4,5,6],[7,8,9]])
x=np.hstack([b,a])
print(x)

#split 1d array into 2d array using slice
a=np.array([1,2])
a=np.split(a,2)
print(a)

print(type(a))

#we can now use hstack more conveniently
b=np.array([[4,5,6],[7,8,9]])
x=np.hstack([b,a])
print(x)

#Numpy mathematical operations
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=a+b #or c=np.add(a,b)
print(c)

#subtract two arrays
c=b-a
c=np.subtract(a,b)
print(c)

#multiply two arrays
c=a*b
print(c)

#divide two arrays
c=a/b
print(c)

#square root a numpy array
c=np.sqrt(a)
print(c)

#matrix multiply two arrays (dot product)
c=np.matmul(a,b)
c=a@b
c=a.dot(b)
c=np.dot(a,b)
print(c)

#sum all element in an array
a=np.array([1,2,3,4,5])
s=np.sum(a)
print(s)

#compute sum of each column
#axis=0 means x column
a=np.array([[1,2],[3,4]])
s=np.sum(a, axis=0)
print(s)

#compute sum of each row
#axis=1 means y row
s=np.sum(a, axis=1)
print(s)

#transpose a 2dimensional array
c=a.T
print(c)

#inverse of a matrix
#linalg is a submodule of Numpy that provides additional math
c=np.linalg.inv(a)
print(c)

#add a column of 1's to an array
x=[1,2,3,4,5]
y=np.ones(5)
c=np.c_[x,y]
print(c)

#Numpy statistic operations
a=np.array([1,3,2])
print(a.min()) #minimum value
print(a.max()) #maximum value in array
print(a.argmin()) #index of min
print(a.argmax()) #index of max
print(a.mean()) #mean value of array
print(np.median(a)) #median value
print(a.std()) #standard deviation of array

#Median of 2 dimensional array
b=np.array([[1,2,3],[5,6,1]])
print(np.median(b))

#Median of 2 dimensional array along x axis
print(np.median(b, axis=0))

#median of two dimensional array along y axis
print(np.median(b,axis=1))