"""
import
"""
import random
import time
import os
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)  # Colorama colours auto-reset

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
    f"{Fore.RED}♡": 3,
    f"{Fore.MAGENTA}♢": 4,
    f"{Fore.CYAN}♤": 6,
    f"{Fore.GREEN}♧": 7
}

symbol_value = {
    f"{Fore.RED}♡": 5,
    f"{Fore.MAGENTA}♢": 4,
    f"{Fore.CYAN}♤": 3,
    f"{Fore.GREEN}♧": 2
}


class Player:
    """
    Player class used to create player
    """
    def __init__(self, name, place, rounds, balance, wins, win):
        self.name = name
        self.place = place
        self.rounds = rounds
        self.balance = DEPOSIT
        self.wins = wins
        self.win = win


def player_details():
    """
    Prompting Player to provide their details
    """
    player_info()
    while True:
        player_name = input(f"{Fore.YELLOW}\
  >>>  What is your name Player? >>> ").capitalize()
        if player_name.isalpha():
            place = False
            while not place:
                player_city = input(f"{Fore.YELLOW}\
  >>>  Which city are you from? >>> ").capitalize()
                if player_city.isalpha():
                    player = Player(name=player_name, place=player_city,
                                    rounds=1, balance=DEPOSIT, wins=0, win=0)
                    return player
                else:
                    print(f"{Fore.RED}  '{player_city}' is not valid")
                    print(f"{Fore.YELLOW}{Back.RED}  !!!  Only letters please")
        else:
            print(f"\n{Fore.RED}  '{player_name}' is not valid")
            print(f"{Fore.YELLOW}{Back.RED} !!!  Only letters please ")


def deposit(player):
    """
    Collects user imput as deposit and implements checks
    if input is a valid number and prints msg.
    """
    deposit_info()
    print(f"{Fore.YELLOW}\
    {player.name}, your default deposit is €{DEPOSIT} ")
    print(f"\n{Fore.RED}  >>> Press 'C' to change deposit/difficulty level")
    answer = input(f"{Fore.GREEN}  >>> Press Enter to continue ").upper()
    if answer == "C":
        print(f"\n{Fore.YELLOW}\
    {player.name}, lets's get your deposit set!\n")
        print(f"{Fore.RED}  >>>  Press '1' to set it to €50 (hard)")
        print(f"{Fore.WHITE}  >>>  Press '2' to set it tt €100 (normal)")
        print(f"{Fore.GREEN}  >>>  Press '3' to set it to €200 (easy)")
        while True:
            selection = input(f"\n{Fore.YELLOW}\
    {player.name}, what's your decision? ").upper()
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
                print(f"\n{Fore.YELLOW}{Back.RED}\
    !!!  NOTE: '{selection}', you entered is not accepted!\n")
                print(f"{Fore.RED}  Choose from the above options!")

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
        lines = input(f"{Fore.YELLOW}\
  Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?  >>> ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"{Fore.YELLOW}{Back.RED}\
  !!!  NOTE: Enter a valid number of lines (between 1-{MAX_LINES})\n")
        else:
            print(f"{Fore.YELLOW}{Back.RED}\
  !!!  NOTE: '{lines}', you entered is not accepted!\n")
            print(f"{Fore.MAGENTA} Please enter a valid number of lines")
            print(f"{Fore.MAGENTA}\
 Number of lines must be a number between  1 and {MAX_LINES}\n")
            lines = 0
    print(f"{Fore.GREEN}  >>>  You bet on {lines} lines")
    return lines


def get_bet():
    """
    Collects user imput as the amount thats being bet by user,
    checks if input is a valid number and prints msg
    """
    get_bet_info()
    while True:
        bet = input(f"{Fore.YELLOW}\
  How much would you like to bet on each line?  >>> €")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"{Fore.YELLOW}{Back.RED}\
  !!!  NOTE: Bet amount must be between €{MIN_BET} and €{MAX_BET}\n")
        else:
            print(f"{Fore.YELLOW}{Back.RED}\
  !!!  NOTE: '{bet}', you entered is not correct!\n")
            print(f"{Fore.MAGENTA} Please enter a valid bet amount again")
            print(f"{Fore.MAGENTA}\
 Bet amount must be a number between €{MIN_BET} and €{MAX_BET}\n")
    print(f"{Fore.GREEN}  >>> Your bet amount is: €{bet}\n")
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
            print(f"{Fore.RED}  >>>  {player.name}  <<<")
            print(f"{Fore.RED}\
  >>>  Insufficient balance to cover {lines} line(s)!\n")
            time.sleep(1.5)
        else:
            break
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"{Fore.RED}  >>>  {player.name}  <<<")
            print(f"{Fore.RED}\
  >>>  Balance won't cover {lines} line(s) you wish to bet on €{bet} each!")
            print(f"{Fore.RED}  >>>  Your current balance is €{balance}!\n")
            time.sleep(1.5)
        else:
            break
    progress_bar()
    spin_info(player)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*16 + "<"*25)
    print(f"{Fore.YELLOW} "*13 + f">>> You are betting €{bet} on \
{lines} line(s) <<<" + " "*9)
    print(f"{Fore.YELLOW} "*21 + f">>> Total bet is €{total_bet} <<<" + " "*22)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*16 + "<"*25)
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
    print(f"{Fore.YELLOW} " + "  --<+>>>>X<<<<+>--  "*3 + "  ")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(f"{Fore.YELLOW}      |  ", f"{Fore.RED}\
", column[row], end=f"{Fore.YELLOW}    |    ")
            else:
                print(f"{Fore.YELLOW}      |  ", f"{Fore.RED}\
", column[row], end=f"{Fore.YELLOW}    |       ")
        print(f"\n{Fore.YELLOW} " + "  --<+>>>>X<<<<+>--  "*3 + "  ")
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
            print("\n" + f"{Fore.YELLOW} "*15 + f"Congratulations \
{player.name}! You won!!!")
    print(f"{Fore.GREEN}*"*66)
    print(f"{Fore.GREEN}  {player.name}, you have won €{winnings}! \
on line(s): ", *winning_lines)
    print(f"{Fore.RED}x"*66)
    print(f"{Fore.RED}  >>>  {player.name}, you have lost on line(s): \
", *loosing_lines)
    return winnings, winning_lines


def update_highscores(player):
    """
    updates the highscores
    """
    for count, rounds in enumerate(highscores_rounds[1:11], 2):
        if player.rounds > int(rounds[2]):
            print(f"{Fore.RED}{Back.GREEN}\
  >>>  Well done {player.name}, you made the top 10!\n")
            player_as_list = [player.name, player.place, player.rounds,
                              player.wins, player.win]
            highscores.append_row(player_as_list)
            highscores.sort((5, 'des'), range='A2:E99')
            highscores.delete_rows(12)
            break
    else:
        print(f"{Fore.YELLOW}{Back.RED}\
  >>>  No can do {player.name}, You didn't make the top 10\n")


def display_highscores():
    """
    Print highscores
    """
    print()
    col_len = {i: max(map(len, inner))
               for i, inner in enumerate(zip(*highscores_rounds))}
    for inner in highscores_rounds:
        for col, word in enumerate(inner):
            print(f"{Fore.YELLOW}{word:{col_len[col]}}",
                  end=f"{Fore.MAGENTA} >|<  ")
        print()

    print("\n" + f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)
    input(f"\n{Fore.YELLOW}  >>>  Press Enter to return to main menu\n")
    clear_screen()


def run_menu(player):
    """
    Runs game Main Menu
    """
    while True:
        run_menu_info()
        print(f"{Fore.YELLOW}\
  {player.name}, choose option from the list below:\n")
        print(f"{Fore.GREEN} >>>   Press 1 to >>> Play  Game <<<")
        print(f"{Fore.CYAN} >>>   Press 2 to >>> View Rules <<<")
        print(f"{Fore.MAGENTA} >>>   Press 3 to >>> View High-Scores <<<")
        print("")
        print(f"{Fore.RED} >>>   Press Q to >>> Quit  Game <<<\n")
        value = input(f"{Fore.YELLOW}  >>>  Option: ").upper()
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
            print(f"{Fore.RED}  '{value}' is not valid!")
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
            print(f"{Fore.RED}" + "*"*27 + " "*11 + "*"*28)
            print(f"{Fore.YELLOW}" + " "*20 + f"+++  {player.name}, Round: \
{player.rounds}  +++")
            print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)
            print(" "*17 + f"{Fore.CYAN}>>>  Current balance is \
€{balance}! <<<" + " "*16)
            if balance <= 0:
                game_over_info(player)
                main()
            else:
                print(" "*23 + f"{Fore.MAGENTA}>>>  Let's play! <<<" + " "*23)
                print(f"{Fore.MAGENTA}" + ">"*27 + " "*11 + "<"*28)
                print(f"{Fore.GREEN}  >>>  Press Enter to Spin <<<")
                answer = input(f"{Fore.RED}  >>>  'R' to Reset Game").upper()
                if answer == "R":
                    game_over_info(player)
                    time.sleep(2)
                    main()
                balance += spin(balance, player)
                player.balance = balance
                player.rounds += 1
                input(f"\n{Fore.YELLOW}  >>>  Press Enter to continue\n")
    else:
        print(f"  Your ballance is €{balance}!")
        input(f"\n{Fore.YELLOW}  >>>  Press Enter to continue\n")
    progress_bar()
    clear_screen()
    welcome_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*27)
    print("\n" + " "*18 + f"{Fore.GREEN}>>> Final balance is €{balance} <<\n")
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


def progress_bar():
    """
    Progress bar function copied from https://stackoverflow.com
    A List of Items need to print progress bar
    Initial call to print 0% progress
    Update Progress Bar
    """
    items = list(range(0, 57))
    lengh = len(items)
    print_progress_bar(0, lengh, prefix=f'{Fore.YELLOW}Loading: ', suffix='\
Complete', length=38)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.005)
        print_progress_bar(i + 1, lengh, prefix='Loading:', suffix='Complete\
', length=38)


def print_progress_bar(iteration, total, prefix='', suffix='\
', decimals=1, length=100, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    by https://stackoverflow.com
    Print iterations progress
    Print New Line on Complete
    """
    percent = ("{0:." + str(decimals) + "f}\
").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    barr = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{barr}| {percent}% {suffix}', end=print_end)
    if iteration == total:
        print()


# messages displayed on screen listed below:
def welcome_screen():
    clear_screen()
    print(f"{Fore.YELLOW}*"*66)
    print(" "*17 + f"{Fore.GREEN}Welcome to One-Armed Bandit!" + " "*21)
    print()
    print(f"{Fore.CYAN}*"*66)
    print(f"{Fore.MAGENTA}{Style.NORMAL}\
    ####  ##   ## #####      ####  #####  ##   ## ##### #####     ")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}\
   ##  ## ###  ## ##        ##  ## ##  ## ### ### ##    ##  ##    ")
    print(f"{Fore.CYAN}{Style.NORMAL}\
   ##  ## ## #### ####  ##  ###### #####  ## # ## ####  ##  ##    ")
    print(f"{Fore.CYAN}{Style.BRIGHT}\
   ##  ## ##  ### ##        ##  ## ## ##  ##   ## ##    ##  ##    ")
    print(f"{Fore.WHITE}\
    ####  ##   ## #####     ##  ## ##  ## ##   ## ##### #####     ")
    print()
    print(f"{Fore.WHITE}\
        ####     ####   ##   ##  #####   ##  ######   ##          ")
    print(f"{Fore.CYAN}{Style.BRIGHT}\
        ##  ##  ##  ##  ###  ##  ##  ##  ##    ##     ##          ")
    print(f"{Fore.CYAN}{Style.NORMAL}\
        #####   ######  ## ####  ##  ##  ##    ##     ##          ")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}\
        ##  ##  ##  ##  ##  ###  ##  ##  ##    ##                 ")
    print(f"{Fore.MAGENTA}{Style.NORMAL}\
        ####    ##  ##  ##   ##  #####   ##    ##     ##          ")
    print()
    print(f"{Fore.CYAN}*"*66)
    print(" "*26 + f"{Fore.RED}by ShemmyYo" + " "*29)
    print(f"{Fore.CYAN}*"*66)


def intructions(player):
    """
    instructions printed when option 2 pressed from main menu
    """
    welcome_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*14 + "<"*27)
    print(f"{Fore.GREEN} "*22 + ">>> Instructions <<<" + " "*24)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*14 + "<"*27)
    print(f"{Fore.YELLOW}-"*66)
    print(f"{Fore.MAGENTA}\
  The aim of the game is to make sure that all of the symbols     ")
    print(f"{Fore.MAGENTA}\
  on the screen of the machine match up in line" + " "*19)
    print(f"{Fore.MAGENTA}\
  Get them all, and you'll win the money!" + " "*25)
    print(f"{Fore.YELLOW}="*66)
    print(f"{Fore.MAGENTA}\
  1. Only horizontal 1 to 3 lines can be bet on" + " "*19)
    print(f"{Fore.MAGENTA}\
  2. When betting on lines you start betting on top line -1- first")
    print(f"{Fore.MAGENTA}\
     middle -2- second and bottom -3- third." + " "*22)
    print(f"{Fore.MAGENTA}\
  3. There is: 3 x ♥, 4 x ♦, 6 x ♠ and 7 x ♣ symbols              ")
    print(f"{Fore.MAGENTA}\
  4. Valued at :  ♥ - 5, ♦ - 4, ♠ - 3 and ♣ - 2                   ")
    print(f"{Fore.MAGENTA}  5. Min. bet is €1 and max is €100" + " "*31)
    print(f"{Fore.YELLOW}="*66)
    print(f"{Fore.GREEN}  {player.name},")
    print(f"{Fore.MAGENTA}\
  all you need is a bag of change and you're ready to go!         ")
    print(f"{Fore.YELLOW}-"*66)
    print(f"{Fore.YELLOW}  >>>  Press Enter to go to >>> MAIN MENU <<<")
    answer = input(f"{Fore.RED}  >>>  Q to Quit \n").upper()
    if answer == "Q":
        quit()


def game_over_info(player):
    """
    game over printed what the end of the game or when user quits
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)
    print(f"{Fore.YELLOW} "*15 + f">>> {player.name} you played \
{player.rounds} round(s)! <<<")
    print(" "*18 + f"{Fore.GREEN}>>> You won {player.wins} time(s)! <<<")
    print(" "*21 + f"{Fore.GREEN}>>> Total win of €{player.win}! <<<")
    print()
    update_highscores(player)
    time.sleep(1)
    updated_highscores = highscores.get_all_values()
    highscores_info()
    col_len = {i: max(map(len, inner))
               for i, inner in enumerate(zip(*updated_highscores))}

    for inner in updated_highscores:
        for col, word in enumerate(inner):
            print(f"{Fore.YELLOW}{word:{col_len[col]}}",
                  end=f"{Fore.MAGENTA} >|<  ")
        print()
    print()
    print(f"{Fore.WHITE}{Back.RED}><"*33)
    print(" "*24 + f"{Fore.RED}>>> GAME OVER <<<" + " "*25)
    print(" "*24 + f"{Fore.YELLOW}>>> Good-Bye! <<<" + " "*25)
    print(f"{Fore.WHITE}{Back.RED}><"*33)
    print(f"\n{Fore.GREEN} >>>  Thanks for playing {player.name}!\n")
    print(f"\n{Fore.YELLOW}  >>>  Press Enter to go to MAIN MENU")
    answer = input(f"{Fore.RED}  >>>  Q to Quit \n").upper()
    if answer == "Q":
        quit()


def run_menu_info():
    """
    message printed by calling main menu
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)
    print(" "*24 + f"{Fore.GREEN}>>> MAIN MENU <<<" + " "*25)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)


def player_info():
    """
    message printed by calling function
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)
    print(" "*23 + f"{Fore.GREEN}>>> Player Info <<<" + " "*24)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)


def deposit_info():
    """
    message printed by calling function
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)
    print(" "*24 + f"{Fore.GREEN}>>>  Deposit  <<<" + " "*25)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)


def get_number_of_lines_info():
    """
    message printed by calling function
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*15 + "<"*26)
    print(" "*22 + f"{Fore.GREEN}>>>  No of Lines  <<<" + " "*23)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*15 + "<"*26)


def get_bet_info():
    """
    message printed by calling function
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*16 + "<"*25)
    print(" "*22 + f"{Fore.GREEN}>>>  Bet per Line  <<<" + " "*22)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*16 + "<"*25)


def spin_info(player):
    """
    message printed by calling function
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*16 + "<"*25)
    print(" "*20 + f"{Fore.GREEN}\
>>>  Turn {player.rounds} Results  <<<" + " "*20)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*25 + " "*16 + "<"*25)


def highscores_info():
    """
    message printed by calling function
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)
    print(" "*20 + f"{Fore.GREEN}>>>  Top 10 High-Scores <<<" + " "*19)
    print(f"{Fore.CYAN}{Style.BRIGHT}" + ">"*27 + " "*11 + "<"*28)


main()
