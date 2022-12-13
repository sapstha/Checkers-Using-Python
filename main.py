# Final Project:Checkers
# Module: main.py
# Student Name: Sapana Shrestha
# Student ID: 00710117
# Description: main module for implementation of Checkers Game in python
# Python Version: 3.10.7
from Checkers.game import Game#all th classes are stored inside the Checkers folder

def game_menu():
    print("\n****Welcome to CHECKERS****\n")
    user_choice=int(input("1. Play Game\n2. View Rules\n3. Exit\n:"))#Displaying available options to the players
    if(user_choice==1):#executes if the user select the option to play the game        
        game_obj = Game()# creating the game Object to instantiate the game class
        game_obj.start_game()#calling the function to start the game between two players
    elif user_choice==2:#executes if the user select the option to view the game rules   
        gameRules="\n-Two Players can play the 8X8 Checker Games.\n-The unoccupied grid squares are denoted by either \'R' or \'B'.\n"
        gameRules+="-The Players pieces are displayed as \'x' or \'o'. \n-One need to enter the row and column position to make the "
        gameRules+="piece move,\n-The input format should be for example: C-2,D-1.\n-A piece can move only on unoccupied location diagonally.\n"
        gameRules+="-Pieces can move only forward,not backward"
        print(gameRules)
    elif user_choice==3:#executes if the user select the option to exit the game 
        print("\nThank You For Using the Program!\n")
        exit()
    else:
        print("\nInvalid Choice!Please enter valid option.\n")
        game_menu()
    

while(True):
    game_menu()#loops until user exits from the game