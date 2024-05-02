print("Welcome to the Dark Dungeon Adventure!")
print("\nYou find yourself standing at the entrance of a mysterious dungeon.")
print("The air is damp, and the only light comes from a flickering torch on the wall.")
print("\nAs you venture deeper, you encounter a fork in the path, Go LEFT and Go RIGHT")

# Initialization and First Choice
print("\nWhich one would you choose?") 
print("1. LEFT")
print("2. RIGHT")
   
choice = input().lower()
# first level
if choice == "left":
    print("\nYou head down the left path and discover a room with two doors.")
    print("One door is marked with a SKILL sympbol, and the other with a KEY.")
    
    # second Level 
    print("\nWhich door do you choose?")
    print("1. Enter the SKULL door")
    print("2. Enter the KEY door")

    choice = input().lower()

    if choice == "skull":
        print("\nAs you enter the SKULL door, you encounter a room filled with spooky apparitions.")
        print("\nYou can either FIGHT them or try to SNEAK pat. What do you want to do?")

        # Third level
        print("1. FIGHT")
        print("2. SNEAK")

        choice = input().lower()

        if choice == "fight":
            print("\nYou bravely face the apparitions and defeat them. You find a treasure chest!")
            print("Congradulations! You emerge victorious.")
        elif choice == "sneak":
            print("\nYou attempt to sneak past the apparitions, but they catch you!")
            print("Game Over. Better luck next time.")

        else:
            print("Invalid choice. Game Over.")

    elif choice == "key":
        print("\nYou open they KEY door and find a room with a giant LOCKED chest and small HOLE in the wall.")
        print("Do you want to try OPENING the chest or GRAWL through the hole?")
        
        # Third level
        print("1. OPEN the chest")
        print("2. CRAWL through the hole")

        choice = input().lower()

        if choice == "open":
            print("\nCongradulations! you find a valuable artifact inside the chest.")
            print("You've successfilly completed the adventure.")

        elif choice == "crawl":
            print("\nAs you crawl through the hole, you discover a hiden passage.")
            print("Unfortunately, it leads to a dead end. Game Over.")

        else:
            print("Invalid choice. Game Over.")

elif choice == "right":
    print("\nYou chose the right path and encounter a room with a mysterious ALTAR and a dark CAVERN.")
    print("\nWhat do you want to do?")

    # Second level
    print("1. Apporoach the ALTAR")  
    print("2. Enter the CAVERN")

    choice = input().lower()

    if choice == "altar":
        print("\nAs you approach the altar, you feel a strange energy. A voice whispers, 'Sacrifice or PRAY.")
        
        # Third level
        print("1. Sacrifice")
        print("2. Pray")

        if choice == "sacrifice":
            print("\nYou make a sacrifice, and a hidden door opens. Congran")
        elif choice == "pray":
            print("Your prayers are answered, and hidden door opens. Congradulations! You move forward.")
        else: 
            print("Invalid choice. Game Over.")

    elif choice == "cavarn":
        print("\nYou enter the dark cavern and find a mysterious POOL and a GLOWING MUSHROOM.")
        print("What do you want to do?")

        # Third level
        print("1. Inspect the POOL")
        print("2. Pick the GLOWING MUSHROOM")

        choice = input().lower()

        if choice == "pool":
            print("\nAs you inspect the pool, you find a magical option. Congradulations!")
            print("You've successfully comleted the advanture.")
        elif choice == "glowing muchroom":
            print("\nYou pick the glowing mushroom, but it's poisonous. Game Over.")
        else:
            print("Invalid choice. Game Over.")

    else:
        print("Invalid choice. Game Over.")

else:
    print("Invalid choice. Game Over.")


