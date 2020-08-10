#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:14:39 2020

@author: nick
"""


#Guess number between 1 & 100
# Track attempts, and display current games attempts and last games attempts

from guessing_game import Guessing_Game as gg
import random
max_number = 100
max_tries = 10


# welcome the player and explain the rules
def welcome_message():
    print('Welcome! You guess a number between 1 & 100, we tell you higher or lower.')
    print('You have 10 tries to get it right!')
    player_name = 'Sall'
    #player_name=input('Whats your name?: ')
    print('Welcome, ' + player_name)
    return player_name    

#announce win, display tries
def winning_message(name, tries):
    print('Congratulations ' + name + ", you won in: " + str(tries) + ' tries.')
    
#announce loss
def loosing_message(name, tries):
    print('Try again ' + name + ', you didnt complete in 10 guesses.')

    x=random.randint(1, max_number)+1
    return x
   
#get a guess from keyboard
def guess_input():
    player_guess=0
    try:
        player_guess = int(input('Guess a number: '))
    except ValueError:
        print('Invalid selection. Try again!')
        player_guess=guess_input()
    return player_guess
    

#check whether the guess is correct
def guess_verify(verify_guess, actual_number):
    actual_number=int(actual_number)
    if verify_guess < actual_number:
        return(0)
    if verify_guess > actual_number:
        return(1)
    if verify_guess==actual_number:
        return(2)

# Ask the player if they would like to play again
def play_another():
    again=input('Would you like to play again (y/n):')
    if again=='y':
        return True
    if again=='n':
        return False
    else:
        print('invalid selection')
        play_another()

#print final score
def final_score(name, tries):
    print('Thank you for playing, ' + name + '. Your final score(s):')
    i=0
    win_loss = [element[0] for element in tries]
    num_tries = [element[1] for element in tries]
    n=0
    print(str(0))
    t=(len(tries))
    print(str(t))
    
    while i<t:
        if win_loss[i]=='win':
            print("Won game " + str(i+1) + ' in ' + str(num_tries[i]) + ' attempts.')
        if win_loss[i]=='loss':
            print("Did not guess correct answer in game: " + str(i+1))
        n=n+num_tries[i]
        i+=1
    l=len(num_tries)
    print(str(n))
    print(str(l))
    print("You're average number of tries was: " + str(n/l))


# game logic and loop
def main_game(actual_number, name):
    tries = 1
    win = False
    while tries < 11:
        main_guess = guess_input()
        answer=guess_verify(main_guess, actual_number)
        if answer==0:
            print("You're low!")
        if answer==1:
            print("Too high!")
        if answer==2:
            win=True
            winning_message(name, tries)
            return win, tries
        if tries==10 and win==False:
            loosing_message(name, tries)
            return win, tries
        tries+=1

#main program logic
def main():
    p1=gg(welcome_message())
    score = []
    play_again=True
    while play_again==True:
        p1.set_game_stat = main_game(p1.return_random(), p1.get_name())
        play_again=play_another()
    final_score(p1.get_name(), p1.get_game_stat())
    

if __name__=="__main__":
    main()