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

#announce win, display tries
def winning_message(name, tries):
    print('Congratulations ' + name + ", you won in: " + str(tries) + ' tries.')
    
#announce loss
def loosing_message(name, tries):
    print('Try again ' + name + ', you didnt complete in 10 guesses.')

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
    verify_guess=int(verify_guess)
    actual_number=int(actual_number)
    if verify_guess < actual_number:
        return(0)
    if verify_guess > actual_number:
        return(1)
    if verify_guess==actual_number:
        return(2)

#main_game(number, )    
    
#main program logic
def main():
    main_name = welcome_message()
    main_number = random_num()
    tries = 1
    win = False
    while tries < 11:
        main_guess = guess_input()
        answer=guess_verify(main_guess, main_number)
        if answer==0:
            print("You're low!")
        if answer==1:
            print("Too high!")
        if answer==2:
            win=True
            winning_message(main_name, tries)
            break
        tries+=1
    if tries==10 and win==False:
        loosing_message(main_name, tries)
        

if __name__=="__main__":
    main()