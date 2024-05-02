"""grade = int(input("What is your grade percentage? "))
    
if grade >= 90:
  print("Your grade is A. \nCongradulation! you have passed the class.")
elif grade >= 80:
  print("your grade is B. \nCongradulation! you have passed the class.")
elif grade >= 70:
  print("Your grade is C. \nCongradulation! you have passed the class.")
elif grade >= 60:
  print("Your grade is D. \nSorry you didn't pass the class.")
else:
  print("Your grade is F. \nSorry you didn't pass the class.")
"""

# Ask the user to input the grade percentage 
grade = int(input("What is your percentage? "))

# Determine the grade based on what is provided from the user
if grade >= 90:
    letter = "A"
elif grade >= 80: 
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# strech Challenge
last_digit = grade % 10

if last_digit >= 7: sign = "+" 
elif last_digit < 3: sign = "-"

# Adjust sign for grade range
if grade >= 93 or letter == "F": sign = ""

# Display grade 
print(f"Your grade is: {letter}{sign}")

# Print a message based on the grade
if grade >= 70:
    print("Congradulations! You have passed your class.")
else:
    print("Sorry you did not pass. You can try again.")
