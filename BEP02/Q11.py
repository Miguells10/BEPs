'''Faça um programa que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento. Mostre o resultado com duas casas
decimais.'''

class Aumento:
    def __init__(self):
        self.salario = float(input("Digite o salario: "))
        self.aumento_salario = self.calcular_aumento_salario()
        self.mostrar_aumento_salario()

    def calcular_aumento_salario(self):
        return self.salario + (self.salario * 0.15)

    def mostrar_aumento_salario(self):
        print(f"O novo salário é: R$ {self.aumento_salario:.2f}")
class Q11:
    Aumento()
