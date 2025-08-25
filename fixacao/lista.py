cont1=cont2=0
while True:
    print("Digite um número (0 para sair): ")
    numero = int(input())
    if numero == 0:
        break
    if numero % 3 == 0:
        print(f"{numero} é múltiplo de 3.")
        cont1= cont1 + 1
    if numero < 0:
        print(f"{numero} é negativo.")
        cont2 = cont2 + 1

print(f"Números múltiplos de 3: {cont1}")
print(f"Números negativos: {cont2}")