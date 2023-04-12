import art


# globals
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player = "X"
winner = None


# print the game board
def print_board(b):
    """
    Print the board of the game.
    """
    print("-"*13)
    print("|", b[0], "|", b[1], "|", b[2], "|")
    print("-"*13)
    print("|", b[3], "|", b[4], "|", b[5], "|")
    print("-"*13)
    print("|", b[6], "|", b[7], "|", b[8], "|")
    print("-"*13)


# get and print out the user input
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
            print("checking winner...")
            check_winner(board)
            switch_player()
        elif inp_num not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Error input. Enter the number 1-9: ")
            continue
        else:
            print("This cell is already taken. Enter another number.")
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


def check_col(board):
    """
    check win col
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


def check_diag(board):
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


def check_winner(board):
    """
    check winner if there are a match in a row, column or diagonal
    """
    if check_row(board):
        print_board(board)
        print(f"The winner is {winner}!")
    elif check_col(board):
        print_board(board)
        print(f"The winner is {winner}!")
    elif check_diag(board):
        print_board(board)
        print(f"The winner is {winner}!")


def switch_player():
    """
    switch the player from X to O
    """
    global player
    if player == "X":
        print(player)
        player = "O"
        print(player)
    else:
        player = "X"


# start the game
def start_game():
    """
    function to start the game
    """
    print("Game is starting....")
    print_board(board)
    user_input(board)


def rules():
    """
    asks the user about reading the rules of the game
    if the answer is "yes" - the game is printing the rules
    if the answer is "no" - the game is starting. I
    if the answer is "undefined" - the game is printing the message
    to enter the correct symbol.
    """
    print(art.LOGO)
    print("Welcome to the TIC TAC TOE game!\n")
    while True:
        answer = input(
            'Do you want to read the RULES? Please, input "y" for YES or "n" for NO: ')
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
