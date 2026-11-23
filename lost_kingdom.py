name = input("What is your name: ")
choice = int(input("Welcome,",name,"!""Chapter 1 — The Forest\nIntroduction:\nYou wake up in a mysterious forest. You don't remember anything about your past.\nYou find a letter on the ground:\n\"The kingdom is in danger. The king has disappeared. Find him before it's too late.\"\nYou look around and discover three paths.\n\n\t1- Ancient Castle\n\t2- Dark Cave\n\t3- Nearby Village\n\nYour choice determines which Chapter 2 you enter.\n "))
if choice == 1:
    decision = int(input("Chapter 2A: Ancient Castle\nYou arrive at an ancient castle. A guard blocks the entrance.\nWhat do you do?\n\n\t1. Talk to the guard.\n\t2. Try to sneak inside.\n\t3. Attack the guard.\n\n"))
    if decision == 1:
        print("The guard tells you the king disappeared inside the dungeon.")
    elif decision == 2:
        print("You successfully enter the castle.")
    elif decision == 3:
        print("The guard defeats you. Game over.")
    else:
        print("Please enter a valid number (1,2,3)")
elif choice == 2:
    decision = int(input("Chapter 2B: Dark Cave\nYou enter a dark cave and discover an old treasure chest.\nWhat do you do?\n\n\t1. Open the chest.\n\t2. Ignore the chest and explore deeper.\n\t3. Leave the cave.\n\n"))
    if decision == 1:
        print("You discover a mysterious golden key.")
    elif decision == 2:
        print("You discover an ancient sword.")
    elif decision == 3:
        print("You return to the forest.")
    else:
        print("Please enter a valid number (1,2,3)")
elif choice == 3:
    decision = int(input("Chapter 2C: Nearby Village\nYou arrive at a small village. An old man approaches you.\nWhat do you do?\n\n\t1. Ask about the missing king.\n\t2. Ask for directions to the castle.\n\t3. Ignore him.\n\n"))
    if decision == 1:
        print("He tells you the king was last seen near the castle.")
    elif decision == 2:
        print("He gives you directions to the castle.")
    elif decision == 3:
        print("You leave without learning anything.")
    else:
        print("Please enter a valid number (1,2,3)")
else:
    print("Please enter a valid number (1,2,3)")