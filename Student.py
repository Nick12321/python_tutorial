#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:39:24 2020

@author: nick
"""
from Person import Person

class Student(Person):
    #initialize Student
    def __init__(self, name, age, idnum):
        #super().__init__(name, age)
        Person.__init__(self, name, age)
        self.idnum=idnum
        
    #return idnum
    def get_id(self):
        return self.idnum
    
    #assign idnum
    def set_id(self, idnum):
        self.idnum=idnum
        
    #return student info as a string
    def __str__(self):
        #sout=Person.__str__(self)
        sout=super().__str__()
        sout += "\n" + "having student id#: " + str(self.idnum);
        return sout