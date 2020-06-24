#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:33:14 2020

@author: nick
"""
"""
Class Person and Student have been moved to their own files. A new file called lesson3_main.py has been created and is now the main file.
This file has been deprecated.
"""


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
    
"""    
    print("------------------")
    p2=Person()
    print(p2)
    name2=p.get_name()
    age2=p.get_age()
    p2.set_name(name2)
    p2.set_age(age2)
    print(p2)
    p3=Person("Chad",100)
    print(p3)
    p4=Person(p.get_name(),p.get_age())
    print(p4)
"""
"""
    name2=str("Carol")
    print(name2)
    p=Person.set_name(input("type name: "))
    print(p)
"""
"""    
    p2=Person()
    print(p2)
    name2=Person.get_name(p)
    print(name2)
    age2=Person.get_age(p)
    p2=Person.set_name("Nick")
    p2=person.set_age(age2)
    #p2=Person.get_name(p), Person.get_age(p)
    print(p2)
"""    
main()



