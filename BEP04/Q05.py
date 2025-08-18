'''5. Crie um programa que peça um número de 1 a 7 e imprima o dia da semana
correspondente (1 para Domingo, 2 para Segunda, etc.). Se o número estiver fora do
intervalo, exiba "Número inválido".'''

numero = int(input("Digite um numero de 1 a 7: "))

match numero:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido")
        