#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:46:17 2020

@author: nick
"""

class Employee:
    
    #initialize Employee
    def __init__(self, profession="", salary=0):
        self.profession=profession
        self.salary=salary
        
    def get_profession(self):
        return self.profession
    
    def get_salary(self):
        return self.salary
    
    def set_profession(self, profession):
        self.profession=profession
        
    def set_salary(self, salary):
        self.salary=salary
        
    def __str__(self):
        #print("-------------")
        #print(type(self.salary))
        #amount=str(self.salary)
        #print("You are a " + self.profession + "making " + amount)
        dout="You are a " + self.profession + "\n"
        dout += "you make " + str(self.salary) + " annually"
        #sout="You are a " + self.profession + "making " str(self.salary)
        return dout

class Manager(Employee):
    #initialize Manager, using Inheritance from Employee
    def __init__(self, )
       

def enter_profession():
    profession=input("Pls enter your profession:")
    return profession

def enter_salary():
    salary=int(input("Pls enter your salary:"))
    return salary

def main():
    profession=enter_profession()
    salary=enter_salary()
    e1=Employee(profession, salary)
    print("-------------")
    print(e1)

main()    
