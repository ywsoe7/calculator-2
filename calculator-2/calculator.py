"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce

while True:
    request = input("What do you want to count? ")
    tokens = request.split(" ")
    if "q" in tokens or "quit" in tokens:
        print("Thank you, the calculator is off.")
        break
    elif len(tokens) < 2:
        if request.isalpha():
            print("this is not a valid input")
            continue
        print("Please, provide more input ")
        continue
        
    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = "0"
    else:
        num2 = tokens[2]
    
    if len(tokens) > 3:
        num3 = tokens[3]

    if len(tokens) > 4:
        print("Please input fewer numbers.")
        continue

    result = None

    if not num1.isdigit() or not num2.isdigit():
        print("Please use numbers")
        continue
    elif operator not in ["+", "-", "*", "pow", "power", "modulo", "mod", "cube", "square", "/"]:
        print("Please, use operators like +, -, *, pow, mod, cube, square, /")
        continue
    elif operator == "+":
        result = add(float(num1), float(num2))
    elif operator == "-":
        result = subtract(float(num1), float(num2))
    elif operator == "*":
        result = multiply(float(num1), float(num2))
    elif operator == "/":
        result = divide(float(num1), float(num2))
    elif operator == "square":
        result = square(float(num1))
    elif operator == "cube":
        result = cube(float(num1))
    elif operator == "pow" or operator == "power":
        result = power(float(num1), float(num2))
    elif operator == "mod" or operator == "modulo":
        result = mod(float(num1), float(num2))
    
    print(result)
    