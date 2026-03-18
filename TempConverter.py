confrom = int(input("What is the unit of tempurature in?: \n(1)farenheit (2)kelvin (3)celsius:"))
temp = float(input("Enter your temperature here: "))
conto = int(input("What would you like to convert it to?: \n(1)farenheit (2)kelvin (3)celsius: "))
if confrom == 1 and conto == 1:
    print(temp)
if confrom == 1 and conto == 2:
    print(temp - 32 * 5/9 + 273.15)
if confrom == 1 and conto == 3:
    print(temp-32*5/9)