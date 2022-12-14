# Final Project:Checkers
# Module:game.py
# Student Name: Sapana Shrestha
# Student ID: 00710117
# Description: Game module that has Game class to manage the overall game, making use of the methods of the board class
# Python Version: 3.10.7
from Checkers.board import Board
class Game:
    
    # Default constructor for Game Class that initializes the two players names
    def __init__(self):
        self.Player1_Name =""
        self.Player2_Name=""
    
    #This fucntion takes the name input from the two players, and initiates the game between the two players
    def start_game(self):
        self.Player1_Name = input("Please Enter the Player 1's Name: ")#gets the name of the Player 1
        self.Player2_Name = input("Please Enter the Player 2's Name: ")#gets the name of the Player 2
        user_input = input("Begin game play? (Y/N) ").lower()
        while user_input not in ['y', 'n']:#iterates until user selected Y to play the Game or N to exit the game
            print("Invalid Choice!")
            user_input = input("Begin game play? (Y/N) ")
        if user_input == 'y':
            self.run_game()#runs the game between the two players if user inputs 'Y'

    #This function runs the game between the two players with the use of the Board class
    def run_game(self):
        self.board = Board(self.Player1_Name, self.Player2_Name)#instantiating the board object with the Board class
        self.board.init_board()#calling the function to initialize the 8X8 Checkers board
        self.board.create_board(0)#creates the board with values in respective grid squares
        is_Player1s_Turn = True#setting true for First Player
        while not self.board.is_game_over():#unless the game is not over, continue to play the game between the two players
            if is_Player1s_Turn:
                is_Player1s_Turn = False   
                self.board.move_a_piece(self.Player1_Name, 1)#moves a piece when the turn is of Player's 1
            else:
                is_Player1s_Turn = True
                self.board.move_a_piece(self.Player2_Name, 2)#moves a piece when the turn is of Player's 2

        if(self.board.is_game_over()):#check if the game is over
            print("\n***Game Over***\n")
            pieces_Player1 = self.board.get_pieces(1)#fetching number of pieces left for Player 1
            pieces_Player2 = self.board.get_pieces(2)#fetching number of pieces left for Player 2
            if(len(pieces_Player1)>len(pieces_Player2)):
                print(self.Player1_Name+' is the Winner!!!!')#if Player1 has more pieces than player 2, Player1 is the Winner
            else:
                print(self.Player2_Name+' is the Winner!!!!!')#if Player2 has more pieces than player 1, Player2 is the Winner

    #This function is used to write the rendered board to a text file for the active game  
    def file_board(self):
        self.file1 = open(self.file_name(self.Player1_Name), "w")
        self.file1.write(self.Player1_Name)
        self.file1.close()

        self.file2 = open(self.file_name(self.Player2_Name), "w")
        self.file2.write(f'{self.Player2_Name}')
        self.file2.close()