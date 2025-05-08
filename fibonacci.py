termo = int(input("Digite o numéro de termos que vc quer"))
i = 0
x = 1
y = 1
result = 0
print(0)
while i < termo:

    y = x
    x = result
    result = x + y
    print(result)

    i += 1

