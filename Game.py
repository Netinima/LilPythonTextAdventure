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
if room == 1:
    print("you died")
elif room == 2:
    print("What do you want to do now")
    break
    