'''Carregue uma lista com temperaturas médias mensais (12) e encontre a
temperatura mais alta e mais baixa.'''

import random

temperaturas = []
for i in range(12):
    temperatura = random.randint(-10, 40)
    temperaturas.append(temperatura)

temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)

print(f"Temperaturas mensais: {temperaturas} °C")
print(f"Temperatura mais alta: {temperatura_maxima:.2f}°C")
print(f"Temperatura mais baixa: {temperatura_minima:.2f}°C")
print(f"Média das temperaturas: {sum(temperaturas)/len(temperaturas):.2f}°C")