
# Get user input
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Calculate subtotal for meals
subtotal = (num_children * child_price) + (num_adults * adult_price)

# Display meal subtotal
print(f"\nMeal Subtotal: ${subtotal:.2f}")

# Get user input for drinks and appetizers
drink_price = float(input("\nWhat is the price of a drink? "))
appetizer_price = float(input("What is the price of an appetizer? "))
num_drinks = int(input("How many drinks are there? "))
num_appetizers = int(input("How many appetizers are there? "))

# Calculate subtotal for drinks and appetizers
print()
extras_subtotal = (num_drinks * drink_price) + (num_appetizers * appetizer_price)

# Display extras subtotal
print(f"Extras Subtotal: ${extras_subtotal:.2f}")

# Calculate total subtotal
subtotal = subtotal + extras_subtotal

# Display total subtotal
print(f"Total Subtotal: ${subtotal:.2f}")

# Get sales tax rate
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

# Calculate sales tax
sales_tax = (subtotal * sales_tax_rate) / 100

# Display sales tax
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate total price including sales tax
total_price = subtotal + sales_tax

# Display total price
print(f"Total: ${total_price:.2f}")

# Get user input for tip percentage
tip_percentage = float(input("\nWhat is the tip percentage? "))

# Calculate tip
tip = (total_price * tip_percentage) / 100

# Display tip
print(f"Tip: ${tip:.2f}")

# Calculate final total with tip
final_total = total_price + tip

# Display final total
print(f"Final Total: ${final_total:.2f}")

# Get payment amount
payment_amount = float(input("\nWhat is the payment amount? "))

# Calculate and display change
change = payment_amount - final_total
print(f"Change: ${change:.2f}")

