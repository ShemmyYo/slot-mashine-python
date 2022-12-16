import random
import time
import os

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "♥": 2,
    "♦": 4,
    "♠": 6,
    "♣": 8
}

symbol_value = {
    "♥": 5,
    "♦": 4,
    "♠": 3,
    "♣": 2
}


def spin_mashine(rows, cols, symbols):
    """
    Returning random columns-symbols for reels
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def deposit():
    """
    Collecting user imput as deposit and checking 
    if input is a valid number
    """
    deposit_info()
    while True:
        amount = input("\033[1;33;40m  What's your deposit? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("  !!!  NOTE: Amount must be grater then 0")
        else:
            print(f"\033[1;31;40m  !!!  NOTE: '{amount}', you entered is not accepted!\n")
            print("\033[1;35;40m  Please enter a valid amount again")
            print("\033[1;35;40m  Amount must be a number, and grater then 0")

    return amount


def get_number_of_lines(): 
    """
    Collecting user imput as number of lines to bet and 
    checking if input is a valid number
    """
    get_number_of_lines_info()
    while True:
        lines = input("\033[1;33;40m  Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"\033[1;31;40m  !!!  NOTE: Enter a valid number of lines (between 1-{MAX_LINES})\n")
        else:
            print(f"\033[1;31;40m  !!!  NOTE: '{lines}', you entered is not accepted!\n")
            print("\033[1;35;40m  Please enter a valid number of lines")
            print(f"\033[1;35;40m  Number of lines must be a number between 1 and {MAX_LINES}\n")

    print(f"\033[1;32;40m  >>>  You bet on {lines} lines\n")
    return lines


def get_bet():
    """
    Collecting user imput as the amount thats being bet by user
    and checking if input is a valid number
    """
    get_bet_info()
    while True:
        bet = input("\033[1;33;40m  How much would you like to bet on each line? €")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"\033[1;31;40m  !!!  NOTE: Bet amount must be between €{MIN_BET} and €{MAX_BET}\n")
        else:
            print(f"\033[1;31;40m  !!!  NOTE: '{bet}', you entered is not correct!\n")
            print("\033[1;35;40m  Please enter a valid bet amount again")
            print(f"\033[1;35;40m  Bet amount must be a number between €{MIN_BET} and €{MAX_BET}\n")

    print(f"\033[1;32;40m  >>> Your bet amount is: €{bet}\n")
    time.sleep(1)

    return bet


def spin(balance):
    """
    Cretaed spin function with while loop within it
    that checks whether user balance can cover bet
    """
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"\033[1;31;40m  >>>  Insufficient balance! Your current balance is €{balance}!\n")
            time.sleep(1)
        else:
            break   

    spin_info()
    print(f"\033[1;33;40m                >>> You are betting €{bet} on {lines} lines <<<")
    print(f"\033[1;33;40m                     >>> Total bet is €{total_bet} <<<")
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    reels = spin_mashine(ROWS, COLS, symbol_count)
    print_slot_mashine(reels)
    winnings, winning_lines = win_check(reels, lines, bet, symbol_value)
    return winnings - total_bet


def print_slot_mashine(columns):
    """
    Prints slot mashine by transposing column to line
    """
    print(f"\n\033[1;33;40m>   <+---------+>      <+---------+>      <+---------+>   <")
    for row in range(len(columns[0])):
        
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print("\033[1;33;40m     |  ", "\033[1;31;40m", column[row], end="\033[1;33;40m    |   ")
            else:
                print("\033[1;33;40m     |  ", "\033[1;31;40m", column[row], end="\033[1;33;40m    |   ")

        print(f"\n>   <+---------+>      <+---------+>      <+---------+>   <")


def win_check(columns, lines, bet, values):
    """
    Checks if 3 same sybols in any lines - win
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_in_reel = column[line]
            if symbol != symbol_in_reel:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
            print()
            print("\n\033[1;33;40m               Congratulations! You won!!!")
            print("\033[1;33;40m******************************************************************")
            print(f"\033[1;32;40m  You have won €{winnings}! on line: ", *winning_lines)

    return winnings, winning_lines


def run_menu():
    """
    Runs game Main Menu
    """
    while True:
        run_menu_info()
        print("\n\033[1;33;40m  Choose option from the list below:\n")

        print("\033[1;35;40m  >>>   Press 1 to >>> Play  Game <<<")
        print("\033[1;35;40m  >>>   Press 2 to >>> View Rules <<<")
        print("\033[1;35;40m  >>>   Press 3 to >>> View (future option) Score-Board <<<")
        print("\033[1;35;40m  >>>   Press Q to >>> Quit  Game <<<\n")
        value = input()
        if value == "1":
            time.sleep(0.5)
            clear_screen()
            welcome_screen()
            break
        elif value == "2":
            clear_screen()
            intructions()
        #elif value == "3":
        #    score-board()
        elif value == "q":
            clear_screen()
            welcome_screen()
            time.sleep(0.5)
            game_over_info()
            time.sleep(0.5)
            quit()
        else:
            print(f"\033[1;31;40m  '{value}' is not valid!")
            time.sleep(1)
            clear_screen()
            welcome_screen()
        clear_screen()
        welcome_screen()


#messages displayed on screen listed below:
def welcome_screen():
    print("\033[1;33;40m******************************************************************")
    print("\033[1;34;10m                 Welcome to One-Armed Bandit!                     ")
    print("                                                                  ")
    print("\033[1;33;40m******************************************************************")
    print("\033[1;34;10m    ####  ##   ## #####      ####  #####  ##   ## ##### #####     ")
    print("\033[1;35;10m   ##  ## ###  ## ##        ##  ## ##  ## ### ### ##    ##  ##    ")
    print("\033[1;36;10m   ##  ## ## #### ####  ##  ###### #####  ## # ## ####  ##  ##    ")
    print("\033[1;37;10m   ##  ## ##  ### ##        ##  ## ## ##  ##   ## ##    ##  ##    ")
    print("\033[1;38;10m    ####  ##   ## #####     ##  ## ##  ## ##   ## ##### #####     ")
    print("                                                                  ")
    print("\033[1;38;10m        ####     ####   ##   ##  #####   ##  ######   ##          ")
    print("\033[1;37;10m        ##  ##  ##  ##  ###  ##  ##  ##  ##    ##     ##          ")
    print("\033[1;36;10m        #####   ######  ## ####  ##  ##  ##    ##     ##          ")
    print("\033[1;35;10m        ##  ##  ##  ##  ##  ###  ##  ##  ##    ##                 ")
    print("\033[1;34;10m        ####    ##  ##  ##   ##  #####   ##    ##     ##          ")
    print("                                                                  ")
    print("\033[1;33;40m******************************************************************")
    print("\033[1;31;40m                          by ShemmyYo                             ")
    print("\033[1;33;40m******************************************************************")


def intructions():
    welcome_screen()
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>              <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\033[1;31;40m                      >>> Instructions <<<                        ")
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>              <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\033[1;35;10m  The aim of the game is to make sure that all of the symbols     ")
    print("\033[1;35;10m  on the screen of the machine match up - get them all,           ")
    print("\033[1;35;10m  and you'll win the money.                                       ")
    print("\033[1;35;10m  All you need is a bag of change and you're ready to go!\n       ")
    print("instructions TBC \n")

    answer = input("\033[1;33;40m  Press Enter to go to >>> MAIN MENU <<< (Q to Quit)\n")
    if answer == "q":
        quit()
    clear_screen()
    welcome_screen()


def run_menu_info():
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\033[1;31;40m                        >>> MAIN MENU <<<                         ")
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")


def deposit_info():
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\033[1;31;40m                        >>>  Deposit  <<<                         ")
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")


def get_number_of_lines_info():
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>               <<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\033[1;31;40m                      >>>  No of Lines  <<<                       ")
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>               <<<<<<<<<<<<<<<<<<<<<<<<<<\n")


def get_bet_info():
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>                <<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\033[1;31;40m                      >>>  Bet per Line  <<<                      ")
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>                <<<<<<<<<<<<<<<<<<<<<<<<<\n")


def spin_info():
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>                <<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\033[1;31;40m                      >>>  Turn Results  <<<                      ")
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>                <<<<<<<<<<<<<<<<<<<<<<<<<")


def game_over_info():
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\033[1;31;40m                        >>> GAME OVER <<<                         ")
    print("\033[1;33;40m                        >>> Good-Bye! <<<                         ")
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<")


def clear_screen():
    """
    Clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    main calling all required functions
    """
    clear_screen()
    welcome_screen()
    run_menu()
    balance = deposit()  
    if (balance >= 0):
        while True:
            print("\n\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print(f"\033[1;32;40m                 >>>  Current balance is €{balance}! <<<            ")
            print("\033[1;34;40m                       >>>  Lets play! <<<                        ")
            print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
            answer = input("\033[1;31;40m>>>>>>>>>>>  Press >>> Enter to Spin <<< (Q to Quit)  <<<<<<<<<<<<\n")
            if answer == "q":
                break
            balance += spin(balance)
    else:
        print(f"  Your ballance is €{balance}!")
    

    time.sleep(0.5)
    clear_screen()
    welcome_screen()
    time.sleep(0.5)
    print("\033[1;34;40m>>>>>>>>>>>>>>>>>>>>>>>>>>>           <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(f"\n\033[1;38;10m                  >>>  Final balance is €{balance}  <<<")
    game_over_info()
    time.sleep(2)
    main()


main()