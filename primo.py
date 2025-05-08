while True:
    number = int(input("Digite um número para verificar se é primo ou não"))
    i = 1
    aux = number
    isprimo = True
    while i < number:

            if number % aux == 0 and number != aux :
                isprimo = False
                print("não é primo")
                break

            aux -= 1
            i += 1

    if isprimo ==  True:
        print("É primo")
