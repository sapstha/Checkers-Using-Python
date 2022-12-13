from Checkers.board import Board
class Game:

    # Default constructor
    def __init__(self):
        pass

    # Function for displaying the game menu
    def start_game(self):
        # Property for storing player 1's name
        self.Player1_Name = ''
        self.Player1_Name = input("Please Enter the Player 1's Name: ")
        while self.Player1_Name == '':
            self.Player1_Name = input("Please Enter a Valid Name for Player 1: ")
        # Prop to store player 2's name
        self.Player2_Name = input("Please Enter the Player 2's Name: ")
        while self.Player2_Name == '':
            self.Player2_Name = input("Please Enter a Valid Name for Player 2: ")

        # Begin game play logic
        user_input = input("Begin game play? (Y/N) ").lower()
        while user_input not in ['y', 'n']:
            print("Invalid Choice!")
            user_input = input("Begin game play? (Y/N) ")
        if user_input == 'y':
            self.run_game()

    # Function to run the game
    def run_game(self):
        self.board = Board(self.Player1_Name, self.Player2_Name)
        self.board.init_board()
        self.board.create_board(0)
        is_Player1s_Turn = True
        while not self.board.is_game_over():
            if is_Player1s_Turn:
                is_Player1s_Turn = False   
                self.board.move_a_piece(self.Player1_Name, 1)
            else:
                is_Player1s_Turn = True
                self.board.move_a_piece(self.Player2_Name, 2)

        if(self.board.is_game_over()):
            print("\n***Game Over***\n")
            pieces_Player1 = self.board.get_pieces(1)
            pieces_Player2 = self.board.get_pieces(2)
            if(len(pieces_Player1)>len(pieces_Player2)):
                print(self.Player1_Name+' is the Winner!!!!')
            else:
                print(self.Player2_Name+' is the Winner!!!!!')
        
    def save_board_to_file(self):
        self.file1 = open(self.file_name(self.Player1_Name), "w")
        self.file1.write(self.Player1_Name)
        #self.file1.close()

        self.file2 = open(self.file_name(self.Player2_Name), "w")
        self.file2.write(f'{self.Player2_Name}')
        #self.file2.close()