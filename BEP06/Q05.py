'''Durante o planejamento de uma obra, um engenheiro registrou a quantidade
de sacos de cimento utilizados em cada um dos 7 dias da semana. Escreva
um programa em Python que leia a quantidade de sacos para cada dia e
exiba o total de sacos de cimento usados na semana. Crie uma nova lista
apenas com os dias em que o consumo foi acima de 29 sacos (utilize list
comprehension) e exiba essa lista.'''

import random
sacos_por_dia = []
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
total_sacos = 0
for dia in dias_semana:
    sacos = random.randint(10, 40)  # Simulando a entrada de sacos de cimento
    sacos_por_dia.append(sacos)
    total_sacos += sacos
    print(f"{dia}: {sacos} sacos")
print("Total de sacos de cimento usados na semana:", total_sacos)
dias_acima_29 = [sacos for sacos in sacos_por_dia if sacos > 29]
print("Dias com consumo acima de 29 sacos:", dias_acima_29)
