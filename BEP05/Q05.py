'''5. Foi feita uma pesquisa com um grupo de alunos de uma universidade, na qual se
perguntou para cada aluno o número de vezes que utilizou o restaurante da
universidade no último mês. A cada novo aluno pergunte ao usuário se ele deseja
continuar a pesquisa.Construa um algoritmo que determine:
a) O percentual de alunos que utilizaram menos que 10 vezes o restaurante;
b) O percentual de alunos que utilizaram entre 10 e 15 vezes;
c) O percentual de alunos que utilizaram o restaurante acima de 15 vezes.'''

import random

total_alunos = 0
alunos_menos_10 = 0
alunos_entre_10_15 = 0
alunos_acima_15 = 0
aluno = 1

while True:
    print("Você deseja continuar a pesquisa? (s/n)")

    continuar = input().lower()
    if continuar != 's':
        break
    else:
        total_alunos += 1
        print(("Quantas vezes você utilizou o restaurante no último mês? "))
        vezes = random.randint(1, 30)
        print(f"Aluno {aluno} utilizou o restaurante", vezes, "vezes.")
        aluno += 1

        if vezes < 10:
            alunos_menos_10 += 1

        elif 10 <= vezes <= 15:
            alunos_entre_10_15 += 1

        else:
            alunos_acima_15 += 1


percentual_menos_10 = (100 * alunos_menos_10) / total_alunos
percentual_entre_10_15 = (100 * alunos_entre_10_15) /total_alunos
percentual_acima_15 =  (100 * alunos_menos_10) / total_alunos

print(f"Percentual de alunos que utilizaram menos que 10 vezes: {percentual_menos_10:.2f}%")
print(f"Percentual de alunos que utilizaram entre 10 e 15 vezes: {percentual_entre_10_15:.2f}%")
print(f"Percentual de alunos que utilizaram acima de 15 vezes: {percentual_acima_15:.2f}%")



