# Creativity: Displays the number of items in the cart when viewing or removing items.
# Shopping Cart Program
# Author - Tope Jinad

names = []
prices = []

while True:
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")

    if choice == "1":
        item = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of '{item}' ?"))
        names.append(item)
        prices.append(item_price)
        print(f"'{item}' has been added to cart.")

    elif choice == "2":
        if len(names) == 0:
            print("Your cart is empty.")
        else:
            print(f"The contents of the shopping cart are ({len(names)} item(s)):")
            for index, name in enumerate(names):
                print(f"{index + 1}. {name} - ${prices[index]:.2f}")

    elif choice == "3":
        if len(names) == 0:
            print("Your cart is empty. Nothing to remove.")
        else:
            print(f"The contents of the shopping cart are ({len(names)} item(s)):")
            for index, name in enumerate(names):
                print(f"{index + 1}. {name} - ${prices[index]:.2f}")
            item_number = int(input("Enter the number of the item you want to remove: "))
            if 1 <= item_number <= len(names):
                removed_item = names.pop(item_number - 1)
                removed_price = prices.pop(item_number - 1)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Invalid item number.")

    elif choice == "4":
        if len(names) == 0:
         print("Your cart is empty.")
        else:
         total = sum(prices)
         print(f"The total price of the items in the cart is ${total:.2f}")
    elif choice == "5":
         print("Thank you. Goodbye.")
         break

    else:
        print("Invalid option. Please enter a number from 1 to 5.")