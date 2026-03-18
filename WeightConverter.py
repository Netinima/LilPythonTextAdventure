number1 = float(input("measurement you would like to convert: "))
confrom = int(input("What unit is the measurement in?: \n(1)Pounds (2)Ounces (3)Grams (4)Kilograms: "))
conto = int(input("What unit would you like to convert to?: \n(1)Pounds (2)Ounces (3)Grams (4)Kilograms: "))
if confrom == 1 and conto ==1:
    print(f"{number1}Lb")