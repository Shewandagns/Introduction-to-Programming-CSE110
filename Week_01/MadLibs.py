# Mad Libs program

# Function to get user input for a specific word type
def get_word(word_type):
    return input(f"{word_type}: ")

# Function to capitalize the exclamation word
def capitalize_exclamation(exclamation):
    return exclamation.capitalize()

# Main program
adjective = get_word("adjective")
animal = get_word("animal")
verb1 = get_word("verb")
exclamation = capitalize_exclamation(get_word("exclamation"))
verb2 = get_word("verb")
verb3 = get_word("verb")

# Display the story with user's words
story = f"The other day, I was really in trouble. It all started when I saw a very\n" \
        f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all\n" \
        f"I could think to do was to {verb2} over and over. Miraculously,\n" \
        f"that caused it to stop, but not before it tried to {verb3}\n" \
        f"right in front of my family."

print("\nYour story is:\n")
print(story)