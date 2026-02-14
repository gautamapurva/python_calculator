# ADVANCED COMMAND LINE CALCULATOR

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_division(x, y):
    if y != 0:
        return x // y
    else:
        return "Error: Division by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Negative number"

def percentage(x, y):
    return (x / y) * 100


print("===== ADVANCED CALCULATOR =====")

while True:
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Floor Division (//)")
    print("8. Square Root")
    print("9. Percentage")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == '0':
        print("Exiting calculator... Goodbye!")
        break

    elif choice in ('1','2','3','4','5','6','7','9'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input!")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '6':
            print("Result:", modulus(num1, num2))
        elif choice == '7':
            print("Result:", floor_division(num1, num2))
        elif choice == '9':
            print("Result:", percentage(num1, num2), "%")

    elif choice == '8':
        try:
            num = float(input("Enter number: "))
            print("Result:", square_root(num))
        except ValueError:
            print("Invalid number input!")

    else:
        print("Invalid choice! Please select a valid option.")
