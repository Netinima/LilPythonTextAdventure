import math

number1 = float(input("Put in the first number: "))
operation = int(input("What would you like to do?: \n(1)Add (2)Subtract (3)Multiply (4)Divide (5)Exponentiate (6)Square Root (7)Round Up (8)Round Down (9)Absolute Value (10)Modulo (11)Factorial (12)Logarithm:  "))
if operation == 1:
    number2 = float(input("Put in the second number: "))
    print(number1 + number2)
elif operation == 2:
    number2 = float(input("Put in the second number: "))
    print(number1 - number2)
elif operation == 3:
    number2 = float(input("Put in the second number: "))
    print(number1 * number2)
elif operation == 4:
    number2 = float(input("Put in the second number: "))
    print(number1 / number2)
elif operation == 5:
    number2 = float(input("Put in the second number: "))
    print(number1 ** number2)
elif operation == 6:
    print(math.sqrt(number1))
elif operation == 7:
    print(math.ceil(number1))
elif operation == 8:
    print(math.floor(number1))
elif operation == 9:
    print(abs(number1))
elif operation == 10:
    number2 = float(input("Put in the second number: "))
    print(number1 % number2)
elif operation == 11:
    print(math.factorial(int(number1)))
elif operation == 12:
    number2 = float(input("Put in the second number:"))
    print(math.log(number1, number2))