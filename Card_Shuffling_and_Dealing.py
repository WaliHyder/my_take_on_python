"""
Created on Tue Nov  1 10:51:05 2022

@author: walihyder
"""

import random

faces = ['Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']



def initialize_deck():
    deck = [(faces[i % 13], suits[i // 13]) for i in range(52)] #list of tuples 
    random.shuffle(deck)  #shuffle
    return deck

#call the function 
deck = initialize_deck() 

for i, (faces, suits) in enumerate(deck): 
    card = faces + ' of ' + suits
    print(f'{card:19}',end='')
    if (i+1)%4 ==0:
        print()