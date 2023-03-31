#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 02:30:48 2022

@author: walihyder
"""
"""Simulating the dice game Craps."""
import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

wins = {}
losses = {}

for i in range(1_000_000):
    # determine game status and point, based on first roll
    die_values = roll_dice()  # first roll
    sum_of_dice = sum(die_values)
    rolls = 1

    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        rolls += 1
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'
    
    #display "wins" or "loses" message
    if rolls > 25:
        rolls = 25
        
        if game_status == 'WON':
            wins[rolls] = wins[rolls] + 1 if rolls in wins else 1
        else:
            losses[rolls] = losses[rolls] + 1 if rolls in losses else 1
                                       
# display number of wins and losses on all rolls

# calculate chances of winning
total_games = sum(wins.values()) + sum(losses.values())
total_wins = sum(wins.values())
total_losses = sum(losses.values())
print(f'\nPercentage of wins= {total_wins / total_games:.2%}')
print(f'Percentage of losses= {total_losses / total_games:.2%}')
print ("Percentage of wins/losses based on total number of rolls")
print ("\nRolls \t% Resolved on this roll\tCumalative % of games resolved")


for i in range(1,26):
    games_resolved = wins.get(i, 0) 
    #p_games_resolved = games_resolved / total_games  
    print(f'{i:>5}{games_resolved}')
    

