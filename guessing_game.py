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
        self.player_record=[]
        self.name = name
        self.tries=0

    #get random number
    def return_random(self):
        max_number=100
        self.random_num=random.randint(1, max_number)+1
        return self.random_num    
    
    #get name
    def get_name(self):
        return self.name
    
    #recieve two variables (tuple???), record game win/loss and # of tries
    def set_game_stat(self, win, tries):
        self.player_record.append(win, tries)
        
    #compare guess to random number            
    def check_guess(self, guess):
        self.guess=int(guess)
        if self.guess < self.random_num:
            return(0)
        if self.guess > self.random_num:
            return(1)
        if self.guess==self.random_num:
            return(2)
    
    #set new game tries = 0
    def new_game(self):
        self.tries = 0
        
    #set number of tries
    def add_tries():
        self.tries=self.tries+1
    
    #get number of tries
    def get_tries():
        return (self.tries)
    
    
        
        
    
    
        