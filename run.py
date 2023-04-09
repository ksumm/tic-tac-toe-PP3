import art

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def print_board(board):
    """
    Printing the board of the game
    """ 
    print("-"*13)
    print("|", board[0], "|", board[1], "|", board[2], "|" )
    print("-"*13) 
    print("|", board[3], "|", board[4], "|", board[5], "|" )
    print("-"*13) 
    print("|", board[6], "|", board[7], "|", board[8], "|" ) 
    print("-"*13)  
       

def start_game():
    print("Game is starting....")
    print_board(board)
    
def rules():
    """
    Asks the user about reading the rules of the game. 
    If answer is "yes" - the game is printing the rules. 
    If answer is "no" - the game is starting. I
    If answer is "undefined" - the game is printing the error message to enter the correct symbol.
    """
    print(art.LOGO)
    print("Welcome to the TIC TAC TOE game!\n")
    while True:
        answer = input('Do you want to read the RULES? Please, input "y" for YES or "n" for NO: ')
        if answer.lower() == 'y':
            print(art.RULES)
            start_game()
            break
        elif answer.lower() == 'n':
            print("\nLet's start to play!\n")
            start_game()
            break
        else:
            print("\nThe wrong answer. Try again?\n")
            continue   
rules()
