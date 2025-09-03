'''4. Crie uma função chamada analisar_notas que receba uma lista de notas. A
função deve retornar três valores: a maior nota, a menor nota e a média das
notas'''

lista = [0]


def analisar_notas(notas):
    print(max(notas))
    print(min(notas))
    print(sum(notas)/len(notas))


analisar_notas(lista)
