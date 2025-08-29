'''1. Carregue uma lista com 20 números inteiros e armazene em outra lista
apenas os números pares e outra os ímpares.'''

import random
numeros = []
for i in range(20):
    numero = random.randint(1, 100)
    numeros.append(numero)

numeros_pares = [num for num in numeros if num % 2 == 0]
numeros_impares = [num for num in numeros if num % 2 != 0]