'''3. Leia o nome e a idade de 10 pessoas e exiba o nome da pessoa mais nova.'''

pessoas = []
for i in range(3):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    pessoas.append((nome, idade))

    if i == 0:
        mais_nova = (nome, idade)
    else:
        if idade < mais_nova[1]:
            mais_nova = (nome, idade)

print("Mais nova:", mais_nova[0], "com idade", mais_nova[1])