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


def spin_mashine(rows, cols, symbols):
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
    print(f"\n-+-+-")
    for row in range(len(columns[0])):
        
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print(f"\n-+-+-")


def deposit():
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
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines (between 1-{MAX_LINES})\n")
        else:
            print(f"NOTE: '{lines}', you entered is not accepted!\n")
            print("Please enter a valid number of lines")
            print(f"Number of lines must be a number between 1 and {MAX_LINES}\n")

    print(f"You bet on {lines} lines\n")
    return lines


def get_bet():
    while True:
        bet = input(f"How much would you like to bet on each line? €")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between then €{MIN_BET} and €{MAX_BET}\n")
        else:
            print(f"NOTE: '{bet}', you entered is not correct!\n")
            print("Please enter a valid bet amount again")
            print(f"Bet amount must be a number grater then €{MIN_BET} and €{MAX_BET}\n")

    print(f"Your bet amount is: €{bet}\n")
    return bet

def main():
    balance = deposit()  
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


main()