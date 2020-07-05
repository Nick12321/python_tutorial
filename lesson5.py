#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:42:22 2020

@author: nick
"""

#Branch control statements

x=4

if x == 5:
    print(" x = 5!")
elif x < 5:
    print(" x is less than 5!")
elif x > 5:
    print('x is greater than 5!')
    
# While loops

x=0
while x<=5:
    print(x)
    x+=1

print('-----------')
# same as for i in range(6):
for i in range(1,5+1):
    print(i)

print('-----------')

for i in range(5,-7,-2):
    print(i)

