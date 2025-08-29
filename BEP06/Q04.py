'''4. Ler uma sequência de números reais e armazená-los. A sequência termina
quando for digitado o número (0) zero. Determinar o maior elemento dessa
sequência e imprimir a lista resultante.'''
import random
lista = []
while True:
    numero = float(input("Digite um número real (0 para sair): "))
    if numero == 0:
        break
    lista.append(numero)
if numero == 0:
    maior = max(lista)
    print(f"Maior número da sequência: {maior:.2f}")
else:
    print("Nenhum número foi digitado.")
print("Lista de números lidos:", lista)