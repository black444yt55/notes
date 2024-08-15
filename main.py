# Basic Calculator

while True:
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))

    oper = input("Choose: + , - , / , *")
    if oper == '-':
        print("Sub is: ", num1-num2)
    elif oper == '+':
        print("Sum is: ", num1 + num2)
    elif oper == '/':
        print("Result: ", num1/num2)
    elif oper == '*':
        print("Multiply is: ", num1*num2)

    else:
        print("Invalid Option Please Choose Again")
