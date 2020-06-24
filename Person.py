#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:40:20 2020

@author: nick
"""

"""
Person class to store a person's name and age
"""

# define a class person

class Person:
    
    # initialize Person
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        
    # return name
    def get_name(self):
        return self.name
    
    # return age
    def get_age(self):
        return self.age
        
    # assign name
    def set_name(self, name):
        self.name = name
        
    # assign age
    def set_age(self, age):
        self.age = age

    ## return person info as a string
    def __str__(self):
        sout="Nice to meet you " + self.name + "\n"
        sout += self.name + ", you are " + str(self.age) + " years old"
        return sout
