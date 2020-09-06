#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:37:47 2020

@author: nick
"""

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
print('Linear Regression using sklearn')
print('y = mx + b')
n = 1000 # number of points

# make random normal distribution x,y points
x, y = datasets.make_regression(n_samples=n, n_features=1, noise=10)

# split 80% of the data to the training set
# 20% of the data to test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5, random_state=0)

# make regression model
reg = LinearRegression()

# fit model with training data
reg.fit(x_train, y_train)

# retrieve slope and y-intercept b
m = reg.coef_
b = reg.intercept_

# calculate y prediction values
y_pred = reg.predict(x_test)

# plotting x,ydata as scatter plot
plt.scatter(x , y , color = "r", marker = "o", s = 5)
# plotting the regression line
plt.plot(x_test, y_pred, color = "b")
# title
plt.title('linear regression using sklearn')
# x,y labels
plt.xlabel('x')
plt.ylabel('y')
# show plot
plt.show()
# plot train and prediction data as histogram
plt.hist([y_test, y_pred], color=['orange', 'green'])
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['y ','y_pred'])
plt.title('y vs ypred')
plt.show()