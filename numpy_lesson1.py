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

