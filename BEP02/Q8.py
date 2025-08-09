'''
Desenvolva um programa que leia os valores de A, B e C de uma equação do
segundo grau (Ax2+Bx+C) e mostre o valor de Delta.
'''

class Delta:
    def __init__(self):
        self.a = float(input("Digite o valor de A: "))
        self.b = float(input("Digite o valor de B: "))
        self.c = float(input("Digite o valor de C: "))
        self.delta = self.calcular_delta()
        self.print = self.mostrar_delta()

    def calcular_delta(self):
        return (self.b ** 2) - (4 * self.a * self.c)

    def mostrar_delta(self):
        print(f"O valor de Delta é: {self.delta:.2f}")

class Q8:
    Delta()



