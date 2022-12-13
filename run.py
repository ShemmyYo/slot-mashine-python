MAX_LINES = 3

def deposit():
    while True:
        amount = input(f"What's your deposit? €\n")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than 0")
        else:
            print(f"'{amount}', you entered is invalid\n")
            print("Please enter a valid amount again")
            print("Amount must be a number, and grater than 0")

    print("Thank  You!")
    print(f"Your deposit is: €{amount}")
    return amount


def get_number_of_lines(): 
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?\n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines (between 1-{MAX_LINES})\n")
        else:
            print(f"'{lines}', you entered is invalid\n")
            print("Please enter a valid number of lines")
            print(f"Number of lines must be a number between 1 and {MAX_LINES}\n")

    print("Thank  You!")
    print(f"You bet {lines} lines\n")
    return lines


def main():
    balance = deposit()  
    lines = get_number_of_lines()


main()