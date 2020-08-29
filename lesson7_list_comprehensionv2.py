#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:20:56 2020

@author: nick
"""
#List Comprehension
new_list=[i for i in range(10)]
print(new_list)

new_list=[i*i for i in range(10)]
print(new_list)

even_squares=[x*x for x in range(10) if x%2==0]
print(even_squares)

#to do - list comprehension to print odd number squares
odd_squares=[x*x for x in range(10) if x%2!=0]
print(odd_squares)

old_list=[1,2,3,4,5]
new_list=[x*2 for x in old_list]
print(new_list)

new_list=[x*2 for x in old_list if x%2==0]
print(new_list)

new_list=[x*2 for x in old_list if x%2!=0]
print(new_list)

new_list=[(x,x*2) for x in old_list]
print(new_list)

new_list=[(x,x*2) for x in old_list if x%2==0]
print(new_list)

#create one dimensional array with 3 0 values
oneD_array=[0 for i in range(3)]
print(oneD_array)

#create two dimensional array with preset values
num_rows=2
num_columns=3
twoD_array=[[0 for i in range(num_columns)]for j in range(num_rows)]
print(twoD_array)

#use list comprehension to sort values
mixed_list=['a', 3, 'b', 5]
sorted_list=sorted([str(x) for x in mixed_list])
print(sorted_list)

#use list comprehension to remove '\n' from a list of strings
list1=['cat\n', 'dog\n', 'lion\n']
print(list1)
list2=[x.replace('\n',"") for x in list1]
print(list2)

#Iterator and next functions

class Squares:
    def __iter__(self):
        self.x=1
        return self

    def __next__(self):
        if self.x<=10:
            x=self.x
            self.x+=1
            return x*x
        else:
            raise StopIteration
        
itr=iter(Squares())
for x in itr:
    print(x)
print("HERE!--------------------------------")

#simple Generator
def simpleGenerator():
    yield 1200
    
result=simpleGenerator()

for x in result:
    print(x)

#Square generator
def squareGenerator():
    for x in range(10):
        yield x*x

result=squareGenerator()

for x in result:
    print(x)

#Zip compress values together from seperate lists
#uneven elements get dropped
numbers=[1,2,3,4,5]
letters=['a', 'b', 'c', 'Gerry', 'Tom', 'Karen']
zipped=zip(numbers, letters)
zipped=list(zipped)
print(zipped)

for x in zipped:
    print(x)
    
list1=[i for i,j in zipped]
list2=[j for i,j in zipped]
print(list1)
print(list2)

print(*zipped)
unzipped=zip(*zipped)
unzipped=list(unzipped)
print(unzipped)

#Higher order functions
list1=[1,2,3,4,5]

def f(x):
    return x + 1

#map function returns an iterator of the function and the list
itr = map(f, list1)
list2=list(itr)
print(list2)

#same result as following for loop
list1=[1,2,3,4,5]
list2=[]
for i in list1:
    list2.append(f(i))
print(list2)

#To Do: make a square function and use map to square the numbers

list1=[1,2,3,4,5,6,7,8,9,10]
def f(x):
    return x*x
itr=map(f, list1)
list2=list(itr)
print(list2)

#Lambda functions
list1=[1,2,3,4,5,6]
itr=map(lambda y: y+1, list1)
print(list(itr))

#To Do: make a lambda square function using map
itr=map(lambda z: z*z, list1)
print(list(itr))

# Filter operates like map, but returns iterator if values meet specific criteria

def even(x):
    return x%2==0

itr=filter(even, list1)
print(list(itr))

#Filter with lambda function
itr=filter(lambda m: m%2==0, list1)
print(list(itr))

#To Do:Make an odd function and use filter to print out odd numbers
def odd(x):
    return x%2!=0

itr=filter(odd, list1)
print(list(itr))

# Use the filter function and a lambda function to print odd numbers
itr=filter(lambda x: x%2!=0, list1)
print(list(itr))

#Use map, filter, and lambda to print all even squared numbers

itr=filter(lambda x:x%2==0, map(lambda x:x*x, list1))
print(list(itr))

# Reduce takes the first two numbers of a list, applies a function to them
#then continue applying function to them
def add(x,y):
    return x+y

from functools import reduce
list1=[1,2,3,4,5,6]
list2=reduce(add, list1)
print(list2)

list2=reduce((lambda x,y: x+y), list1)
print(list2)

#To Do - apply reduce function on a function that multiplies two numbers together

def multiply(x,y):
    return x*y

list3 = reduce(multiply, list1)
print(list3)

#Recursion
def multn(n):
    if n==0:
        return 1
    else:
        return multn(n-1)*n
x=multn(5)
print(x)

def pown(b,n):
    if(n==0):
        return 1
    else:
        return pown(b,n-1)*b

x=pown(2,3)
print(x)

#Recursion -summing all numbers in a sequence

def seqn(n):
    if(n==0):
        return 0
    else:
        x=(n*(n+1))/2
        print(x)
        return x+seqn(n-1)

x=seqn(5)
print(x)

#Recursion - Fibonacci Sequence

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
x=fib(10)
print(x)

#Combinations: num of combinations for n letters
# and r choices (out of 5 letters, # of combo of 2)
def combinations(n,r):
    if r==0 or n==r:
        return 1
    else:
        return combinations(n-1, r) + combinations(n-1, r-1)
print(combinations(15,3))

#Recursion - Print words in reverse, or forwards
#depending on where print statement is.
def print_reverse(s,n):
    if n==0:
        print('\n')
    else:
        print(s[n-1], end='')
        print_reverse(s, n-1)
        #print(s[n-1], end='')
s='asjkdhjkafdhaskjfhaskj'
print_reverse(s,len(s))
#print('\n')

#Palindrome - recursive function returns True / False
def is_palindrome(s,i,j):
    if i>=j:
        return True
    else:
        if s[i] != s[j]:
            return False
        else:
            return is_palindrome(s, i+1, j-1)

s='radar'
print(is_palindrome(s, 0, len(s)-1))
s='asjkdhjkafdhaskjfhaskjjksahfjksahdfakjhdkjsa'
print(is_palindrome(s, 0, len(s)-1))
s='da da da'
print(is_palindrome(s, 0, len(s)-1))

#Permutations
# print permutations of string s
def print_permutations(s, i, j):
    # print out permutation
    if i == j:
        print(s)
    else:
        for k in range(i, j+1):
            # swap i and k
            c = s[i]
            # s[i] = s[k]
            s = s[:i] + s[k] + s[i+1:]
            #s[k] = c
            s = s[:k] + c + s[k+1:]

            # recursive call
            print_permutations(s, i + 1, j)
            # put back, swap i and k

            c = s[i]
            #s[i] = s[k]
            s = s[:i] + s[k] + s[i+1:]
            #s[k] = c;
            s = s[:k] + c + s[k+1:]
s='ABC'
print_permutations(s, 0, len(s)-1)

#Combinations
def print_combinations(s, combs, start, end, n, r):
    if n==r:
        for j in range(r+1):
            print(combs[j],end="")
        print("")
        return
    #replace n with all possible elements
    i=start
    while(i<=end and end -i +1 >= r-n):
        combs=combs[:n] + s[i] + combs[n+1:]
        print_combinations(s, combs, i+1, end, n+1, r)
        i+=1

print('\n')
#Combinations

s="ABCDE"
combs=" " * (len(s)+1)
print_combinations(s, combs, 0, len(s)-1, 0, 1)

print_combinations(s, combs, 0, len(s)-1, 0, 2)

print_combinations(s, combs, 0, len(s)-1, 0, 3)
print_combinations(s, combs, 0, len(s)-1, 0, 4)
print_combinations(s, combs, 0, len(s)-1, 0, 5)

#To Do: recursive reverse string
#this one works:
def reverse_string(s, n):
    if n==0:
        print('\n')
    else:
        print(s[n-1])
        n-=1
        reverse_string(s, n)
s='abcdefghijklmnop'
reverse_string(s, len(s))

#Get one that prints to a string
def reverse_string(s,n):
    if n==0:
        return s[0]
    else:
        return s[n] + reverse_string(s,n-1)

s='tomorrow'
print(reverse_string(s, len(s)-1))

#Write function that searches for a number in a list and returns
# True if found, or False if not found.

def search_digit(s,i,j):
    if j<0:
        return False
    else:
        if s[j] == i:
            return True
        else:
            return search_digit(s, i, j-1)

s=[1,2,3,4,5,6,7,8,9]
print(search_digit(s, 1, len(s)-1))

print('here!-------------------')
#Another way of searching for number
def search_digit(d, x):

     if d == 0:
          return False

     elif d % 10 == x:
         print(d%10)
         return True

     else:
         print(d//10)
         return search_digit(d//10,x)

print(search_digit(12346789,8))
print(search_digit(12346789,5))

#recursive function that recieves list of digits of any length and adds them
# example: sum_digits(1234) = 10

def sum_digits(d):
     if d == 0:
          return 0
     else:
          return sum_digits(d//10) + d % 10

print(sum_digits(123456789))

