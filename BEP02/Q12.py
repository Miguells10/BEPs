'''12. Escreva um programa para uma locadora de carros que pergunte a
quantidade de Km percorridos por um carro alugado e a quantidade de dias

pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro
custa R$90 por dia e R$0,20 por Km rodado. Mostre o resultado com duas
casas decimais.'''

class Aluguel:
    def __init__(self):
        self.kms_percorridos = float(input("Quantos km foram percorridos?"))
        self.dias = float(input("Quantos dias o carro foi alugado?"))
        self.preco_total = self.calcular_valor()
        self.printar = self.mostrar_valor()

    def calcular_valor(self):
       return (self.dias * 90) + (self.kms_percorridos * 0.2)

    def mostrar_valor(self):
        print(f"O valor total do aluguel foi {self.preco_total:.2f}")

class Q12:
    Aluguel()