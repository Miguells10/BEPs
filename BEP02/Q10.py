'''Crie um programa que leia o preço de um produto, calcule e mostre o seu
PREÇO PROMOCIONAL, com 5% de desconto e duas casas decimais.'''

class Promocao:
    def __init__(self):
        self.preco_produto = float(input("Digite o preço do produto: "))
        self.preco_promocional = self.calcular_preco_promocional()
        self.mostrar_preco_promocional()

    def calcular_preco_promocional(self):
        return self.preco_produto * 0.95

    def mostrar_preco_promocional(self):
        print(f"O preço promocional do produto é: R$ {self.preco_promocional:.2f}")

# Executando a classe Q10
class Q10:
    Promocao()