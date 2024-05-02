print("On the scale of 1 to 10, answer the following quastions.")
loan = int(input("How larg is your loan? "))
credit = int(input("How good is your credit hidtory? "))
income = int(input("How is your income? "))
payment = int(input("How larg is your down payment? "))

if loan >= 5:
    if credit >= 7 and income >= 7:
        decision = True
    elif credit >= 7 or income >= 7:
        decision = payment >= 5
    else:
        decision = False

else:
    if credit < 4:
        decision = False
    else:
        decision = (income >= 7 or payment >= 7) or (income >= 4 and payment >= 4)

if decision:
    print("Congradulations! You are qualified for the loan.")
else:
    print("Sorry, You did not qualify for the loan.")


