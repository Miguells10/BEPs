#Escreva um algoritmo para ler as dimensões de um retângulo (base e altura),
#calcular e escrever a área do retângulo

class Q5:
    print("Digite a base do retângulo:")
    base = float(input())
    print("Digite a altura do retângulo:")
    altura = float(input())
    area = base * altura
    print(f"A área do retângulo com base {base:.2f} e altura {altura:.2f} é {area:.2f}.")