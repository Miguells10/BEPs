'''
Escreva um programa para ler o número total de eleitores de um município, o
número de votos brancos, nulos e válidos. Calcular e escrever o percentual
que cada um representa em relação ao total de eleitores.
'''

class Q7:
    print("Digite o número total de eleitores:")
    total_eleitores = int(input())
    contagem = total_eleitores

    while contagem > 0:
        try:
            print("Digite o número de votos brancos:")
            votos_brancos = int(input())
            contagem -= votos_brancos

            print("Digite o número de votos nulos:")
            votos_nulos = int(input())
            contagem -= votos_nulos

            print("Digite o número de votos válidos:")
            votos_validos = int(input())
            contagem -= votos_validos
            if contagem < 0:
                raise ValueError("A soma dos votos não pode exceder o total de eleitores.")
            if contagem > 0:
                raise ValueError("Todos os votos devem ser contabilizados.")

        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")
            continue

        percentual_brancos = (votos_brancos / total_eleitores) * 100
        percentual_nulos = (votos_nulos / total_eleitores) * 100
        percentual_validos = (votos_validos / total_eleitores) * 100

        print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
        print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
        print(f"Percentual de votos válidos: {percentual_validos:.2f}%")