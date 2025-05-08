

total = 0
while True:
    cod = int(input("Digite o código do produto\nCódigo Preço\n1 0,50\n2 1,00\n3 4,00\n5 7,00\n9 8,00\n"))
    if cod == 0:
        break




    if cod == 1:
        total += qnt * 0.50
    elif cod == 2:
        total += qnt * 1
    elif cod == 3:
        total += qnt * 4
    elif cod == 5:
        total += qnt * 7
    elif cod == 9:
        total += qnt * 8
    else:
        print("Código inválido")
        continue
    qnt = int(input("digite a quantidade de produtos que deseja comprar"))

print(f"a sua compra deu um total de {total}")