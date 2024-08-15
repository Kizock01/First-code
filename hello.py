num1 = float(input("Digite um número: "))
conta = str(input("Digite a operação: "))
num2 = float(input("Digite outro número: "))

if conta == "+":
    print(num1 + num2)
elif conta == "-":
    print(num1 - num2)
elif conta == "x" or conta == "." or conta == "*":
    print(num1 * num2)
elif conta == "/":
    print(num1 / num2)
else:
    print("Operação inválida")