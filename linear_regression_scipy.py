#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:15:46 2020

@author: nick
"""

import numpy as np 
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

print('Linear Regression using scipy')
print('y = mx + b')

n = 10 # number of points

# make random normal distribution x,y points
# mean , std, size
x = np.random.normal(0,1,n)
y = np.random.normal(0,.25,n)

# straight line function y = f(x)

def f(x, m, b):
    return m*x + b

# y2 = mx + b
m, b = curve_fit(f, x, y) # your data x, y to fit

# calculate y2 = mx + b
y2 = m[0]*x + b[0,1]

# plot regression line
# plotting as scatter plot
plt.scatter(x, y, color = "r", marker = "o", s = 30)

# axis dimensions
plt.axis([-1, 1, -1, 1])

# plotting the regression line
plt.plot(x, y2, color = "b")

# title
plt.title('linear regression using scipy')

# x,y labels
plt.xlabel('x')
plt.ylabel('y')

# show plot
plt.show() 