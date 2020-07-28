#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:14:39 2020

@author: nick
"""


#Guess number between 1 & 100
# Track attempts, and display current games attempts and last games attempts

import random
max_number = 100
max_tries = 10


# welcome the player and explain the rules
def welcome_message():
    print('Welcome! You guess a number between 1 & 100, we tell you higher or lower.')
    print('You have 10 tries to get it right!')
    #player_name=input('Whats your name?: ')
    player_name = 'Nick'
    print('Welcome, ' + player_name)
    return player_name    
    
#generate a random number
def random_num():
    x=random.randint(1, max_number)+1
    return x

   
#get a guess from keyboard
def guess_input():
    player_guess = input('Guess a number: ')
    return player_guess



#check whther the guess is correct
def guess_verify(verify_guess, actual_number):
    verify_guess=str(verify_guess)
    actual_number=str(actual_number)
    if verify_guess < actual_number:
        return(0)
    if verify_guess > actual_number:
        return(1)
    if verify_guess==actual_number:
        return(2)
    
    
#print score
def print_score():
    z=1
    
#main program logic and loop
def main():
    tries = 0
    main_name = welcome_message()
    main_number = random_num()
    while tries < 10:
        main_guess = guess_input()
        answer=guess_verify(main_guess, main_number)
        if answer==0:
            print("You're low!")
        if answer==1:
            print("Too high!")
        if answer==2:
            print("You won!")
            break
        tries+=1
        
        
    
    print('Number is: ' + str(main_number))
    

if __name__=="__main__":
    main()