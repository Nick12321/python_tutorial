#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:31:10 2020

@author: nick
"""


#Dictionary work
# Create two dictionaries, one with name / animal type, and the other with animal type / sound
# Get user to input animal name, and provide a sentence describing the animal type and sound.


d1={'Harley':'dog'}
d1["Chleo"] = 'lion'
d1['Tigress'] = 'tiger'
d2={'dog':'barks', 'lion':'roars', 'tiger':'grunts'}
print(d2.keys())
print(d1.values())


def get_name():
    animal_name="Chleo"
    #animal_name=input("Name of the animal you would like to know about? ")
    return(animal_name)

def print_info(animal_name, animal_type, animal_sound):
    print(animal_name + " is a " + animal_type + " that " + animal_sound + ".")
    #following line creates a list from d1 keys, and the ordinal comes from 'index'.
    #print(list(d1.keys())[list(d1.values()).index(animal_type)])

def get_type(animal_name):
    animal_type=d1[animal_name]
    return animal_type

def get_sound(animal_type):
    animal_sound=d2[animal_type]
    return(animal_sound)
       
animal_name=get_name()
animal_type=get_type(animal_name)
animal_sound=get_sound(animal_type)
print_info(animal_name, animal_type, animal_sound)

print(list(d1.values()).index('tiger'))
 