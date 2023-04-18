"""
Import
"""
import colorama
from colorama import Fore, Style
import art
colorama.init()


# globals
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player = "X" # pylint: disable=C0103
winner = None # pylint: disable=C0103
game_running = True # pylint: disable=C0103


# print the game board
def print_board(g_board):
    """
    Print the board of the game.
    """
    print(Fore.YELLOW  + "-"*13 + Fore.RESET)
    print(Fore.YELLOW  + "|", g_board[0], "|", g_board[1], "|", g_board[2], "|" + Fore.RESET)
    print(Fore.YELLOW + "-"*13 + Fore.RESET)
    print(Fore.YELLOW + "|", g_board[3], "|", g_board[4], "|", g_board[5], "|"+ Fore.RESET)
    print(Fore.YELLOW + "-"*13 + Fore.RESET)
    print(Fore.YELLOW + "|", g_board[6], "|", g_board[7], "|", g_board[8], "|"+ Fore.RESET)
    print(Fore.YELLOW + "-"*13 + Fore.RESET)


# get and print out the user input
def user_input(board):
    """
    display the player's move on the board
    check the user input value:
    - if it is a number from 1 to 9
    - if the cell is already occupied
    """
    while True:
        inp_num = int(input(f"{Fore.MAGENTA}\nEnter a number 1-9:\n {Fore.RESET}"))
        if inp_num >= 1 and inp_num <= 9 and board[inp_num-1] == "-":
            board[inp_num-1] = player
            break
        elif inp_num not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(Fore.CYAN + "Error input. Enter the number 1-9: "+ Fore.RESET)
            continue
        else:
            print(Fore.CYAN + "This cell is already taken. Enter another number." + Fore.RESET)
            continue
        print_board(board)



# check the winner
def check_row(board):
    """
    check win row
    """
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_column(board):
    """
    check win column
    """
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def check_diagonal(board):
    """
    check win diagonal
    """
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def check_draw(board):
    """
    check if there no winners
    """
    global game_running
    if "-" not in board:
        print_board(board)
        print("\nIt is a Draw!")
        print(Fore.CYAN + Style.BRIGHT + "\nTo start New Game press the Run Program button. Nice to see you again!" + Fore.RESET)
        game_running = False


def check_winner(board):
    """
    check winner if there are a match in a row, column or diagonal
    """
    global game_running
    if check_row(board):
        print_board(board)
        print(f"{Fore.CYAN}{Style.BRIGHT}\nThe winner is {winner}!{Fore.RESET}")
        print(Fore.CYAN + Style.BRIGHT + "\nTo start New Game press the Run Program button. Nice to see you again!" + Fore.RESET)
        game_running = False

    elif check_column(board):
        print_board(board)
        print(f"{Fore.CYAN}{Style.BRIGHT}\nThe winner is {winner}!{Fore.RESET}")
        print(Fore.CYAN + Style.BRIGHT + "\nTo start New Game press the Run Program button. Nice to see you again!" + Fore.RESET)
        game_running = False

    elif check_diagonal(board):
        print_board(board)
        print(f"{Fore.CYAN}{Style.BRIGHT}\nThe winner is {winner}!{Fore.RESET}")
        print(Fore.CYAN + Style.BRIGHT + "\nTo start New Game press the Run Program button. Nice to see you again!" + Fore.RESET)
        game_running = False


def rules():
    """
    asks the user about reading the rules of the game
    if the answer is "yes" - the game is printing the rules
    if the answer is "no" - the game is starting. I
    if the answer is "undefined" - the game is printing the message
    to enter the correct symbol.
    """
    global game_running
    print(art.LOGO)
    print(Fore.YELLOW + "Welcome to the TIC TAC TOE game!\n" + Fore.RESET)
    while True:
        answer = input(
            Fore.YELLOW +
            'Do you want to read the RULES? Please, input "y" for YES or "n" for NO: '
             + Fore.RESET)
        if answer.lower() == 'y':
            print(art.RULES)
            break
            game_running = True
        elif answer.lower() == 'n':
            print(Fore.MAGENTA + "\nLet's start to play!\n" + Fore.RESET)
            break
            game_running = True
        else:
            print(Fore.CYAN + "\nThe wrong answer. Try again?\n" + Fore.RESET)
            continue


rules()


def switch_player():
    """
    switch the player from X to O
    """
    global player
    if player == "X":
        player = "O"

    else:
        player = "X"



# start the game
while game_running:
    print_board(board)
    user_input(board)
    check_winner(board)
    check_draw(board)
    switch_player()
