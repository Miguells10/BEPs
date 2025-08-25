'''6. Escrever um algoritmo que leia um conjunto de 50 informações contendo, cada
uma delas, a altura e o sexo biológico de uma pessoa (1 - masculino 2-feminino),
calcule e mostre o seguinte:
a) a maior e a menor altura da turma
b) a média da altura das mulheres
c) a média da altura da turma.'''
import random
total_pessoas = 50

soma_altura_mulheres = 0
cont_mulheres = 0
soma_altura_total = 0

while total_pessoas > 0:
    altura = round(random.uniform(1.5, 2.0), 2)  # Simulando a entrada de altura
    sexo = random.choice([1, 2])  # Simulando a entrada de sexo (1 - masculino, 2 - feminino)
    print(f"Altura: {altura} m, Sexo: {'Masculino' if sexo == 1 else 'Feminino'}")

    if total_pessoas == 50:
        maior_altura = altura
        menor_altura = altura
    else:
        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura

    if sexo == 2:  # Feminino
        soma_altura_mulheres += altura
        cont_mulheres += 1

    soma_altura_total += altura
    total_pessoas -= 1

media_altura_mulheres = soma_altura_mulheres / cont_mulheres
media_altura_total = soma_altura_total / 50

print(f"Maior altura da turma: {maior_altura} m")
print(f"Menor altura da turma: {menor_altura} m")
print(f"Média da altura das mulheres: {media_altura_mulheres:.2f} m" if cont_mulheres > 0 else 0)
print(f"Média da altura da turma: {media_altura_total:.2f}" )