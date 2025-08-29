'''Fazer um programa para ler uma lista de 5 elementos, e, em seguida,
mostrar a posição(não o índice) onde se encontram o maior e o menor valor
e seus respectivos valores.'''

import random
lista = []
for i in range(5):
    numero = random.randint(1, 100)
    lista.append(numero)

maior = max(lista)
menor = min(lista)
posicao_maior = lista.index(maior) + 1
posicao_menor = lista.index(menor) + 1
print("Lista:", lista)
print(f"Maior valor: {maior} na posição {posicao_maior}")
print(f"Menor valor: {menor} na posição {posicao_menor}")