import random
import time
import os

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
DEPOSIT = 100

ROWS = 3
COLS = 3

symbol_count = {
    "♡": 3,
    "♢": 4,
    "♤": 6,
    "♧": 7
}

symbol_value = {
    "♡": 5,
    "♢": 4,
    "♤": 3,
    "♧": 2
}

def clear_screen():
    """
    Clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    """
    Player class used to create player
    """
    def __init__(self, name, place, rounds, balance):
        self.name = name
        self.place = place
        self.rounds = 0
        self.balance = DEPOSIT


def player_details():
    """
    Prompting Player to provide their details
    """
    player_info()
    while True:
        player_name = input("\033[1;33;40m  >>>  What is your name? \
>>> ").capitalize()
        if player_name.isalpha():
            place = False
            while not place:
                player_place = input("\033[1;33;40m  >>>  Which city \
are you from? >>> ").capitalize()
                if player_place.isalpha():
                    player = Player(name=player_name, place=player_place,
                                    rounds=0, balance=DEPOSIT)
                    return player
                else:
                    clear_screen()
                    print(f"\033[1;31;40m  '{player_place}' is not valid")
                    print("\033[1;31;40m  !!!  Only letters please")
        else:
            print(f"\033[1;31;40m  '{player_name}' is not valid")
            print("\033[1;31;40m  !!!  Only letters please")


def deposit(player):
    """
    Collects user imput as deposit and implements checks
    if input is a valid number and prints msg.
    """
    deposit_info()
    print(f"\033[1;35;40m  {player.name}, your default deposit is €100")
    answer = input("\n\033[1;35;10m  >>> Press Enter and continue or \
'C' to change deposit amount ").upper()
    if answer == "C":
        while True:
            amount = input(f"\033[1;35;40m  {player.name}, what's your deposit? €")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("  !!!  NOTE: Amount must be grater then 0")
            else:
                print(f"\033[1;31;40m  !!!  NOTE: '{amount}', you \
entered is not accepted!\n")
                print(f"\033[1;35;40m  {player.name}, please enter a valid amount \
again")
                print("\033[1;35;40m  Amount must be a number, and \
grater then 0")
    else:
        amount = DEPOSIT
    return amount


def get_number_of_lines():
    """
    Collects user imput as number of lines to bet,
    checks if input is a valid number and prints msg.
    """
    get_number_of_lines_info()
    while True:
        lines = input("\033[1;33;40m  Enter the number of lines to bet on \
(1-" + str(MAX_LINES) + ")?  >>> ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"\033[1;31;40m  !!!  NOTE: Enter a valid number of \
lines (between 1-{MAX_LINES})\n")
        else:
            print(f"\033[1;31;40m  !!!  NOTE: '{lines}', you entered is \
not accepted!\n")
            print("\033[1;35;40m  Please enter a valid number of lines")
            print(f"\033[1;35;40m  Number of lines must be a number between\
 1 and {MAX_LINES}\n")
    print(f"\033[1;32;40m  >>>  You bet on {lines} lines")
    return lines


def get_bet():
    """
    Collects user imput as the amount thats being bet by user,
    checks if input is a valid number and prints msg
    """
    get_bet_info()
    while True:
        bet = input("\033[1;33;40m  How much would you like to bet on each\
 line?  >>> €")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"\033[1;31;40m  !!!  NOTE: Bet amount must be between\
 €{MIN_BET} and €{MAX_BET}\n")
        else:
            print(f"\033[1;31;40m  !!!  NOTE: '{bet}', you entered is not \
correct!\n")
            print("\033[1;35;40m  Please enter a valid bet amount again")
            print(f"\033[1;35;40m  Bet amount must be a number between \
€{MIN_BET} and €{MAX_BET}\n")
    print(f"\033[1;32;40m  >>> Your bet amount is: €{bet}\n")
    time.sleep(1)
    return bet


def spin(balance, player):
    """
    Created spin function with 2 while loops within to:
    checks whether user balance can cover bet,
    checks whether user balance can cover amount of lines
    """
    while True:
        lines = get_number_of_lines()
        if balance <= 3 and balance < lines:
            print(f"\033[1;31;40m  >>>  {player.name}  <<<")
            print(f"\033[1;31;40m  >>>  Insufficient balance to cover \
{lines} line(s)!\n")
            time.sleep(1.5)
        else:
            break
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"\033[1;31;40m  >>>  {player.name}  <<<")
            print(f"\033[1;31;40m  >>>  Balance won't cover {lines} line(s)\
 you wish to bet on €{bet} each!")
            print(f"\033[1;31;40m  >>>  Your current balance is €{balance}!\n")
            time.sleep(1.5)
        else:
            break
    clear_screen()
    welcome_screen()
    progress_bar()
    spin_info()
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)
    print("\033[1;33;40m "*13 + f">>> You are betting €{bet} on \
{lines} line(s) <<<" + " "*9)
    print("\033[1;33;40m "*21 + f">>> Total bet is €{total_bet} <<<" + " "*22)
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)
    reels = spin_mashine(ROWS, COLS, symbol_count)
    print_slot_mashine(reels)
    winnings, winning_lines = win_check(reels, lines, bet, symbol_value, player)
    return winnings - total_bet


def spin_mashine(rows, cols, symbols):
    """
    Returns random columns-symbols for reels
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


def print_slot_mashine(columns):
    """
    Prints slot mashine by transposing column to line
    """
    print(" "*66)
    print("\033[1;33;40m " + "  --<+>>>>X<<<<+>--  "*3 + "  ")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print("\033[1;33;40m      |  ", "\033[1;31;40m\
", column[row], end="\033[1;33;40m    |    ")
            else:
                print("\033[1;33;40m      |  ", "\033[1;31;40m\
", column[row], end="\033[1;33;40m    |       ")
        print("\n\033[1;33;40m " + "  --<+>>>>X<<<<+>--  "*3 + "  ")
    print(" "*66)


def win_check(columns, lines, bet, values, player):
    """
    Checks if 3 same sybols in any lines - and prints win/loose lines
    """
    winnings = 0
    winning_lines = []
    loosing_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_in_reel = column[line]
            if symbol != symbol_in_reel:
                loosing_lines.append(line+1)
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
            print()
            print("\n" + "\033[1;33;40m "*15 + f"Congratulations {player.name}! You won!!!")
            print("\033[1;33;40m*"*66)
            print(f"\033[1;32;40m  >>>  {player.name}, you have won €{winnings}! on line(s)\
: ", *winning_lines)
    print("\033[1;31;40mx"*66)
    print(f"\033[1;31;40m  >>>  {player.name}, you have lost on line(s): ", *loosing_lines)
    return winnings, winning_lines


def run_menu(player):
    """
    Runs game Main Menu
    """
    while True:
        run_menu_info()
        print(f"\033[1;33;40m  {player.name}, choose option from the list below:\n")
        print("\033[1;35;40m  >>>   Press 1 to >>> Play  Game <<<")
        print("\033[1;35;40m  >>>   Press 2 to >>> View Rules <<<")
        print("")
        print("\033[1;35;40m  >>>   Press Q to >>> Quit  Game <<<\n")
        value = input("\033[1;33;40m  >>>  Option: ").upper()
        if value == "1":
            time.sleep(0.5)
            clear_screen()
            welcome_screen()
            break
        elif value == "2":
            clear_screen()
            intructions(player)
        elif value == "Q":
            clear_screen()
            welcome_screen()
            time.sleep(0.5)
            quit()
        else:
            print(f"\033[1;31;40m  '{value}' is not valid!")
            time.sleep(1)
        clear_screen()
        welcome_screen()


def main():
    """
    main calling all required functions to run the game and checks
    if balance suficient to play game on balance return
    """
    clear_screen()
    welcome_screen()
    progress_bar()
    player = player_details()
    clear_screen()
    welcome_screen()
    progress_bar()
    run_menu(player)
    balance = deposit(player)
    if (balance > 0):
        while True:
            clear_screen()
            welcome_screen()
            print("\033[1;33;40m "*26 + f"+++  {player.name}  +++")
            print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
            print("\033[1;32;40m "*17 + f">>>  Current balance is \
€{balance}! <<<" + " "*16)
            if balance <= 0:
                game_over_info()
                main()
            else:
                print("\033[1;34;40m "*23 + ">>>  Let's play! <<<" + " "*23)
                print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
                answer = input("\033[1;31;40m>"*13 + "  Press >>> Enter t\
o Spin <<< (M for MENU)  " + "<"*9).upper()
                if answer == "M":
                    game_over_info()
                    time.sleep(2)
                    main()
                balance += spin(balance, player)
                input("\n\033[1;33;40m  >>>  Press Enter to continue\n")
    else:
        print(f"  Your ballance is €{balance}!")
        input("\n\033[1;33;40m  >>>  Press Enter to continue\n")
    progress_bar()
    clear_screen()
    welcome_screen()
    print("\033[1;34;40m>"*27 + " "*11 + "<"*27)
    print("\n" + "\033[1;38;10m "*18 + f">>> Final balance is €{balance} <<\n")
    progress_bar()
    game_over_info()
    time.sleep(2)
    main()


# Progress bar function copied from https://stackoverflow.com
def progress_bar():
    # A List of Items need to print progress bar
    items = list(range(0, 57))
    lengh = len(items)
    # Initial call to print 0% progress
    printProgressBar(0, lengh, prefix='\033[1;33;40mLoading: ', suffix='\
Complete', length=38)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.005)
        # Update Progress Bar
        printProgressBar(i + 1, lengh, prefix='Progress:', suffix='Complete\
', length=38)


# Print iterations progress copied from https://stackoverflow.com
def printProgressBar(iteration, total, prefix='', suffix='\
', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    by https://stackoverflow.com
    """
    percent = ("{0:." + str(decimals) + "f}\
").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# all messages displayed on screen listed below:
def welcome_screen():
    clear_screen()
    print("\033[1;33;40m*"*66)
    print("\033[1;34;10m "*17 + "Welcome to One-Armed Bandit!" + " "*21)
    print()
    print("\033[1;34;10m*"*66)
    print("\033[1;34;10m    ####  ##   ## #####      ####  #####  ##   ## ###\
## #####     ")
    print("\033[1;35;10m   ##  ## ###  ## ##        ##  ## ##  ## ### ### ## \
   ##  ##    ")
    print("\033[1;36;10m   ##  ## ## #### ####  ##  ###### #####  ## # ## ###\
#  ##  ##    ")
    print("\033[1;37;10m   ##  ## ##  ### ##        ##  ## ## ##  ##   ## ## \
   ##  ##    ")
    print("\033[1;38;10m    ####  ##   ## #####     ##  ## ##  ## ##   ## ###\
## #####     ")
    print()
    print("\033[1;38;10m        ####     ####   ##   ##  #####   ##  ######  \
 ##          ")
    print("\033[1;37;10m        ##  ##  ##  ##  ###  ##  ##  ##  ##    ##    \
 ##          ")
    print("\033[1;36;10m        #####   ######  ## ####  ##  ##  ##    ##    \
 ##          ")
    print("\033[1;35;10m        ##  ##  ##  ##  ##  ###  ##  ##  ##    ##    \
             ")
    print("\033[1;34;10m        ####    ##  ##  ##   ##  #####   ##    ##    \
 ##          ")
    print()
    print("\033[1;34;10m*"*66)
    print("\033[1;31;40m "*26 + "by ShemmyYo" + " "*29)
    print("\033[1;34;10m*"*66)


def intructions(player):
    welcome_screen()
    print("\033[1;34;40m>"*25 + " "*14 + "<"*27)
    print("\033[1;35;10m "*22 + ">>> Instructions <<<" + " "*24)
    print("\033[1;34;40m>"*25 + " "*14 + "<"*27)
    print("\033[1;33;40m-"*66)
    print("\033[1;35;10m  The aim of the game is to make sure that all of the\
 symbols     ")
    print("\033[1;35;10m  on the screen of the machine match up in line" + "\
 "*19)
    print("\033[1;35;10m  Get them all, and you'll win the money!" + " "*25)
    print("\033[1;33;40m="*66)
    print("\033[1;35;10m  1. Only horizontal 1 to 3 lines can be bet on" + "\
 "*19)
    print("\033[1;35;10m  2. When betting on lines you start betting on top \
line first -1-")
    print("\033[1;35;10m     middle -2- second and bottom -3- third." + " "*22)
    print("\033[1;35;10m  3. There is: 3 x ♥, 4 x ♦, 6 x ♠ and 7 x ♣ symbols  \
            ")
    print("\033[1;35;10m  4. Valued at :  ♥ - 5, ♦ - 4, ♠ - 3 and ♣ - 2       \
            ")
    print("\033[1;35;10m  5. Min. bet is €1 and max is €100" + " "*31)
    print("\033[1;33;40m="*66)
    print(f"\033[1;35;10m  {player.name},")
    print("\033[1;35;10m  all you need is a bag of change and you're ready \
to go!         ")
    print("\033[1;33;40m-"*66)
    answer = input("\033[1;33;40m  >>>  Press Enter to go to >>> MAIN MENU <<<\
 (Q to Quit)  <<<    \n").upper()
    if answer == "Q":
        quit()


def run_menu_info():
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
    print("\033[1;35;10m "*24 + ">>> MAIN MENU <<<" + " "*25)
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)


def player_info():
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
    print("\033[1;35;10m "*23 + ">>> Player Info <<<" + " "*24)
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)


def deposit_info():
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
    print("\033[1;35;10m "*24 + ">>>  Deposit  <<<" + " "*25)
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)


def get_number_of_lines_info():
    print("\033[1;34;40m>"*25 + " "*15 + "<"*26)
    print("\033[1;35;10m "*22 + ">>>  No of Lines  <<<" + " "*23)
    print("\033[1;34;40m>"*25 + " "*15 + "<"*26)


def get_bet_info():
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)
    print("\033[1;35;10m "*22 + ">>>  Bet per Line  <<<" + " "*22)
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)


def spin_info():
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)
    print("\033[1;35;10m "*22 + ">>>  Turn Results  <<<" + " "*22)
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)


def game_over_info():
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
    print("\033[1;31;40m "*24 + ">>> GAME OVER <<<" + " "*25)
    print("\033[1;33;40m "*24 + ">>> Good-Bye! <<<" + " "*25)
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
    input("\n\033[1;33;40m  >>>  Press Enter to exit game\n")


if __name__ == '__main__':
    main()
