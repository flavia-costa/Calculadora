from calculator import *

def menu():
    print("--------(Calculator)---------")
    print("Choose desired operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exponentiation")
    print("0 - Exit")
    print("-------------------------------")

while True:
    menu()
    op = input("Enter the desired option: ")

    if op == '0':
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if op == '1':
        result = addition(num1, num2)
    elif op == '2':
        result = subtraction(num1, num2)
    elif op == '3':
        result = multiplication(num1, num2)
    elif op == '4':
        result = division(num1, num2)
    elif op == '5':
        result = exponentiation(num1, num2)

    print("----------------------")
    print("Result: ", result)
