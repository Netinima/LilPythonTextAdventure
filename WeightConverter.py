number1 = float(input("measurement you would like to convert: "))
confrom = int(input("What unit is the measurement in?: \n(1)Pounds (2)Ounces (3)Grams (4)Kilograms: "))
conto = int(input("What unit would you like to convert to?: \n(1)Pounds (2)Ounces (3)Grams (4)Kilograms: "))
if confrom == 1 and conto ==1:
    print(f"{number1}Lb")
elif confrom == 1 and conto == 2:
    print(f'{number1 * 16}Oz')
elif confrom == 1 and conto == 3:
    print(f"{number1*453.592}g")
elif confrom == 1 and conto == 4:
    print(f'{number1*0.453592}kg')
elif confrom == 2 and conto == 1:
    print(f"{number1*0.0625}Lb")
elif confrom == 2 and conto == 2:
    print(f"{number1}Oz")
elif confrom == 2 and conto == 3:
    print(f"{number1*28.3495}g")
elif confrom == 2 and conto == 4:
    print(f"{number1*0.0283495}kg")
elif confrom == 3 and conto == 1:
    print(f"{number1*0.00220462}Lb")
elif confrom == 3 and conto == 2:
    print(f"{number1*0.035274}Oz")
elif confrom == 3 and conto == 3:
    print(f"{number1}g")
elif confrom == 3 and conto == 4:
    print(f"{number1*0.001}kg")
elif confrom == 4 and conto == 1:
    print(f"{number1*2.20462}Lb")
elif confrom == 4 and conto == 2:
    print(f"{number1*35.274}Oz")
elif confrom == 4 and conto == 3:
    print(f"{number1*1000}g")
elif confrom == 4 and conto == 4:
    print(f"{number1}kg")