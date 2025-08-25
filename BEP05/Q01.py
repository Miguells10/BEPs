'''1. Elaborar um programa que apresente o resultado da soma e da média aritmética
dos valores pares situados entre 40 e 70 (inclusive)'''

soma = 0
cont = 0
for num in range(40, 71):
    if num % 2 == 0:
        soma += num
        cont += 1
print('Soma dos valores pares entre 40 e 70:', soma)
if cont > 0:
    media = soma / cont
    print('Média aritmética dos valores pares entre 40 e 70:', media)
else:
    print('Não há valores pares entre 40 e 70.')