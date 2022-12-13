import datetime
# Board class
from Checkers.pieces import Piece
from Checkers.constants import *
class Board:

    # Default constructor
    def __init__(self, player_1, player_2):
        self.selectedPieces = []
        self.Player1_Name= player_1
        self.Player2_Name = player_2


        self.file_1 = open(f'{str(self.file_name(self.Player1_Name))}.txt', "w")
        self.file_1.write('Player '+self.Player1_Name+' Moves:\n')

        self.file_2 = open(f'{str(self.file_name(self.Player2_Name))}.txt', "w")
        self.file_2.write('Player '+self.Player2_Name+' Moves:\n')

    def file_name(self,name_of_player):
        now = datetime.datetime.now()
        print(now.today().strftime('%d-%m-%Y %H:%M.%S %p'))
        return str(name_of_player + "_" + now.today().strftime('%d_%m_%Y %H.%M.%S %p')) #datetime.now())

    # Declare the board
    def init_board(self):
        self.board = [['temp' for i in range(8)] for _ in range(8)]
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) %2 != 0:
                    if row < 3:
                        self.selectedPieces.append(Piece(row,col,'x'))
                    elif row >= 5:
                        self.selectedPieces.append(Piece(row,col,'o'))
                    self.board[row][col] = 'B'
                else:
                    self.board[row][col] = 'R'
    
    # Display the board
    def create_board(self,player_number):
        rows = ['A','B','C','D','E','F','G','H']
        print(' ',end='   ')
        if player_number==0:
            self.file_1.write('    ')
            self.file_2.write('    ')
        if player_number==1:
            self.file_1.write('    ')
        if player_number==2:
            self.file_2.write('    ')
        for i in range(8):
            print(i+1, end='   ')
            if player_number==0:
                self.file_1.write(str(i+1)+'   ')
                self.file_2.write(str(i+1)+'   ')
            if player_number==1:
                self.file_1.write(str(i+1)+'   ')
            if player_number==2:
                self.file_2.write(str(i+1)+'   ')

            # self.file1.write(f'{i+1}', end=' ')
            # self.file2.write(f'{i+1}', end=' ')
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
            # self.file1.write(rows[row], end=' ')
            # self.file2.write(rows[row], end=' ')
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
                    # self.file1.write(piece.getType(), end=' ')
                    # self.file2.write(piece.getType(), end=' ')
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
                        # self.file1.write('B', end=' ')
                        # self.file2.write('B', end=' ')
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
                        # self.file1.write('R', end=' ')
                        # self.file2.write('R', end=' ')
                        self.board[row][col] = 'R'
            print()
            if player_number==0:
                self.file_1.write('\n')
                self.file_2.write('\n')
            if player_number==1:
                self.file_1.write('\n')
            if player_number==2:
                self.file_2.write('\n')

    # Check if the position is occupied or not
    def is_location_occupied(self, row, col):
        return [row, col] in [piece.get_location() for piece in self.selectedPieces]

    # Get the piece by location (co-ordinates)
    def get_piece_by_loc(self, row, col):
        for piece in self.selectedPieces:
            if piece.get_location() == [row, col]:
                return piece
        return None

    # check if the move is safe or not
    def check_save_move(self, move, player_number):
        from_row = ord(move[0]) - ord('A')
        from_col = int(move[2]) - 1
        to_row = ord(move[4]) - ord('A')
        to_col = int(move[6]) - 1
        # Location is valid
        if from_row >= 0 and from_col >= 0 and to_row < 8 and to_col < 8:
            # Source location contains a valid piece
            piece = self.get_piece_by_loc(from_row, from_col)
            if piece != None:
                # Destination location is not occupied
                if not self.is_location_occupied(to_row, to_col):
                    # Single Move
                    if piece.get_type() in ['X','O']: # King, allow reverse move
                        diff_col = (to_col - from_col)
                        if diff_col < 0:
                            diff_col = diff_col * -1
                        diff_row = (to_row - from_row)
                        if diff_row < 0:
                            diff_row = diff_row * -1
                        # Double move
                        if diff_col == 2 and diff_row == 2: 
                            # Check if the immediate diagonal contains opponent's piece
                            middle_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                            if player_number == 1:
                                if middle_piece != None and (middle_piece.get_type() == 'o' or middle_piece.getType() == 'O'):
                                    return True
                            else:
                                if middle_piece != None and (middle_piece.get_type() == 'x' or middle_piece.getType() == 'X'):
                                    return True
                        elif diff_col == 1 and diff_row == 1: # Single move
                            return True
                    else: # Normal Piece, do not allow backward move
                        diff_col = to_col - from_col
                        if diff_col < 0:
                            diff_col = diff_col * -1
                        diff_row = 0
                        if player_number == 1: # Do not allow negative row difference
                            diff_row = to_row - from_row
                            if diff_col == 2 and diff_row == 2: 
                                # Check if the immediate diagonal contains opponent's piece
                                middle_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                                if player_number == 1:
                                    if middle_piece != None and (middle_piece.get_type() == 'o' or middle_piece.get_type() == 'O'):
                                        return True
                                else:
                                    if middle_piece != None and (middle_piece.get_type() == 'x' or middle_piece.get_type() == 'X'):
                                        return True
                            elif diff_col == 1 and diff_row == 1: # Single move
                                return True
                        else: # Do not allow positive row difference
                            diff_row = to_row - from_row
                            if diff_col == 2 and diff_row == -2: 
                                # Check if the immediate diagonal contains opponent's piece
                                middle_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                                if player_number == 1:
                                    if middle_piece != None and (middle_piece.get_type() == 'o' or middle_piece.get_type() == 'O'):
                                        return True
                                else:
                                    if middle_piece != None and (middle_piece.get_type() == 'x' or middle_piece.get_type() == 'X'):
                                        return True
                            elif diff_col == 1 and diff_row == -1: # Single move
                                return True
                        
                    # Double Move
            # if [from_row, from_col] in [piece.getLoc() for piece in self.ActivePieces]:
        return False

    # Method to move the piece from one place to another
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
            # Post-processing of move
            pieceType = piece.get_type()

            # Check if the piece has to be changed into King
            if player_number == 1 and to_row == 7:
                piece.set_type('X')
            elif player_number == 2 and to_col == 0:
                piece.set_type('O')

            # Check if any piece has to be removed due to this move
            if pieceType in ['X','O']: # King piece
                #col_difference = math.abs(to_col - from_col)
                #row_difference = math.abs(to_row - from_row)
                diff_col = (to_col - from_col)
                if diff_col < 0:
                    diff_col = diff_col * -1
                diff_row = (to_row - from_row)
                if diff_row < 0:
                    diff_row = diff_row * -1
                # Double move
                if diff_col == 2 and diff_row == 2: 
                    # Check if the immediate diagonal contains opponent's piece
                    mid_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                    self.remove_piece(mid_piece)
            else: # Normal piece
                diff_col = (to_col - from_col)
                if diff_col < 0:
                    diff_col = diff_col * -1
                diff_row = 0
                if player_number == 1: # Do not allow negative row difference
                    diff_row = to_row - from_row
                    if diff_col == 2 and diff_row == 2: 
                        # Check if the immediate diagonal contains opponent's piece
                        mid_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                        self.remove_piece(mid_piece)
                else: # Do not allow positive row difference
                    diff_row = to_row - from_row
                    if diff_col == 2 and diff_row == -2: 
                        # Check if the immediate diagonal contains opponent's piece
                        mid_piece = self.get_piece_by_loc((from_row+to_row)/2, (from_col+to_col)/2)
                        self.remove_piece(mid_piece)
        if(player_number==1):
            self.file_1.write('\n'+player_name.capitalize()+' Moved '+user_choice[0]+user_choice[2]+' to '+user_choice[4]+user_choice[6]+'\n')
        if(player_number==2):
            self.file_2.write('\n'+player_name.capitalize()+' Moved '+user_choice[0]+user_choice[2]+' to '+user_choice[4]+user_choice[6]+'\n')

        self.create_board(player_number)
        
    # Remove the piece from the board
    def remove_piece(self, piece):
        #piece_location = piece.getLoc()
        self.selectedPieces.remove(piece)
        piece.set_location(-1,-1)

    # Get the pieces of a player
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

    # Check if the game is over
    def is_game_over(self):
        pieces_Player1 = self.get_pieces(1)
        pieces_Player2 = self.get_pieces(2)
        return len(pieces_Player1) == 0 or len(pieces_Player2) == 0