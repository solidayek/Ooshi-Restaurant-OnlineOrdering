def drinks():
    # Define drink codes
    milkTea = 1
    taroTea = 2
    matchaLatte = 3
    cocaCola = 4
    pepsi = 5
    sprite = 6

    # Define the list of drinks
    boba = ["1 Milk Tea", "2 Taro Tea", "3 Matcha Latte"]
    soda = ["4 Coca-Cola", "5 Pepsi", "6 Sprite"]

    # Join the lists into strings
    result = ', '.join(boba)
    print("Boba Drinks: " + result)

    result1 = ', '.join(soda)
    print("Soda Drinks: " + result1)


def main():
    text = "Welcome to Ooshi Restaurant"
    width = 60  # Adjust the width as needed

    centered_text = text.center(width)

    print(centered_text)

    Burger = 1
    Sushi = 2
    Steak = 3
    Noodles = 4
    Chow_Mein = 5

    balance = 0

    print("1 Burger\n2 Sushi\n3 Steak\n4 Noodles\n5 Chow Mein")
    done = False

    while not done:
        print("Enter your order in respective to their codes. For example, 1 for Burger, 5 for Chow Mein")
        userInput = input("Enter your order: ")

        try:
            userOrder = int(userInput)
        except ValueError:
            print("Invalid input. Please enter a valid order code.")
            continue

        if userOrder == Burger:
            print("You ordered a Burger. Thank you!")
            balance += 5
        elif userOrder == Sushi:
            print("You ordered Sushi. Thank you!")
            balance += 10
        elif userOrder == Steak:
            print("You ordered Steak. Thank you!")
            balance += 15
        elif userOrder == Noodles:
            print("You ordered Noodles. Thank you!")
            balance += 8
        elif userOrder == Chow_Mein:
            print("You ordered Chow Mein. Thank you!")
            balance += 9
        else:
            print("Invalid order code. Please select a valid item from the menu.")

        anotherOrder = input("Would you like to order something else? (yes/no/others): ").lower()
        if anotherOrder != 'yes' and anotherOrder != 'others':
            done = True
        elif anotherOrder == 'others':
            drinks()
            print("Enter your order for drinks in respective to their codes.")
            while True:
                userOrder = input("Enter your drink order (1 for Milk Tea, 2 for Taro Tea, etc.): ")
                if userOrder == '1':
                    print("You ordered a milk tea.")
                    balance += 4
                elif userOrder == '2':
                    print("You ordered a taro tea.")
                    balance += 3.5
                elif userOrder == '3':
                    print("You ordered a matcha latte.")
                    balance += 4.5
                elif userOrder == '4':
                    print("You ordered a coca cola.")
                    balance += 3.5
                elif userOrder == '5':
                    print("You ordered a pepsi.")
                    balance += 3.5
                elif userOrder == '6':
                    print("You ordered a sprite.")
                    balance += 3.5
                else:
                    print("Invalid drink code. Please select a valid drink from the menu.")
                more_drinks = input("Would you like to order more drinks? (yes/no): ").lower()
                if more_drinks != 'yes':
                    break

    print("Your total balance is $", balance)
    print("Enjoy your meal at Ooshi Restaurant! Come back for more")

main()
