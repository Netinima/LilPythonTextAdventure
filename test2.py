room = 0
start = False
a1 = False

while True:
    print("Welcome to my Game I made it for practice")
    print("What would you like to do: \nStart(1) Quit(2) View Unlocked Endings(3)")
    option = int(input())
    
    if option == 1:
        start = True
    elif option == 2:
        print("Thanks for playing!")
        break
    elif option == 3:
        print("View Unlocked Endings - Coming Soon")
        continue
    else:
        print("Invalid option, please choose 1, 2, or 3")
        continue

    while start == True:
        match room:
            case 0:
                print("\n=== You wake up in a white room ===")
                print("(1)KYS  (2) Try to escape")
                room = int(input("What do you do? "))
            
            case 1:
                print("\n=== You Died, should we celebrate ===")
                print("Game Over!")
                play_again = int(input("Play again? (1) Yes (2) Return to Main Menu: "))
                if play_again == 1:
                    room = 0
                elif play_again == 2:
                    start = False
                    room = 0
                else:
                    print("Invalid input, please choose 1 or 2")
            
            case 2:
                print("\n=== You escape! ===")
                print("Congratulations! You found your way out.")
                room = int(input("(1) Continue to next level (2) Quit: "))
                if room == 1:
                    room = 3
                else:
                    start = False
                    room = 0
            
            case 3:
                print("\n=== You enter a dark corridor ===")
                print("(1) Go left (2) Go right")
                room = int(input("Which path? "))
                if room == 1:
                    print("You found treasure!")
                    start = False
                    room = 0
                elif room == 2:
                    print("You hit a dead end.")
                    room = 0
            
            case _:
                print("Invalid room number!")
                room = 0
