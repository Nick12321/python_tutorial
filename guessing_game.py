#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:07:07 2020

@author: nick
"""
###make import statements in homework5_8.py

# Make Guess_Game class to store guess number, tries per game.
# method to generate random number, check guess (low or high)
# Game__init__ generate and store random number, and empty list for tries
# Guess_Game will store info

import random

class Guessing_Game:
    
    #initialize class
    def __init__(self, name):
        max_number=100
        self.random_num=random.randint(1, max_number)+1
        self.tries=[]
        self.name = name
        
    #name getter
    def get_name():
        return self.name
    
    #compare guess to random number            
    def check_guess(self, guess):
        self.guess=int(guess)
        if self.guess < self.random_num:
            return(0)
        if self.guess > self.random_num:
            return(1)
        if self.guess==self.random_num:
            return(2)
    
    #getter for random_num
    def return_random(self):
        return self.random_num
    
    #set new game tries = 1
    def new_game(self):
        self.tries = 1
        
    #keep track of number of tries
    def 
    
    
        