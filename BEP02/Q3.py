#Faça um programa que leia um número inteiro e mostre o seu antecessor e
#seu sucessor.

class Q3:
    print("Digite um número inteiro:")
    numero = int(input())
    antecessor = numero - 1
    sucessor = numero + 1
    print(f"O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}.")