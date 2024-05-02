import time

# Additional creativity to display the message in delay print
def delay_print(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def start_game():
    # Welcome message and initial riddle
    delay_print("Welcome to the Enchanted Forest Adventure!")
    delay_print("You find yourself at the entrance of a magical forest. A talking OWL appears and says:")
    delay_print("'To proceed, answer my riddle: What has keys but can't open locks?' ")

    # User input for the riddle
    user_input = input().lower()

    # Check if the user's answer is correct
    if "piano" in user_input:
        delay_print("\nCorrect! The owl nods and guides you deeper into the forest.")
        forest_path()
    else:
        delay_print("Incorrect! The owl hoots disapprovingly. The forest entrance fades away. Game Over.")

def forest_path():
    # Introduction to the forest path
    delay_print("\nAs you venture further, you encounter a MYSTERIOUS STREAM, a GLOWING CAVE entrance and a SECRET DOOR.")
    delay_print("Which path will you choose?")

    # Loop to handle user input until a valid choice is made
    while True:
        delay_print("1. Follow the MYSTERIOUS STREAM")
        delay_print("2. Enter the GLOWING CAVE")
        delay_print("3. Open the SECRET DOOR")

        # User input for the forest path choice
        user_choice = input().lower()

        # Check the user's choice and proceed accordingly
        if user_choice == "mysterious stream":
            delay_print("\nYou follow the stream and encounter a friendly WATER NYMPH.")
            delay_print("She offers you a magical DRINK. Do you ACCEPT or REFUSE?")

            # Nested loop for the second level of choices
            while True:
                delay_print("1. ACCEPT the magical drink")
                delay_print("2. REFUSE the offer")

                # User input for the second-level choice
                user_choice = input().lower()

                # Check the second-level choice and proceed accordingly
                if user_choice == "accept":
                    congratulations()
                    return
                elif user_choice == "refuse":
                    delay_print("\nThe water nymph looks disappointed. She vanishes, and you continue your journey.")
                    forest_path()
                else:
                    delay_print("Invalid choice. Please enter 'accept' or 'refuse'.")

        elif user_choice == "secret door":
             delay_print("\nYou enter the door and encounter a monster.")
             delay_print("Would you like to RUN or ATTAK?")

             # Nested loop for the second level of choices
             while True:
                 delay_print("1. ATTAK")
                 delay_print("2. RUN")

                 # User input for the second-level choice
                 user_choice = input().lower()

                 # Check the second-level choice and proceed accordingly
                 if user_choice == "attak":
                     congratulations()
                     return
                 elif user_choice == "run":
                     delay_print("You choose to run, unfortunatly the monster followed you and killed you.")
                     delay_print("\nSorry, you lost the game")
                     forest_path()
                 else:
                     delay_print("Invalid choice. Please enter 'attak' or 'run'.")                    

        elif user_choice == "glowing cave":
            delay_print("\nYou enter the glowing cave and find yourself in a room with FLOATING CRYSTALS.")
            delay_print("Do you TOUCH the crystals or IGNORE them?")

            # Another nested loop for the second level of choices
            while True:
                delay_print("1. TOUCH the floating crystals")
                delay_print("2. IGNORE the crystals")

                # User input for the second-level choice
                user_choice = input().lower()

                # Check the second-level choice and proceed accordingly
                if user_choice == "touch":
                    delay_print("\nAs you touch the crystals, they emit a soothing light. A hidden door opens.")
                    delay_print("You discover a secret path. Do you TAKE the path or STAY in the room?")

                    # Yet another nested loop for the third level of choices
                    while True:
                        delay_print("1. TAKE the secret path")
                        delay_print("2. STAY in the room")

                        # User input for the third-level choice
                        user_choice = input().lower()

                        # Check the third-level choice and proceed accordingly
                        if user_choice == "take":
                            congratulations()
                            return
                        elif user_choice == "stay":
                            delay_print("\nYou choose to stay in the room. Time passes, and nothing happens.")
                            delay_print("You decide to leave the room and continue exploring the forest.")
                            forest_path()
                        else:
                            delay_print("Invalid choice. Please enter 'take' or 'stay'.")

                elif user_choice == "ignore":
                    delay_print("\nYou ignore the crystals and proceed deeper into the cave.")
                    dark_tunnel()
                else:
                    delay_print("Invalid choice. Please enter 'touch' or 'ignore'.")
        
        else:
            delay_print("Invalid choice. Please enter 'mysterious stream', 'glowing cave' or 'secret door'.")

def dark_tunnel():
    # Introduction to the dark tunnel
    delay_print("\nYou find yourself in a DARK TUNNEL with faint echoes. You hear a distant ROAR.")
    delay_print("Do you PROCEED cautiously or RUN through the tunnel?")

    # Loop to handle user input until a valid choice is made
    while True:
        delay_print("1. PROCEED cautiously")
        delay_print("2. RUN through the tunnel")

        # User input for the second-level choice
        user_choice = input().lower()

        # Check the second-level choice and proceed accordingly
        if user_choice == "proceed":
            delay_print("\nYou proceed cautiously and find a hidden passage. Congratulations! You've made it through.")
            new_challenge()
            return
        elif user_choice == "run":
            delay_print("\nYou run through the dark tunnel, but it leads to a dead end. The roar gets louder. Game Over.")
            return
        else:
            delay_print("Invalid choice. Please enter 'proceed' or 'run'.")

def new_challenge():
    # Introduction to the new challenge
    delay_print("\nYou emerge from the tunnel and encounter a WIZARD's tower and a MYSTERIOUS PORTAL.")
    delay_print("What do you want to do?")

    # Loop to handle user input until a valid choice is made
    while True:
        delay_print("1. Approach the WIZARD's tower")
        delay_print("2. Enter the MYSTERIOUS PORTAL")

        # User input for the second-level choice
        user_choice = input().lower()

        # Check the second-level choice and proceed accordingly
        if user_choice == "wizard's tower":
            delay_print("\nAs you approach the wizard's tower, the wizard challenges you to a magical DUEL.")
            delay_print("Do you ACCEPT the challenge or attempt to RUN away?")

            # Yet another nested loop for the third level of choices
            while True:
                delay_print("1. ACCEPT the challenge")
                delay_print("2. RUN away")

                # User input for the third-level choice
                user_choice = input().lower()

                # Check the third-level choice and proceed accordingly
                if user_choice == "accept":
                    delay_print("\nThe wizard is impressed with your courage. He offers you a magical artifact.")
                    delay_print("Congratulations! You've completed the challenge.")
                    congratulations()
                    return
                elif user_choice == "run":
                    delay_print("\nYou attempt to run, but the wizard's magic prevents your escape. Game Over.")
                    return
                else:
                    delay_print("Invalid choice. Please enter 'accept' or 'run'.")

        elif user_choice == "mysterious portal":
            delay_print("\nYou enter the mysterious portal and find yourself in a dimension of FLOATING ISLANDS.")
            delay_print("You see a GLIDING PLATFORM and a FLYING DRAGON. What will you choose?")

            # Another nested loop for the third level of choices
            while True:
                delay_print("1. Use the GLIDING PLATFORM")
                delay_print("2. Ride the FLYING DRAGON")

                # User input for the third-level choice
                user_choice = input().lower()

                # Check the third-level choice and proceed accordingly
                if user_choice == "gliding platform":
                    delay_print("\nYou use the gliding platform and safely navigate between the floating islands.")
                    delay_print("Congratulations! You've successfully traversed the dimensional challenge.")
                    congratulations()
                    return
                elif user_choice == "flying dragon":
                    delay_print("\nYou attempt to ride the flying dragon, but it takes you on a chaotic journey.")
                    delay_print("Eventually, you crash into a floating island. Game Over.")
                    return
                else:
                    delay_print("Invalid choice. Please enter 'gliding platform' or 'flying dragon'.")

        else:
            delay_print("Invalid choice. Please enter 'wizard's tower' or 'mysterious portal'.")

def game_over():
    print("Game Over. Better luck next time!")

def congratulations():
    delay_print("Congratulations! You've successfully completed the adventure.")

# Start the game
start_game()
