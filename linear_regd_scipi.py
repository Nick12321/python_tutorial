#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:41:29 2020

@author: nick
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

print('Linear Regression using scipy')
print('y=mx + b')
#number of points
n=10

#make random normal distribution x,y points
#mean, std, size
x=np.random.normal(0,1,n)
y=np.random.normal(0,.25,n)

#straight line function y=f(x)
def f(x,f,b):
    return m*x+b

#data x,y to fit
m,b = curve_fit(f,x,y)

#calculate y2=mx+b
y2=m[0]*x + b[0,1]

#plot regression line using scatter plot
plt.scatter(x,y, color='r', marker='o', s=30)
#axis dimensions
plt.axis([-1,1,-1,1])
#plotting the regression line
plt.plot(x, y2, color='b')
plt.title('linear regression using scipy')
#x,y labels
plt.xlabel('x')
plt.ylabel('y')
plt.show()