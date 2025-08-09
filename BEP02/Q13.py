'''Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos
ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro.
Calcule quantos dias de vida um fumante perde e exiba o total em dias.'''

class Reducao:
    def __init__(self):
        self.cigarros = int(input("Quantos cigarros voce fuma por dia?"))
        self.anos = int(input("Quantos anos voce fuma?"))
        self.dias_perdidos = self.calculo()
        self.mostrar_dias()

    def calculo(self):
        minutos_dia = self.cigarros * 10
        minutos_ano = minutos_dia * 365 * self.anos
        dias_perdidos = int((minutos_ano/60)/24)
        return dias_perdidos

    def mostrar_dias(self):
        print(f"Os dias de vida perdidos foram: {self.dias_perdidos}")

class Q13:
    Reducao()