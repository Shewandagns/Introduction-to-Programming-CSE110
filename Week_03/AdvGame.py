print("Hello, Welcomr to your advanture game.")

choice = input("You are at a crossroad, would you like to go LEFT, RIGHT or FORWARED?")

if choice.lower() == "left":
    choice = input("You encounter a monster, would you like to RUN or ATTACK?")
    
    if choice.lower() == "attack":
        choice = input("The monster is armed, do you need a KNIFE or GUN?")

        if choice.lower() == "knofe":
            print("That was not the best idea, sorry you lost!")

        elif choice.lower() == "gun":
            print("Aha! brilliant idea, You have killed the monster. You won!")

        else:
            print("please exit!")

    elif choice.lower() == "run":
        choice = input("Why choose run? Are you not brave enough? Dou you wish to CONTINUE or ABORT mission?") 
       
        if choice.lower() == "continue":
            choice = input("NIce one! I commend your bravery. Do you want to choose an ARROW or a DAGGER? ")

            if choice.lower() == "arrow":
                print("Good Choice, you have killed the monster, You won!")

            elif choice.lower() == "dagger":
                print("Oh no! the monster has killed you. You lost!")

            else:
                print("Invalid choice")

        elif choice.lower() == "abort":
            print("Poor cowerd! You lost the game!")
        else:
            print("No other options left! please exit!")
    
    else:
        print("Invalid choice, please exit!")

elif choice.lower() == "right":
    choice = input("There is a goul-like creature, do you wish to FIGHT or FLEE? ")
    
    if choice.lower() == "fight":
        print("You are so brave! You have killed the goul with the knofe you found by your side. Congrats")

    elif choice.lower() == "flee":
        print("Why so scared? it is just a game! Do you still want to PLAY or EXIT?")

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

