# Mad Libs program with additional elements and "a" or "an" usage

# Function to get user input for a specific word type
def get_word(word_type):
    return input(f"{word_type}: ")

# Function to capitalize the exclamation word
def capitalize_exclamation(exclamation):
    return exclamation.capitalize()

# Main program
adjective1 = get_word("adjective")
animal1 = get_word("animal")
verb1 = get_word("verb")
exclamation = capitalize_exclamation(get_word("exclamation"))
verb2 = get_word("verb")
noun = get_word("noun")
adjective2 = get_word("adjective")
adverb = get_word("adverb")
adjective3 = get_word("adjective")
animal2 = get_word("animal")
verb3 = get_word("verb")
adjective4 = get_word("adjective")
plural_noun = get_word("plural noun")
number = get_word("number")

# Display the story with user's words and additional elements
story = f"The other day, I was really in trouble. It all started when I saw a very\n" \
        f"{adjective1} {animal1} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all\n" \
        f"I could think to do was to {verb2} over and over. Miraculously,\n" \
        f"that caused it to stop, but not before it tried to {verb3}\n" \
        f"right in front of my family. My {noun} felt {adjective2}, and I had to\n" \
        f"{adverb} {adjective3} to escape. I never thought a {animal2} could be so\n" \
        f"{verb3} and {adjective4}! Suddenly, I noticed {plural_noun} appearing from\n" \
        f"nowhere, numbering about {number}. It was like a scene from a crazy movie."

# Print the story
print("\nYour story is:\n")
print(story)
