'''3. Você recebeu uma frase e sua tarefa é contar a frequência de cada palavra. Para
simplificar, desconsidere maiúsculas/minúsculas (ou seja, &quot;Python&quot; e &quot;python&quot; devem
ser contadas como a mesma palavra). O resultado final deve mostrar cada palavra única
e o número de vezes que ela apareceu.'''

palavra = input('Digite uma frase: ').lower().split()
dicionario = {}

for i in palavra:
    if i in dicionario:
        dicionario[i] += 1
    else:
        dicionario[i] = 1

print(dicionario)
