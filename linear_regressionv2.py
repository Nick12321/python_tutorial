#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:01:26 2020

@author: nick
"""

"""
linearRegression.py
"""
import numpy as np
import matplotlib.pyplot as plt
print('Linear Regression')
print('y = mx + b')
n = 10 # number of points
# make random normal distribution x,y points
# mean , std, size
x = np.random.normal(0,1,n)
y = np.random.normal(0,.25,n)
# y2 = mx + b

# calculate m
# ( Σ y )( Σ x^2) – (Σ x) (Σ x y )
# m = -----------------------------
# n ( Σ x^2) - ( Σ x)^2
top = (np.sum(y)*np.sum(x*x) - np.sum(x) * np.sum(x*y))
bottom = (n * np.sum(x*x) - np.sum(x) * np.sum(x))
m=top/bottom
print('m = ',m)

# calculate b
# n ( Σ x y ) – (Σ x) (Σ y )
# b = ------------------------------------------
# n ( Σ x^2) - ( Σ x)^2
top = ( n * np.sum(x*y) - np.sum(x) * np.sum(y))
bottom = (n * np.sum(x*x) - np.sum(x) * np.sum(x))
b = top / bottom
print('b = ',b)
# calculate y2 = mx + b
y2 = m*x + b

# plot regression line
# plotting as scatter plot
plt.scatter(x, y, color = "r", marker = "o", s = 30)
# set x-y axis dimensions
plt.axis([-1, 1, -1, 1])
# plotting the regression line
plt.plot(x, y2, color = "b")
# title
plt.title('linear regression')

# x,y labels
plt.xlabel('x')
plt.ylabel('y')
# show plot
plt.show()