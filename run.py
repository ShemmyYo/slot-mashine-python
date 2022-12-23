"""
import
"""
import random
import time
import os
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('slot_mashine')

highscores = SHEET.worksheet('highscores')
highscores_rounds = highscores.get_all_values()

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


class Player:
    """
    Player class used to create player
    """
    def __init__(self, name, place, rounds, balance, wins, win):
        self.name = name
        self.place = place
        self.rounds = 1
        self.balance = DEPOSIT
        self.wins = 0
        self.win = 0


def player_details():
    """
    Prompting Player to provide their details
    """
    player_info()
    while True:
        player_name = input("\033[1;33;40m  >>>  What is your name Player? \
                             >>> ").capitalize()
        if player_name.isalpha():
            place = False
            while not place:
                player_place = input("\033[1;33;40m  >>>  Which city \
                                      are you from? >>> ").capitalize()
                if player_place.isalpha():
                    player = Player(name=player_name, place=player_place,
                                    rounds=1, balance=DEPOSIT, wins=0, win=0)
                    return player
                else:
                    print(f"\033[1;31;40m  '{player_place}' is not valid")
                    print("\033[1;31;40m  !!!  Only letters please")
        else:
            print(f"\n\033[1;31;40m  '{player_name}' is not valid")
            print("\033[1;31;40m  !!!  Only letters please")


def deposit(player):
    """
    Collects user imput as deposit and implements checks
    if input is a valid number and prints msg.
    """
    deposit_info()
    print(f"\033[1;33;40m  {player.name}, your default deposit is €100")
    print("\n\033[1;31;40m  >>> Press 'C' to change deposit/difficulty level")
    answer = input("\n\033[1;35;10m  >>> Press Enter to continue").upper()
    if answer == "C":
        print(f"\n\033[1;33;40m  {player.name}, lets's get your \
        deposit set!\n")
        print("\033[1;37;10m  >>>  Press '1' to set it to €50 (hard)")
        print("\033[1;37;10m  >>>  Press '2' to set it tt €100 (normal)")
        print("\033[1;37;10m  >>>  Press '3' to set it to €200 (easy)")
        while True:
            selection = input(f"\n\033[1;33;40m  {player.name}, what's your\
                                decision? ").upper()
            if selection == "1":
                amount = 50
                break
            elif selection == "2":
                amount = 100
                break
            elif selection == "3":
                amount = 200
                break
            else:
                print(f"\n\033[1;31;40m  !!!  NOTE: '{selection}', you \
                        entered is not accepted!\n")
                print("\033[1;31;40m  Choose from the above options!")

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
    progress_bar()
    spin_info(player)
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)
    print("\033[1;33;40m "*13 + f">>> You are betting €{bet} on \
            {lines} line(s) <<<" + " "*9)
    print("\033[1;33;40m "*21 + f">>> Total bet is €{total_bet} <<<" + " "*22)
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)
    reels = spin_mashine(ROWS, COLS, symbol_count)
    print_slot_mashine(reels)
    winnings, winning_lines = win_check(reels, lines, bet,
                                        symbol_value, player)
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
            player.win += values[symbol] * bet
            winning_lines.append(line+1)
            player.wins += 1
            print()
            print("\n" + "\033[1;33;40m "*15 + f"Congratulations \
                    {player.name}! You won!!!")
    print("\033[1;33;40m*"*66)
    print(f"\033[1;32;40m  >>>  {player.name}, you have won €{winnings}! \
            on line(s): ", *winning_lines)
    print("\033[1;31;40mx"*66)
    print(f"\033[1;31;40m  >>>  {player.name}, you have lost on line(s): \
            ", *loosing_lines)
    return winnings, winning_lines


def update_highscores(player):
    """
    updates the highscores
    """
    for count, rounds in enumerate(highscores_rounds[1:11], 2):
        if player.rounds > int(rounds[2]):
            print(f"\033[1;33;40m  >>>  Well done {player.name}, you made \
                    the top 10!\n")
            player_as_list = [player.name, player.place, player.rounds,
                              player.wins, player.win]
            highscores.append_row(player_as_list)
            highscores.sort((4, 'des'), range='A2:E99')
            highscores.delete_rows(12)
            break
    else:
        print(f"\033[1;31;40m  >>>  No can do {player.name}, \
                You didn't make the top 10\n")


def display_highscores():
    """
    Print highscores
    """
    print("\033[1;33;40m")
    col_len = {i: max(map(len, inner))
               for i, inner in enumerate(zip(*highscores_rounds))}
    for inner in highscores_rounds:
        for col, word in enumerate(inner):
            print(f"\033[1;33;40m{word:{col_len[col]}}",
                  end="\033[1;35;40m  >|<  ")
        print()

    print("\n" + "\033[1;34;40m>"*27 + " "*11 + "<"*28)
    input("\n\033[1;33;40m  >>>  Press Enter to return to main menu\n")
    clear_screen()


def run_menu(player):
    """
    Runs game Main Menu
    """
    while True:
        run_menu_info()
        print(f"\033[1;33;40m  {player.name}, choose option \
                from the list below:\n")
        print("\033[1;35;40m  >>>   Press 1 to >>> Play  Game <<<")
        print("\033[1;35;40m  >>>   Press 2 to >>> View Rules <<<")
        print("\033[1;35;40m  >>>   Press 3 to >>> View High-Scores <<<")
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
        elif value == "3":
            clear_screen()
            welcome_screen()
            highscores_info()
            display_highscores()
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
    if balance > 0:
        while True:
            clear_screen()
            if balance <= 0:
                game_over_info(player)
                main()
            else:
                print("\033[1;33;40m "*20 + f"+++  \
                        {player.name}, Round: {player.rounds}  +++")
                print("\033[1;33;40m "*22 + f"+++  \
                        You have won {player.wins} round(s)!  +++")
                print("\033[1;33;40m "*28 + f"+++  \
                        Total of €{player.win}  +++")
                print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
                print("\033[1;32;40m "*17 + f">>>  Current balance is \
                        €{balance}! <<<" + " "*16)
                print("\033[1;34;40m "*23 + ">>>  Let's play! <<<" + " "*23)
                print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
                answer = input("\033[1;31;40m>"*13 + "  Press >>> Enter t\
                        o Spin <<< (E for Exit)  " + "<"*9).upper()
                if answer == "E":
                    game_over_info(player)
                    time.sleep(2)
                    main()
                balance += spin(balance, player)
                player.balance = balance
                player.rounds += 1
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
    time.sleep(2)
    game_over_info(player)
    time.sleep(2)
    clear_screen()
    welcome_screen()
    progress_bar()
    run_menu(player)


def clear_screen():
    """
    Clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


# Progress bar function copied from https://stackoverflow.com
def progress_bar():
    # A List of Items need to print progress bar
    items = list(range(0, 57))
    lengh = len(items)
    # Initial call to print 0% progress
    print_progress_bar(0, lengh, prefix='\033[1;33;40mLoading: ', suffix='\
Complete', length=38)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.005)
        # Update Progress Bar
        print_progress_bar(i + 1, lengh, prefix='Progress:', suffix='Complete\
', length=38)


# Print iterations progress copied from https://stackoverflow.com
def print_progress_bar(iteration, total, prefix='', suffix='\
', decimals=1, length=100, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    by https://stackoverflow.com
    """
    percent = ("{0:." + str(decimals) + "f}\
").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    barr = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{barr}| {percent}% {suffix}', end=print_end)
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
    print("\033[1;35;10m     middle second -2- and bottom third -3-" + " "*22)
    print("\033[1;35;10m  3. There is: 3 x ♥, 4 x ♦, 6 x ♠ and 7 x ♣ symbols  \
            ")
    print("\033[1;35;10m  4. Valued at :  ♥ x 5, ♦ x 4, ♠ x 3 and ♣ x 2       \
            ")
    print("\033[1;35;10m  5. Min. bet is €1 and max is €100" + " "*31)
    print("\033[1;35;10m  6. Up/Down your deposit to change difficulty level")
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


def spin_info(player):
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)
    print("\033[1;35;10m "*20 + f">>>  Turn {player.rounds} Results  \
          <<<" + " "*20)
    print("\033[1;34;40m>"*25 + " "*16 + "<"*25)


def highscores_info():
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
    print("\033[1;35;10m "*20 + ">>>  Top 10 High-Scores <<<" + " "*19)
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)


def game_over_info(player):
    print("\033[1;34;40m>"*27 + " "*11 + "<"*28)
    print("\033[1;33;40m "*12 + f">>> {player.name} you played \
          {player.rounds} round(s)! <<<")
    print("\033[1;35;10m "*15 + f">>> You won {player.wins} time(s)! <<<")
    print("\033[1;35;10m "*18 + f">>> Total win of €{player.win}! <<<")
    print()
    update_highscores(player)
    updated_highscores = highscores.get_all_values()
    highscores_info()
    col_len = {i: max(map(len, inner))
               for i, inner in enumerate(zip(*updated_highscores))}

    for inner in updated_highscores:
        for col, word in enumerate(inner):
            print(f"\033[1;33;40m{word:{col_len[col]}}",
                  end="\033[1;35;40m  >|<  ")
        print()
    print("\033[1;35;10m>"*33 + "<"*33)
    print("\033[1;31;40m "*24 + ">>> GAME OVER <<<" + " "*25)
    print("\033[1;33;40m "*24 + ">>> Good-Bye! <<<" + " "*25)
    print("\033[1;35;10m>"*33 + "<"*33)
    print(f"\n\033[1;35;10m  >>>  Thanks for playing {player.name}!\n")
    answer = input("\033[1;33;40m  >>>  Press Enter to go to >>> MAIN MENU <<<\
                    (Q to Quit)  <<<    \n").upper()
    if answer == "Q":
        quit()


main()
