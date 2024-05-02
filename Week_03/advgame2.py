print("Welcome to the Enchanted Forest Adventure!")
print("You find yourself at the entrance of a magical forest. A talking OWL appears and says:")
choice = input("'To proceed, answer my riddle: What has keys but can't open locks?")

if choice.lower() == "piano":
    print("Correct! The owl nods and guides you deeper into the forest.")
else:
    print("Incorrect! The owl hoots disapprovingly. The forest entrance fades away. Game Over.")

choice = input("As you venture further, you encounter a DOOR, a MYSTERIOUS STREAM and a GLOWING CAVE entrance.")
print("Which path will you choose?")

if choice.lower() == "mystreious stream":
    print("You follow the stream and encounter a friendly WATER NYMPH.")
    choice = input("She offers you a magical DRINK. Do you ACCEPT or REFUSE?")
    
    if choice.lower() == "accept":
        print("Congradulations! You have recieved power, however in your path you have encounter a monster.")
        choice = input("The monster is armed, do you need a KNIFE or GUN?")

        if choice.lower() == "knofe":
            print("That was not the best ichoice, sorry you were killed!")

        elif choice.lower() == "gun":
            print("Aha! brilliant idea, You have killed the monster. You won!")

        else:
            print("please exit!")

    elif choice.lower() == "refuse":
        choice = input("Why choose refuse? Are you not brave enough? Dou you wish to ACCEPT or ABORT mission?") 
       
        if choice.lower() == "accept":
            choice = input("That is a good choice! I commend your bravery. Do you want to choose an ARROW or a DAGGER? ")

            if choice.lower() == "arrow":
                print("Good Choice, you have killed the monster, You won!")

            elif choice.lower() == "dagger":
                print("Oh no! You were killed the monster. You lost!")

            else:
                print("Invalid choice")

        elif choice.lower() == "abort":
            print("Sorry to see you go! You lost the game!")
        else:
            print("No other options left! please exit!")
    
    else:
        print("Invalid choice, please exit!")

elif choice.lower() == "glowing cave":
    print("You enter the glowing cave and find yourself in a room with FLOATING CRYSTALS.")
    choice = input("Do you TOUCH the crystals or IGNORE them? ")
    
    if choice.lower() == "touch":
        print("As you touch the crystals, they emit a soothing light. A hidden door opens.")
        choice = input("You discover a secret path. Do you TAKE the path or STAY in the room?")

    elif choice.lower() == "take":
        print("Congradulation")

        if choice.lower() == "play":
            print("Nice choice, You have a gun! kill the goul! ")
            print("Congrats! You have killed it!")

        elif choice.lower() == "exit":
            print("Sorry coward! try again next time")

        else:
            print("Please try again next time, Thanks")

    else:
        print("Please, enter a valid option")

elif choice.lower() == "Forward":
    choice = input("This Option is is boring, do you wish to PROCEED or QUIT? ")

    if choice.lower() == "proceed":
        print("It is a lonely path, You are alone in this journey! Mission Faild! try other option")

    elif choice.lower() == "quit":
        print("Okay have a lovely day!")

    else:
        print("please leave the game")

else:
    print("That is too bad, Ga,e over")

