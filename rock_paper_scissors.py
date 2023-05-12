#!/usr/bin/python3

import numpy as np
from numpy import random

################# Rules  ###################
#  Rock beats Scissors
#  Paper beats Rock
#  Scissors beats Paper
############################################

def RPS():
    choices = {1: "rock",
               2: "paper",
               3: "scissors"
               }
    
    play = True
    while play:
        print("") ## Entering newline before input
        user_choice = input('Enter "Rock, Paper, Scissors, or Quit (R/P/S/Q): ')
        comp_choice = choices[np.random.randint(1,4)]
        
        if user_choice.lower() == "q" or user_choice.lower() == "quit" or user_choice.lower() == "quite":
            print("\nBye then!")
            break
        elif user_choice.lower() == "r" or user_choice.lower() == "rock":
            user_choice = "rock"
        elif user_choice.lower() == "p" or user_choice.lower() == "paper":
            user_choice = "paper"
        elif user_choice.lower() == "s" or user_choice.lower() == "scissors":
            user_choice = "scissors"
        else:
            print(f'\nInvalid input ({user_choice}), please choose again: ')
            continue
        
        print(f'\nYou chose {user_choice}, and I chose {comp_choice}.')

        if user_choice == "rock" and comp_choice == "paper":
            print("I won! Let's play again!")
        elif user_choice == "rock" and comp_choice == "scissors":
            print(f"You won! Let's play again!")
        elif user_choice == "rock" and comp_choice == "rock":
            print(f"Draw, let's play again!")

        elif user_choice == "paper" and comp_choice == "paper":
            print(f"Draw, let's play again!")
        elif user_choice == "paper" and comp_choice == "rock":
            print(f"You won! Let's play again!")
        elif user_choice == "paper" and comp_choice == "scissors":
            print(f"I won! Let's play again!")

        elif user_choice == "scissors" and comp_choice == "scissors":
            print(f"Draw, let's play again!")
        elif user_choice == "scissors" and comp_choice == "rock":
            print(f"I won! Let's play again!")
        elif user_choice == "scissors" and comp_choice == "paper":
            print(f"You won! Let's play again!")

        else:
            print("Error in finding winner.  Pleaes contact coder.")

        print("") # adding a new line before input
        again = input("Do you want to play again? (Y/N) ")
        if again.lower() == "y" or again.lower() == "yes":
            play = True
        elif again.lower() == "n" or again.lower() == "no":
            play = False
            print("Bye then!")
        else:
            print(f"You entered {again}. Please only choose 'yes', 'no', 'y', or 'n'.")

RPS()



    

    