import random

def choose_secret_word():
    word_list = ["mosiah", "nephi", "lehi", "ether", "luke", "nelson",]
    return random.choice(word_list)

def get_hint(secret_word):

# List of hists or cattegories
    hints = {
        "mosiah": "He is a king in the Book of Mormon.",
        "nephi": "He is the son of Lehi",
        "lehi": "He was the first prophet in the Book of Mormon.",
        "ether": "He is the brother of Jared.",
        "luke": "One of the apostel of the Lord",
        "nelson": "the living prophet",
    }

# Get the hint for the choice secret word and Welcom the user to the game
    return hints.get(secret_word, "No hint available for this word.")

def play_game():
    secret_word = choose_secret_word()
    max_guesses = 5
    hint_for_secret_word = get_hint(secret_word)

    print(f"Welcom to the word guessing game! Here's a hint: {hint_for_secret_word}")

    guess = ""
    guess_count = 0
    hint = " _ " * len(secret_word)
    # give the user a hint how many latters are in the word
    print(f"Your hint is:{hint}")

    while secret_word != guess and guess_count < max_guesses:
        # Ask the user to input their guess
        guess = input("Please enetr your guess: ").lower()
        guess_count += 1

        if secret_word == guess:
            print("\nCongradulations! You guessed it!")
             # Inform the user how long it took them to guess the correct answer
            print(f"It took you {guess_count} number of guesses.")

        elif len(secret_word) != len(guess):
             # Inform the user to make number adjustmemt 
            print("\nSorry, your guess must have same number of letters as the secret word.")
    
        else:
            print("\nYour guess was incorrect!")
            # Provide hint for the user to imporove their guesses
            print(f"Your hint is:{hint}")

            for index, letter in enumerate(guess):
                if guess[index] == secret_word[index]:
                    # print the correct guesses who are in acctual spot in capital letter 
                    print(letter.upper(), end = " ")
                
                elif letter in secret_word:
                    # provide correct guesses who are not in acctual spot with small letter
                    print(letter.lower(), end = "")

                else:
                    print(" _ ", end = " ")

    # Check if the user ran out of guesses
    if guess_count == max_guesses and secret_word != guess:
        print(f"\nSorry, you've reached the maximum number of guesses ({max_guesses}). The secretword was'{secret_word}'.")    

    play_again = input("\nDO you want to play again? (yes/no): ").lower()
    return play_again == "yes"

# Start the game
while play_game():
    pass

