#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:33:50 2020

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
