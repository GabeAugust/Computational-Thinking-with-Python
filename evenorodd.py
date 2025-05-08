

while True:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    if (n1 + n2) % 2 == 0:
        print(f"A soma dos números é par")
    else:
        print(f"A soma dos números é impar")

    option = int(input("Digite 1 pra continuar e qualquer tecla pra sair: "))
    if option == 1:
        continue
    else:
        break