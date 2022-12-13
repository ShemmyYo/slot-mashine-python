MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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


main()