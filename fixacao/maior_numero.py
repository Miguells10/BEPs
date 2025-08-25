quantidade = int(input("Quantidade de numeros: "))

for i in range(quantidade):
    numero = int(input("Digite um numero: "))

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero


print("O maior numero digitado foi:", maior)
print("O menor numero digitado foi:", menor)