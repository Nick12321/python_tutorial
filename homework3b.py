#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:46:17 2020

@author: nick
"""
from Employee import Employee
from Manager import Manager
   
def enter_name():
    name=input("Please enter your name: ")
    return name

def enter_age():
    age=int(input("Enter your age: "))
    return age

def enter_profession():
    profession=input("Pls enter your profession: ")
    return profession

def enter_salary():
    salary=int(input("Pls enter your salary: "))
    return salary

def enter_bonus():
    bonus = int(input("Please enter your bonus: "))
    return bonus

def main():
    name = enter_name()
    age = enter_age()
    profession=enter_profession()
    salary=enter_salary()
    bonus=enter_bonus()
    e1=Manager(name, age, profession, salary, bonus)
    print("-------------")
    print(e1)

if __name__=="__main__":
main()    
