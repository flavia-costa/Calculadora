from calculadora import *

def menu():
    print("--------(Calculadora)---------")
    print("Escolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exponenciação")
    print("0 - Sair")
    print("-------------------------------")


while True:
    menu()
    op = input("Digite a opção desejada: ")

    if op == '0':
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if op == '1':
        resultado = soma(num1, num2)
    elif op == '2':
        resultado = subtracao(num1, num2)
    elif op == '3':
        resultado = multiplicacao(num1, num2)
    elif op == '4':
        resultado = divisao(num1, num2)
    elif op == '5':
        resultado = expoenciacao(num1, num2)
   
    print("----------------------")
    print("Resultado: ", resultado)

