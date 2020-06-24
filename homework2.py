#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:17:09 2020

@author: nick
"""


def welcome():
    print("Another Hello World!")
    
def enter_profession():
    name=input("What is your name?")
    profession=input("What is your profession?")
    return(name, profession)

def enter_salary():
    salary=int(input("What is your salary?"))
    return(salary)

def print_person(name, profession, salary):
    print(name, "You are a", profession, "and you make", salary, "per year")
    
def main():
    welcome()
    name, profession=enter_profession()
    salary=enter_salary()
    print_person(name, profession, salary)
    
main()
