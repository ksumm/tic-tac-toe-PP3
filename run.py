import art

print(art.LOGO)
print("Welcome to the TIC TAC TOE game!\n")

def start_game():
    print("Game is starting....")

def rules():
    """
    Asks the user about reading the rules of the game. 
    If answer is "yes" - the game is printing the rules. 
    If answer is "no" - the game is starting. I
    If answer is "undefined" - the game is printing the error message to enter the correct symbol.
    """
    while True:
        answer = input('Do you want to read the RULES? Please, input "y" for YES or "n" for NO: ')
        if answer.lower() == 'y':
            print("\nRules\n")
            break
        elif answer.lower() == 'n':
            print("\nLet's start to play!\n")
            start_game()
            break
        else:
            print("\nThe wrong answer. Try again?\n")
            continue
            
rules()
  



