# Get user input
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Calculate subtotal
subtotal = (num_children * child_price) + (num_adults * adult_price)

# Display subtotal
print(f"\nSubtotal: ${subtotal:.2f}")

# Get sales tax rate
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

# Calculate sales tax
sales_tax = (subtotal * sales_tax_rate) / 100

# Display sales tax
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate total price
total_price = subtotal + sales_tax

# Display total price
print(f"Total: ${total_price:.2f}")

# Get payment amount
payment_amount = float(input("\nWhat is the payment amount? "))

# Calculate and display change
change = payment_amount - total_price
print(f"Change: ${change:.2f}")
