names = []

new_name = ""
while new_name != "end":
    new_name = input("Type the name of a friend: ")
    if new_name != "end": #Check if the input is not "end"
        names.append(new_name)


# remove the least element if it is "end"
if names and names[-1] == "end":
     names.pop()

print("\nYour friends are:")
for name in names:
    print(name)

