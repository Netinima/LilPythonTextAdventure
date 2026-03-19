onascr = 1
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
        room = -2
        onascr = 0
        if a1 == True:
            print("You killed yourself, Why (Ending 1)")
        onascr = int(input("Leave(1)"))
        if onascr == 1:
            room = 0
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
                if a1 == False:
                    print("You've unlocked Ending 1")
                a1 = True
                play_again = int(input("Play again? (1) Yes (2) Return to Main Menu: "))
                if play_again == 1:
                    room = 0
                elif play_again == 2:
                    start = False
                    room = 0
                else:
                    print("Invalid input, please choose 1 or 2")
            
            case 2:
                print("\n=== What now?! ===")
                print("You can't really do anything yes?")
                room = int(input("(1)Punch The Wall (2)Meditate in hopes that it gvies you the right energy:  "))
                if room == 1:
                    room = 3
                else:
                    start = False
                    room = 0
            
            case 3:
                print("test")

            case _:
                print("Invalid room number!")
                room = 0
