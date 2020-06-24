#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:02:03 2020

@author: nick
"""


def welcome():
    print("Hello World!")
    
def enter_name():
    name=input("what is your name?")
    return name

def enter_age():
    age=int(input("What is your age?"))
    return age

def print_person(name3, age3):
    print("Nice to meet you", name3)
    print(name3, "You are", age3, "years old")
    
def main():
    welcome()
    name2=enter_name()
    age2=enter_age()
    print_person(name2, age2)
    
main()
    