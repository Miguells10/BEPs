from math import sqrt


class sqrt:
    numero = int(input("Digite um numero ai: "))
    if(numero>=0):
        raiz = sqrt(numero)
        print(f"Raiz quadrada de {numero} eh: {raiz:.2f} ")
    else: print("Numero invalido")