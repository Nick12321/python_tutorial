#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:27:30 2020

@author: nick
"""

import numpy as np

a=np.array([1,2,3,4,5])
print(np.shape(a))

b=np.array([[1,2,3], [4,5,6]])
print(np.shape(b))
print(b)
print(b.shape)

#address numpy ordinals with comma seperating set then position
b[0,0]=10
print(b)

x=b[1,-2]
print(x)

x=b[1,-1] # same as x=b[1,2]
print(x)