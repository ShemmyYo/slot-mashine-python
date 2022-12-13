import random

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
    functions returning random columns-symbols for reels
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
    function printing slot mashine by transposing column to line
    """
    print(f"\n-+-+-")
    for row in range(len(columns[0])):
        
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print(f"\n-+-+-")


def win_check(columns, lines, bet, values):
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
            print("Congratulations You won!")
            print(f"You have won €{winnings}! on line: ", *winning_lines)

    return winnings, winning_lines


def deposit():
    """
    function collecting user imput as deposit and checking 
    if input is a valid number
    """
    while True:
        amount = input(f"What's your deposit? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater then 0")
        else:
            print(f"NOTE: '{amount}', you entered is not accepted!\n")
            print("Please enter a valid amount again")
            print("Amount must be a number, and grater the1000n 0")

    print(f"Your deposit is: €{amount}\n")
    return amount


def get_number_of_lines(): 
    """
    function collecting user imput as number of lines to bet and 
    checking if input is a valid number
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ") (or press Q to Quit) ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines (between 1-{MAX_LINES})\n")
        elif lines == "q":
            break
        else:
            print(f"NOTE: '{lines}', you entered is not accepted!\n")
            print("Please enter a valid number of lines")
            print(f"Number of lines must be a number between 1 and {MAX_LINES}\n")

    print(f"You bet on {lines} lines\n")
    return lines


def get_bet():
    """
    function collecting user imput as the amount thats being bet by user
    and checking if input is a valid number
    """
    while True:
        bet = input("How much would you like to bet on each line? (or press Q to Quit) €")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between then €{MIN_BET} and €{MAX_BET}\n")
        elif bet == "q":
            break
        else:
            print(f"NOTE: '{bet}', you entered is not correct!\n")
            print("Please enter a valid bet amount again")
            print(f"Bet amount must be a number grater then €{MIN_BET} and €{MAX_BET}\n")

    print(f"Your bet amount is: €{bet}\n")
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

        if total_bet >= balance:
            print(f"Insufficient balance! Your current balance is €{balance}!\n")
        else:
            break

    print(f"You are betting €{bet} on {lines} lines")
    print(f"Total bet is €{total_bet}")

    reels = spin_mashine(ROWS, COLS, symbol_count)
    print_slot_mashine(reels)
    winnings, winning_lines = win_check(reels, lines, bet, symbol_value)
    return winnings - total_bet


def main():
    """
    main calling all required functions
    """
    balance = deposit()  
    while True:
        print(f"Current balance is €{balance}\n")
        answer = input("Press Enter to spin (Q to Quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Your balance is {balance}\n")
    print("Good-bye!")



main()