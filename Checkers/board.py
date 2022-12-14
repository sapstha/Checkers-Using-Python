# Module: board.py
# Student Name: Sapana Shrestha
# Student ID: 00710117
# Description: board module consisting of the Board class
# Python Version: 3.10.7
import datetime
from Checkers.pieces import Piece
from Checkers.constants import ROWS,COLS#improting the constants from constant.py module
class Board:

    # Default constructor for Board class that initializes names of Player1 and Player2
    def __init__(self, player_1, player_2):
        self.selectedPieces = []
        self.Player1_Name= player_1
        self.Player2_Name = player_2

        '''Here, two files for each Player is created where all the moves made by them gets stored.
        File Name is created using name of the Player, and the date the game is played.'''
        self.file_1 = open(f'{str(self.file_header(self.Player1_Name))}.txt', "w")#creates or opens the file in witten mode
        self.file_1.write('Player '+self.Player1_Name+' Moves:\n')#Writing the Player 1s Name to the file

        self.file_2 = open(f'{str(self.file_header(self.Player2_Name))}.txt', "w")
        self.file_2.write('Player '+self.Player2_Name+' Moves:\n')#Writing the Player 2s Name to the file

    #This function returns the file name consisting the name of the Players, along with the date and the time the game is played
    def file_header(self,name_of_player):
        now = datetime.datetime.now()#get the present date the game is played
        return str(name_of_player + "_" + now.today().strftime('%d_%m_%Y %H.%M.%S %p'))#concatenating the day,month,year,hour,minute,seconds to the Player Name

    # This function initializes and declares the board
    def init_board(self):
        self.board = [['temp' for i in range(ROWS)] for _ in range(COLS)]
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) %2 != 0:
                    if row < 3:
                        self.selectedPieces.append(Piece(row,col,'x'))#assign piece x to square grid in rows 0,1,2
                    elif row >= 5:
                        self.selectedPieces.append(Piece(row,col,'o'))#assign piece o to square grid in rows 5,6,7
                    self.board[row][col] = 'B'#assign value B(Black) for unoccupied grid squares.
                else:
                    self.board[row][col] = 'R'#assign value R(Red) for unoccupied grid squares.
    
    ''' This function displays the board according to the changing position of the pieces.
    Also, the varying board structure is stored in the file. All the moves made by the Player 1 is stored
    in file_1 and all the moves made by the Player 2 is stored in the file_2 in a grid format'''
    def create_board(self,player_number):
        rows = ['A','B','C','D','E','F','G','H']#labelling the rows
        print(' ',end='   ')
        if player_number==0:
            self.file_1.write('    ')
            self.file_2.write('    ')
        if player_number==1:
            self.file_1.write('    ')
        if player_number==2:
            self.file_2.write('    ')
        for i in range(8):#labeling the columns
            print(i+1, end='   ')
            if player_number==0:
                self.file_1.write(str(i+1)+'   ')
                self.file_2.write(str(i+1)+'   ')
            if player_number==1:
                self.file_1.write(str(i+1)+'   ')
            if player_number==2:
                self.file_2.write(str(i+1)+'   ')

        print()
        if player_number==0:
                self.file_1.write('\n')
                self.file_2.write('\n')
        if player_number==1:
                self.file_1.write('\n')
        if player_number==2:
                self.file_2.write('\n')
        for row in range(8):
            print(rows[row], end = ' | ')
            if player_number==0:
                self.file_1.write(rows[row]+' | ')
                self.file_2.write(rows[row]+' | ')
            if player_number==1:
                self.file_1.write(rows[row]+' | ')
            if player_number==2:
                self.file_2.write(rows[row]+' | ')
            for col in range(8):
                piece = self.get_piece_by_loc(row, col)
                if piece != None:
                    print(piece.get_type(), end=' | ')
                    if player_number==0:
                        self.file_1.write(piece.get_type()+' | ')
                        self.file_2.write(piece.get_type()+' | ')
                    if player_number==1:
                        self.file_1.write(piece.get_type()+' | ')
                    if player_number==2:
                        self.file_2.write(piece.get_type()+' | ')                    
                else:
                    if (row + col) % 2 != 0:
                        print('B',end=' | ')
                        if player_number==0:
                            self.file_1.write('B'+' | ')
                            self.file_2.write('B'+' | ')
                        if player_number==1:
                            self.file_1.write('B'+' | ')
                        if player_number==2:
                            self.file_2.write('B'+' | ')
                        self.board[row][col] = 'B'
                    else:
                        print('R',end=' | ')
                        if player_number==0:
                            self.file_1.write('R'+' | ')
                            self.file_2.write('R'+' | ')
                        if player_number==1:
                            self.file_1.write('R'+' | ')
                        if player_number==2:
                            self.file_2.write('R'+' | ')
                        self.board[row][col] = 'R'
            print()
            if player_number==0:
                self.file_1.write('\n')
                self.file_2.write('\n')
            if player_number==1:
                self.file_1.write('\n')
            if player_number==2:
                self.file_2.write('\n')

    #This function is used to check whether the position is occupied by the pieces or not
    def is_location_occupied(self, row, col):
        return [row, col] in [piece.get_location() for piece in self.selectedPieces]

    #This function is used to get a piece by the location/coordinated using row,col
    def get_piece_by_loc(self, row, col):
        for piece in self.selectedPieces:
            if piece.get_location() == [row, col]:
                return piece
        return None

    #This function is to determine if the move made by the player is valid or not
    def check_save_move(self, move, player_number):
        from_row = ord(move[0]) - ord('A')
        from_col = int(move[2]) - 1
        to_row = ord(move[4]) - ord('A')
        to_col = int(move[6]) - 1
       
        if from_row >= 0 and from_col >= 0 and to_row < 8 and to_col < 8:#To determine if the location is valid
            piece = self.get_piece_by_loc(from_row, from_col)
            if piece != None:
                if not self.is_location_occupied(to_row, to_col):#Determine if destination location is occupied or not
                    if piece.get_type() in ['X','O']: # if the piece is King, it can move both backward and forward diagonally
                        diff_col = (to_col - from_col)
                        if diff_col < 0:
                            diff_col = diff_col * -1
                        diff_row = (to_row - from_row)
                        if diff_row < 0:
                            diff_row = diff_row * -1
                        if diff_col == 2 and diff_row == 2: #To check whether the immediate diagonal contains the opponent piece or not
                            middle_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                            if player_number == 1:
                                if middle_piece != None and (middle_piece.get_type() == 'o' or middle_piece.getType() == 'O'):
                                    return True
                            else:
                                if middle_piece != None and (middle_piece.get_type() == 'x' or middle_piece.getType() == 'X'):
                                    return True
                        elif diff_col == 1 and diff_row == 1:
                            return True
                    else: #Not allowing the normal piece to move backward
                        diff_col = to_col - from_col
                        if diff_col < 0:
                            diff_col = diff_col * -1
                        diff_row = 0
                        if player_number == 1: #Not allowing for the negative row difference
                            diff_row = to_row - from_row
                            if diff_col == 2 and diff_row == 2: #To check whether the immediate diagonal contains the opponent piece or not
                                middle_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                                if player_number == 1:
                                    if middle_piece != None and (middle_piece.get_type() == 'o' or middle_piece.get_type() == 'O'):
                                        return True
                                else:
                                    if middle_piece != None and (middle_piece.get_type() == 'x' or middle_piece.get_type() == 'X'):
                                        return True
                            elif diff_col == 1 and diff_row == 1:
                                return True
                        else: # #Not allowing for the positive row difference
                            diff_row = to_row - from_row
                            if diff_col == 2 and diff_row == -2:  #To check whether the immediate diagonal contains the opponent piece or not
                                middle_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                                if player_number == 1:
                                    if middle_piece != None and (middle_piece.get_type() == 'o' or middle_piece.get_type() == 'O'):
                                        return True
                                else:
                                    if middle_piece != None and (middle_piece.get_type() == 'x' or middle_piece.get_type() == 'X'):
                                        return True
                            elif diff_col == 1 and diff_row == -1:
                                return True
        return False

    #This function moves the piece from one position to the other position
    def move_a_piece(self, player_name, player_number):
        if player_number==1:
            user_choice = input(f'\n{player_name} Please Enter Your Move (x piece): ')
        else:
            user_choice = input(f'\n{player_name} Please Enter Your Move (o piece): ')
        while not self.check_save_move(user_choice, player_number):
            print('Invalid Move')
            user_choice = input(f'\n{player_name} :Please Enter Your Move: ')
        
        from_row = ord(user_choice[0]) - ord('A')
        from_col = int(user_choice[2]) - 1
        to_row = ord(user_choice[4]) - ord('A')
        to_col = int(user_choice[6]) - 1
        piece = self.get_piece_by_loc(from_row, from_col)
        if piece != None:
            piece.set_location(to_row, to_col)
            pieceType = piece.get_type()

            if player_number == 1 and to_row == 7:#Checking if the piece is to be Kinged or not
                piece.set_type('X')#x gets changed to X if it is kinged
            elif player_number == 2 and to_row == 0:#Checking if the piece is to be Kinged or not
                piece.set_type('O')#o gets changed to O if it is kinged

            if pieceType in ['X','O']: # King piece
                diff_col = (to_col - from_col)
                if diff_col < 0:
                    diff_col = diff_col * -1
                diff_row = (to_row - from_row)
                if diff_row < 0:
                    diff_row = diff_row * -1
                if diff_col == 2 and diff_row == 2: # Double move
                #To check whether the immediate diagonal contains the opponent piece or not
                    mid_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                    self.remove_piece(mid_piece)
            else: # Normal piece
                diff_col = (to_col - from_col)
                if diff_col < 0:
                    diff_col = diff_col * -1
                diff_row = 0
                if player_number == 1: # Not allowing negative row difference
                    diff_row = to_row - from_row
                    if diff_col == 2 and diff_row == 2: 
                        #To check whether the immediate diagonal contains the opponent piece or not
                        mid_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                        self.remove_piece(mid_piece)
                else: #Not allowing positive row difference
                    diff_row = to_row - from_row
                    if diff_col == 2 and diff_row == -2: 
                        # Check if the immediate diagonal contains opponent's piece
                        mid_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                        self.remove_piece(mid_piece)
        #Saving each moves of the Player in their respective files
        if(player_number==1):
            self.file_1.write('\n'+player_name.capitalize()+' Moved '+user_choice[0]+user_choice[2]+' to '+user_choice[4]+user_choice[6]+'\n')
        if(player_number==2):
            self.file_2.write('\n'+player_name.capitalize()+' Moved '+user_choice[0]+user_choice[2]+' to '+user_choice[4]+user_choice[6]+'\n')

        self.create_board(player_number)#creating the board with new position of the pieces
        
    #This function removes the piece from the board
    def remove_piece(self, piece):
        self.selectedPieces.remove(piece)
        piece.set_location(-1,-1)

    #returns the pieces of the player
    def get_pieces(self, player_number):
        pieces = []
        for piece in self.selectedPieces:
            if piece.get_location() != [-1,-1]:
                if player_number == 1:
                    if piece.get_type() in ['x','X']:
                        pieces.append(piece)
                else:
                    if piece.get_type() in ['o','O']:
                        pieces.append(piece)
        return pieces

    #This function checks if the game is Over
    def is_game_over(self):
        pieces_Player1 = self.get_pieces(1)#get the remainig pieces of Player 1
        pieces_Player2 = self.get_pieces(2)#get teh remaining pieces of Player 2
        return len(pieces_Player1) == 0 or len(pieces_Player2) == 0