#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:33:14 2020

@author: nick
"""

from Person import Person
from Student import Student


#function to print a welcome message
def welcome():
    print("Hello world!")
    
#function to read a name from the keyboard and return the value
def enter_name():
    name=input("Please type your name: ")
    # name="Todd"
    return name

#function to read an age from the keyboard and return the value
def enter_age():
    age=int(input("How old are you? "))
    # age=int(12)
    return age

#function to enter student ID number
def enter_id():
    student_yn=input("Are you a student (y/n):")
    if student_yn=="y":
        idnum=int(input("Enter your Student Number: "))
    elif student_yn=="n":
        idnum=0
    else:
        print("Invalid selection")
        enter_id()
    return idnum

def main():
    welcome()
    name=enter_name()
    age=enter_age()
    idnum=enter_id()
    print(idnum)
    p=Student(name, age, idnum)
    print(p)

if __name__=="__main__":
    main()



