user_input = int(input("Please type a positive number: "))

while user_input < 0:
    print("Sorry, that is a negative number. Please try again.")
    user_input = int(input("Please type a positive number: "))

    print(f"The number is: {user_input}")


answer = ""

while answer != "yes":
    answer = input("May I have a piece of candy? ")

print("Thank you.")