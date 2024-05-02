print("You find yourself standing at the entrance of a spooky mansion.")
print("The door is slightly ajar, and you hear eerie whispers.")
# print("Type your choices in ALL CAPS.")
print("\nDo you want to ENTER the mansion or WALK AWAY?")

user_input = input("Your choice: ")

if user_input.upper() == "ENTER":
    
    print("\nYou cautiously enter the mansion. The creaking floorboards echo through the halls.")
    
    # Level 2 choices
    user_input = input("\nDo you want to go UPSTAIRS or EXPLORE the rooms? ")
    
    if user_input.upper() == "UPSTAIRS":
        print("\nAs you climb the stairs, you hear a faint sound. At the top, you find a locked door.")
        
        # Level 3 choices
        user_input = input("\nDo you want to PICK the lock or HEAD BACK downstairs? ")
       
        if user_input.upper() == "PICK":
            print("\nSuccess! You find a dusty attic with an old chest.")
            
            # Level 4 choices
            user_input = input("\nOpen the CHEST or LEAVE the attic? ")
           
            if user_input.upper() == "OPEN":
                
                print("\nInside the chest, you discover a mysterious amulet.")
                
                # Level 5 choices
                user_input = input("\nDo you want to WEAR the amulet or KEEP EXPLORING? ")
                
                if user_input.upper() == "WEAR":
                   
                    print("\nAs you put on the amulet, a magical glow surrounds you. You feel empowered!")
                
                elif user_input.upper() == "KEEP":
                    
                    print("\nYou decide to explore more of the mansion.")
                else:
                    print("\Invalid choice. The amulet begins to hum mysteriously.")
           
            elif user_input.upper() == "LEAVE":
                
                print("\nYou decide to leave the attic and continue exploring the mansion.")
           
            else:
                print("\Invalid choice. The chest seems to emanate a strange aura.")
        
        elif user_input.upper() == "HEAD BACK":
            print("\nYou decide to head back downstairs, leaving the locked door behind.")
       
        else:
            print("\Invalid choice. The locked door seems to whisper secrets.")
   
    elif user_input.upper() == "EXPLORE":
        
        print("\nYou explore the rooms, discovering dusty furniture and forgotten memories.")
        
        # Level 3 choices
        user_input = input("\nDo you want to SEARCH for clues or EXIT the mansion? ")
        
        if user_input.upper() == "SEARCH":
            
            print("\nYou find a hidden passage behind a bookshelf, leading to a secret library.")
            
            # Level 4 choices
            user_input = input("\nRead the BOOKS or LEAVE the library? ")
            
            if user_input.upper() == "READ":

                print("\nThe books reveal ancient knowledge. You gain insight into the mansion's history.")
            
            elif user_input.upper() == "LEAVE":
                print("\nYou decide to leave the library, armed with newfound knowledge.")
            else:
                print("Invalid choice. The library whispers forgotten tales.")
        
        elif user_input.upper() == "EXIT":
            print("\nYou choose to exit the mansion, leaving its mysteries behind.")
       
        else:
            print("Invalid choice. The mansion's secrets linger in the air.")
    else:
        print("Invalid choice. The mansion awaits your next move.")

elif user_input.upper() == "WALK AWAY":
    print("\nYou decide to walk away from the spooky mansion, leaving its mysteries untouched.")

else:
    print("Invalid choice. The whispers from the mansion fade as you hesitate.")
