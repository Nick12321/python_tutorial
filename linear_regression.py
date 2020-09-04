#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:36:50 2020

@author: nick
"""

import numpy as np
import matplotlib.pyplot as plt

print('Linear Regression')
print('y=mx+b')

n=30
#make random normal distribution points for x,y
#mean, std, size

x=np.random.normal(0,1,n)
y=np.random.normal(0,.25,n)

#y2=m*x+b

plt.scatter(x,y, color='r', marker='o', s=30)
plt.plot(x,y,color='b')

#calculate m

top=(np.sum(y)*np.sum(x*x)-np.sum(x)*np.sum(x*y))
bottom=(n*np.sum(x*x)-np.sum(x)*np.sum(x))
m=top/bottom
print('m = ', m)

#calculate b

top=(n*np.sum(x*y) - np.sum(x)*np.sum(y))
bottom=(n*np.sum(x*x) - np.sum(x)*np.sum(x))
b=top/bottom
print('b = ',b)

#calculate y2=mx + b
y2 = m*x + b

#plot regression line

#plotting as scatter plot
plt.scatter(x,y, color='r', marker='o', s=30)

#set x-y axis dimensions
plt.axis([-1,1,-1,1])

#plotting regression line
plt.plot(x, y2, color='b')

#title
plt.title('linear regression')

#x,y labels
plt.xlabel('x')
plt.ylabel('y')

#show plot
plt.show()