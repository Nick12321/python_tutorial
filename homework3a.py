#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:46:17 2020

@author: nick
"""

class Employee:
    
    #initialize Employee
    def __init__(self, name="", age=0):
        self.name=name
        self.age=age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name=name
        
    def set_age(self, age):
        self.age=age
        
    def __str__(self):
        
        dout="Hello, " + self.name + " Our records indicate you are " + str(self.age) +" years old."
        return dout


# Manager class should handle profession, salary, and bonus
# Name and age should be derived from Employee
class Manager(Employee):
    #initialize Manager, using Inheritance from Employee
    def __init__(self, name, age, profession, salary, bonus):
        super().__init__(name, age)
        self.profession=profession
        self.salary=salary
        self.bonus=bonus
        
    def get_profession(self):
        return self.profession
    
    def get_salary(self):
        return self.salary
    
    def get_bonus(self):
        return self.bonus
    
    def set_profession(self, profession):
        self.profession = profession
        
    def set_salary(self, salary):
        self.salary = salary
    
    def set_bonus(self, bonus):
        self.bonus = bonus
        
    def __str__(self):
        sout=super().__str__()
        sout += "\n" + "You are a " + self.profession + " with a salary of: " + str(self.salary) + " and a bonus of: " + str(self.bonus);
        return sout
    
    
    
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

main()    
