'''3. Escreva uma função chamada saudar que receba um nome e uma saudacao
opcional. Se a saudação não for fornecida, ela deve usar "Olá" como padrão. A
função deve retornar uma string formatada.'''

def saudar(nome, saudacao):
    if len(saudacao) == 0:
        return print("Olá " + nome)
    else:
        return print(saudacao + nome)


chamada_nome = input("Digite um nome: ")
chamada_saudacao = input("Digite uma saudação: ")
saudar(chamada_nome, chamada_saudacao)