'''12. Desenvolva um programa que faça 5 perguntas para uma pessoa sobre um crime:
1. "Telefonou para a vítima no último mês?"
2. "Esteve no local do crime na última semana?"
3. "Mora perto da vítima?"
4. "Devia para a vítima?"
5. "Já trabalhou com a vítima?"
O programa deve classificar a pessoa como "Inocente", "Suspeita" (2 respostas
positivas), "Cúmplice" (3 ou 4 respostas positivas) ou "Assassino" (5 respostas
positivas).'''

perguntas = [
    "Telefonou para a vítima no último mês? (s/n) ",
    "Esteve no local do crime na última semana? (s/n) ",
    "Mora perto da vítima? (s/n) ",
    "Devia para a vítima? (s/n) ",
    "Já trabalhou com a vítima? (s/n) "
]

respostas_positivas = 0
for pergunta in perguntas:
    resposta = input(pergunta).lower()
    if resposta == 's':
        respostas_positivas += 1
    elif resposta != 'n':
        print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
        exit()
if respostas_positivas == 5:
    classificacao = "Assassino"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"
print(f"Classificação: {classificacao}")
