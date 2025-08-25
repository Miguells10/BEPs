'''2. Leia a idade de 20 pessoas e exiba quantas pessoas são maiores de idade.'''
import random

maior_idade= 0
for i in range(20):
    idade = random.randint(1, 100)  # Simulando a entrada de idade
    print(f"Idade da pessoa {i+1}: {idade}")
    if idade >= 18:
        maior_idade += 1
print(
"Total de pessoas maiores de idade:", maior_idade
)