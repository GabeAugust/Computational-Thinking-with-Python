numbers = [1, 5 , 7 , 9]


def soma_valores (numbers):
    soma = 0
    for i in range(len(numbers)):
        soma = soma + numbers[i]
    print(soma)
soma_valores(numbers)

