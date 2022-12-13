def deposit():
    while True:
        amount = input("What's your deposit? €\n")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than 0")
        else:
            print("Please enter a valid amount again")
            print("Amount must be grater than 0")

    print("Thank  You!")
    print(f"Your deposit is: €{amount}")
    return amount


deposit() 