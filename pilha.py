pilha = [1, 2, 3, 5, 6]
while True:
    print(f"Pilha atual {pilha}")
    option = int(input("Digite:\n 1- Para adicionar um elemento a pilha"
                       "\n 2-Para tirar um elemento da pilha"))
    if option == 1:
        novo_elemento = input("Digite o novo elemento da pilha que deseja adicionar: ")
        pilha.append(novo_elemento)
    elif option == 2:
        print(len(pilha))
        pilha.pop()
    else:
        print("Opção invalida")
