#1. Crie um programa que leia o nome e o salário de um funcionário, mostrando
#no final uma mensagem. “O funcionário [nome] tem um salário de R$
#[salario].

class Q1:
    print("Qual é o nome do funcionário?")
    nome = input()
    print("Qual é o salário do funcionário?")
    salario = float(input())
    print(f"O funcionário {nome} tem um salário de R$ {salario:.2f}.")
