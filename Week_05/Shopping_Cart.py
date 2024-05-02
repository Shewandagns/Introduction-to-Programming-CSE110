# Welcome message
print("Welcome to the Shopping Cart Program!\n")

# List to store items
shopping_cart = []

# Main loop to handle user actions
while True:
    
    # Display menu options
    print("""
Please select one of the following: 
1. Add item 
2. View cart
3. Remove item
4. Compute total
5. Quit
""")
    # Prompt user for an action
    option = input("Please enter an action: ")

    # Add item to the cart
    if option == '1':
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        print(f"'{item}' has been added to the cart.\n")

    # View items in the cart
    elif option == '2':
        if shopping_cart:
            print("The contents of the shopping cart are:")
            for item in shopping_cart:
                print(item)
        else:
            print("Your cart is empty.")
        print()

    # Remove item from the cart
    elif option == '3':
        if shopping_cart:
            print("The contents of the shopping cart are:")
            for i, item in enumerate(shopping_cart, start=1):
                print(f"{i}. {item}")
            try:
                remove_item = int(input("Please enter the number of the item you want to remove: "))
                if 1 <= remove_item <= len(shopping_cart):
                    removed_item = shopping_cart.pop(remove_item - 1)
                    print(f"'{removed_item}' has been removed from the cart.\n")
                else:
                    print("Invalid item number. Please enter a valid number.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        else:
            print("Your cart is empty. There are no items to remove.\n")

    # Compute total (not implemented)
    elif option == '4':
        if shopping_cart:
            print("Compute total feature is not available in this version.\n")
        else:
            print("Your cart is empty. There are no items to compute the total.\n")

    # Quit the program
    elif option == '5':
        print("Thank you. Goodbye.")
        break

    # Invalid option
    else:
        print("Invalid option. Please select a number between 1 and 5.\n")
