print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number 
print(f"The sum is: {sum}")

count = len(numbers)
average = sum / count

print(f"\nThe average is: {average}")

best_fo_far = -1

for number in numbers:

    if number > best_fo_far:
        best_fo_far = number

print(f"The largest number is: {best_fo_far}")

# Strech Challenge

smallest_so_far = 9999

for number in numbers:
    if number > 0 and number < smallest_so_far:
        smallest_so_far = number

print(f"The smallest positive number is: {smallest_so_far}")

sorted_list = sorted(numbers)

print("\nThe sorted list is: ")

for number in sorted_list:
    print(number)




