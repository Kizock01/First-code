num1 = float(input("Digite um numero:"))
conta = str(input("DIgite a operacao:"))
num2 = float(input("Digite outro numero:"))

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
