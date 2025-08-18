'''1. Desenvolva um programa que solicite um número inteiro e, usando a estrutura
if-else, determine e exiba se o número é "Par" ou "Ímpar".'''

numero = int(input("Qual o numero inteiro?"))
if numero % 2 == 0:
    print(f"O numero {numero} é par")
else:
    print(f"O numero {numero} é impar")
