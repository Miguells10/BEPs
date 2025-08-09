'''
Escreva um programa para ler o salário mensal atual de um funcionário e o
percentual de reajuste. Calcular e escrever o valor do novo salário com duas
casas decimais.
'''

class Calcular:
    def __init__(self):
        self.salario_atual = float(input("Digite o salário mensal atual do funcionário: "))
        self.percentual_reajuste = float(input("Digite o percentual de reajuste: "))
        self.novo_salario = self.calcular_novo_salario()
        self.mostrar_novo_salario()

    def calcular_novo_salario(self):
        return self.salario_atual * (1 + (self.percentual_reajuste / 100))

    def mostrar_novo_salario(self):
        print(f"O novo salário com reajuste é: R$ {self.novo_salario:.2f}")

class Q9:
    Calcular()