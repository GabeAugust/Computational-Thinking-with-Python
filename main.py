nomes = ["João", "Maria", "Gabriel", "Pedro", "Julia"]

while True:
    print(f"Fila atual {nomes}")
    option = int(input("Digite:\n 1- Para adicionar alguém a fila\n 2-Para chamar o proximo"))
    if (len(nomes) >= 1):
        print(len(nomes))
        if option == 1:
            adicionarProximo = input("Digite o nome que deseja adicionar na fila")
            nomes.append(adicionarProximo)
        elif option == 2:
            nomes.pop(0)
        else:
            print("Opção invalida")
    else:
        print("Não tem ninguém na fila")
