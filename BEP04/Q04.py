'''4. Peça a idade de um usuário e, com base nela, classifique-o em uma das seguintes
categorias: "Criança" (0-12 anos), "Adolescente" (13-17 anos) ou "Adulto" (18 anos ou
mais).'''

idade = int(input("Qual sua idade? "))
if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else: print("Idade invalida")

