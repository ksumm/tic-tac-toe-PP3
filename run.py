import art

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]        
player = "X"       

def print_board(board):
    """
    Print the board of the game.
    """ 
    print("-"*13)
    print("|", board[0], "|", board[1], "|", board[2], "|" )
    print("-"*13) 
    print("|", board[3], "|", board[4], "|", board[5], "|" )
    print("-"*13) 
    print("|", board[6], "|", board[7], "|", board[8], "|" ) 
    print("-"*13)

def user_input(board): 
    """
    display the player's move on the board
    check the user input value:
    - if it is a number from 1 to 9
    - if the cell is already occupied
    """   
    while True:
        inp_num = int(input("Enter a number 1-9: "))
        if inp_num >= 1 and inp_num <= 9 and board[inp_num-1] == "-":
            board[inp_num-1] = player  
        elif not (inp_num in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
            print("Error input. Enter the number 1-9: ")
            continue
        else:
            print("This cell is already taken. Enter another number.")
            continue 
        print_board(board)

def start_game():
    print("Game is starting....")
    print_board(board)
    user_input(board)
        
def rules():
    """
    Asks the user about reading the rules of the game. 
    If answer is "yes" - the game is printing the rules. 
    If answer is "no" - the game is starting. I
    If answer is "undefined" - the game is printing the message 
    to enter the correct symbol.
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
