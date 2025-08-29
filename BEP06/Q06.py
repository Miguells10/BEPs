'''Faça um programa para corrigir provas de múltipla escolha. Cada prova
contém 10 questões. A primeira lista a ser carregada é o gabarito da prova.
Os outros dados são os números de matrícula dos alunos e as respostas que
deram às questões. Considere que temos 10 alunos. Calcule e mostre o
número da matrícula e a nota de cada aluno. Mostre também a porcentagem
de aprovação.'''
import random

alternativas = ['a', 'b', 'c', 'd', 'e']
gabarito = []
num_alunos = 10
notas = []
aprovados = 0

for i in range(10):
    resposta = random.choice(alternativas)
    gabarito.append(resposta)

print("Gabarito:", gabarito)

for i in range(num_alunos):
    matricula = 1000 + i
    respostas_aluno = []
    nota = 0

    for j in range(10):
        resposta = random.choice(alternativas)
        respostas_aluno.append(resposta)
        if resposta == gabarito[j]:
            nota += 1
    print("Aluno matrícula:", matricula)
    print("Respostas:", respostas_aluno)
    print("Nota:", nota)

    notas.append((matricula, nota))
    if nota >= 6:
        aprovados += 1
porcentagem = (aprovados / num_alunos) * 100

print("Porcentagem de aprovação: ", porcentagem )