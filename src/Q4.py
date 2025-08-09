#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira (em
#R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,50.

class Q4:
    print("Quanto dinheiro você tem na carteira (em R$)?")
    dinheiro = float(input())
    cotacao_dolar = 5.50
    dolares = dinheiro / cotacao_dolar
    print(f"Com R$ {dinheiro:.2f}, você pode comprar US$ {dolares:.2f}.")