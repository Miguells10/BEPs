#Faça um programa que leia a largura e altura de uma parede, calcule e mostre
#a área a ser pintada e a quantidade de tinta necessária para o serviço,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

class Q6:
    print("Qual é a largura da parede (em metros)?")
    largura = float(input())
    print("Qual é a altura da parede (em metros)?")
    altura = float(input())

    area = largura * altura
    tinta_necessaria = area / 2  # Cada litro de tinta pinta 2 m²

    print(f"A área a ser pintada é de {area:.2f} m².")
    print(f"A quantidade de tinta necessária é de {tinta_necessaria:.2f} litros.")