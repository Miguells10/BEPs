import random

lista = []
lista_positiva = []
lista_negativa = []
for i in range(8):
    numero = random.randint(-100, 100)
    lista.append(numero)
    if i > 0:
        if numero > 0:
            lista_positiva.append(numero)
        else:
            lista_negativa.append(numero)

lista_positiva_compreshion = [i for i in lista if i > 0]
lista_negativa_compreshion = [i for i in lista if i <= 0]

print("Lista completa:", lista)
print("Lista positiva:", lista_positiva)
print("Lista negativa:", lista_negativa)

print("-----------------------------------------------------------")
print("Lista positiva (comprehension):", lista_positiva_compreshion)
print("Lista negativa (comprehension):", lista_negativa_compreshion)