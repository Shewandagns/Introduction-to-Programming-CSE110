# Welcome message
print("Welcome to the Shopping Cart Program!\n")

# List to store items and their prices
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

    option = input("Please enter an action: ")

    if option == '1':
        # Promt user for item name, price, and quantity
        item = input("What item would you like to add? ")
        price = float(input(f"What is the prices of '{item}'? "))
        quantity = int(input("Enter quantity: "))

        # Add item information to shopping cart as a dictionary
        shopping_cart.append({'item': item, 'price': price, 'quantity': quantity})
        print(f"'{quantity} {item}' has been added to the cart.\n")

    elif option == '2':
        if shopping_cart:

            # Display the contents of the shopping cart with better formatting
            print("The contents of the shopping cart are:")

            # Additional Features: Role Number and quantity in View Cart
            print("{:<5} {:<5} {:20} {:<10} {:<10}".format("Role", "Qty", "Item", "Price", "Total")) 
            for i, item_info in enumerate(shopping_cart, start=1):
                total_price = item_info['price'] * item_info['quantity']
                print("{:<5} {:<5} {:<20} ${:<10.2f} ${:<10.2f}".format(i, item_info['quantity'], item_info['item'], item_info['price'], total_price))
            
        else:
            print("Your cart is empty.")
        print()

    elif option == '3':
        # Remove item from the shopping cart
        if shopping_cart:

            print("The contents of the shopping cart are:")
            
            # The role number allows users to easily identify and select items for removal.
            # Improves user experience by providing clearer navigation and interaction with the shopping cart.
            print("{:<5} {:<5} {:20} {:<10} {:<10}".format("Role", "Qty", "Item", "Price", "Total"))
            for i, item_info in enumerate(shopping_cart, start=1):
                total_price = item_info['price'] * item_info['quantity']
                print("{:<5} {:<5} {:<20} ${:<10.2f} ${:<10.2f}".format(i, item_info['quantity'], item_info['item'], item_info['price'], total_price))

            try:
                remove_item = int(input("Please enter the number of the item you want to remove: "))

                if 1 <= remove_item <= len(shopping_cart):                  
                    removed_item = shopping_cart.pop(remove_item - 1)
            
                    print("Item removed.\n")

                else:
                    print("Invalid item number. Please enter a valid number.\n")

            except ValueError:
                print("Invalid input. Please enter a number.\n")

        else:
            print("Your cart is empty. There are no items to remove.\n")


    elif option == '4':
        
        # Compute total price of items in the shopping cart
        if shopping_cart:
            total = sum(item_info['price'] * item_info['quantity'] for item_info in shopping_cart)
            print(f"The total price of the items in the shopping cart is ${total:.2f}.\n")

        else:
            print("Your cart is empty. There are no items to compute the total.\n")

    # Quit the program
    elif option == '5':
        print("Thank you. Goodbye.")
        break

    # Invalid option
    else:
        print("Invalid option. Please select a number between 1 and 5.\n")
