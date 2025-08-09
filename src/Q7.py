'''
Escreva um programa para ler o número total de eleitores de um município, o
número de votos brancos, nulos e válidos. Calcular e escrever o percentual
que cada um representa em relação ao total de eleitores.
'''

class Q7:
    print("Digite o número total de eleitores:")
    total_eleitores = int(input())

    while total_eleitores > 0:
        try:
            print("Digite o número de votos brancos:")
            votos_brancos = int(input())

            print("Digite o número de votos nulos:")
            votos_nulos = int(input())

            print("Digite o número de votos válidos:")
            votos_validos = int(input())


        percentual_brancos = (votos_brancos / total_eleitores) * 100
        percentual_nulos = (votos_nulos / total_eleitores) * 100
        percentual_validos = (votos_validos / total_eleitores) * 100

        print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
        print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
        print(f"Percentual de votos válidos: {percentual_validos:.2f}%")