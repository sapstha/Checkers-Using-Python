from Checkers.game import Game

def menu():
    print("\n****Welcome to CHECKERS****\n")
    user_choice=int(input("1. Play Game\n2. View Rules\n3. Exit\n:"))
    if(user_choice==1):
        # Instantiate the game class
        game_obj = Game()
        # Display game menu
        game_obj.start_game()
    elif user_choice==2:
        gameRules="\n-Two Players can play the 8X8 Checker Games.\n-The unoccupied grid squares are denoted by either \'R' or \'B'.\n"
        gameRules+="-The Players pieces are displayed as \'x' or \'o'. \n-One need to enter the row and column position to make the "
        gameRules+="piece move,\n-The input format should be for example: C-2,D-1.\n-A piece can move only on unoccupied location diagonally.\n"
        gameRules+="-Pieces can move only forward,not backward"
        print(gameRules)
    elif user_choice==3:
        print("\nThank You For Using the Program!\n")
        exit()
    else:
        print("\nInvalid Choice!Please enter valid option.\n")
        menu()
    

while(True):
    menu()