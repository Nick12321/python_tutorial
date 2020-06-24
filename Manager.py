#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:34:50 2020

@author: nick
"""

from Employee import Employee

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
    