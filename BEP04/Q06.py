'''6. Escreva um programa que leia os comprimentos dos três lados de um triângulo e
determine se ele é "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou
"Escaleno" (todos os lados diferentes).Considere que para que três medidas possam
formar um triângulo, cada lado deve ser maior que zero e menor do que a soma dos
outros dois.'''

lado1 = int(input("Digite o comprimento do primeiro lado: "))
lado2 = int(input("Digite o comprimento do segundo lado: "))
lado3 = int(input("Digite o comprimento do terceiro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Os lados devem ser maiores que zero.")
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("As medidas fornecidas não podem formar um triângulo.")
else:
    if lado1 == lado2 == lado3:
        print("O triângulo é Equilátero (todos os lados iguais).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é Isósceles (dois lados iguais).")
    else:
        print("O triângulo é Escaleno (todos os lados diferentes).")