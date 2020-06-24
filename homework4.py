#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:31:06 2020

@author: nick
"""


# 1. print out if a number is even, using just a print statement and an arithmetic operator
# 2. "" if a number is odd

num1=int(input("Type a number: "))
print(num1, " is even: ", (num1 % 2)==0)

"""
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
"""

# 3. Swap 2 number using arithmetic operators + and -

num2 = int(input("Enter a second number: "))
print("Number 1 was:", num1)
print("Number 2 was: ", num2)
num3=num1 + num2
num2=num3-num2
num1=num3-num1
print("Number 1 is now: ", num1)
print("Number 2 is now: ", num2)

# 4. Swap 2 numbers using bitwise operators xor^

#Python program to swap two variables without using third variable
print("----------------")
print(str(num1), " = ", str(num1), " ^ ", str(num2))
num1 = num1 ^ num2
print(str(num1), " = ", str(num1), " ^ ", str(num2))
num2=num1^num2
print(str(num1), " = ", str(num1), " ^ ", str(num2))
num1=num1^num2 #a = a ^ b
print(str(num1), " = ", str(num1), " ^ ", str(num2))

"""
a = a ^ b
b = a ^ b
a = a ^ b
"""
#printing the output
print("Swapped value of x is %d & y is %d" %(num1,num2))

# Multiply a number by 8 using a shift operator
#Make a string and replace the first letter with another letter
# Note: in combining the two exercises, replacing string components doesnt work
# because the size of the number changes. Need to search and replace.
s1 = "fact: " + str(num1) + " multiplied (x) by 8 (2^3) is: " + str(num1<<3) + "?"
print(s1)
s1 = "F" + s1[1:23] + "X" + s1[24:-1] + "!"
#s2 = s1[1:]
#s2 = "F" + s2[:-1] + "!"
print(s1)
#s1 = s1[:20] + "X" + s1[21:]
s2 = s1[:20]
s3 = s1[21:]
s4 = s3 + s2
print(s4)
