room = 0
while room == 0:
    print("You wake up in a white room what do you do")
    print("(1)KYS  (2)Try and escape")
    room = int(input())
    if room > 2:
        print("choose 1 or 2")
        room = 0
        print("You wake up in a white room what do you do")
        print("(1)KYS  (2)Try and escape")
        room = int(input())
        continue
    elif room < 1:
        print("choose 1 or 2")
        room = 0
        print("You wake up in a white room what do you do")
        print("(1)KYS  (2)Try and escape")
        room = int(input())
        continue
while room in [1,2]:
    if room == 1:
        print("you died")
        room = int(input("Do you want to play again?"
        " (1)Yes (2)No"))
        if input == 1:
            room = 0
        elif input == 2:
            print("Thanks for playing")
            break
        else:
            print("choose 1 or 2")
            room = int(input("Do you want to play again?"
            " (1)Yes (2)No"))
    elif room == 2:
        print("What do you want to do now")
        