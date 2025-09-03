'''Crie uma função chamada gerar_relatorio que receba um número variável
de argumentos nomeados (keyword arguments) e imprima um relatório
formatado com cada par chave-valor. Ex: gerar_relatorio(nome="João
Silva", idade=30, cidade="São Paulo", profissao="Engenheiro")
e retornaria:
Nome: João Silva
Idade: 30
Cidade: São Paulo
Profissao: Engenheiro'''

def gerar_relatorio (**kwargs):
    for chave, valor in kwargs.items():
        print(f"`{chave} : {valor}")


gerar_relatorio(nome="João Silva", idade=30, cidade="São Paulo", profissao="Engenheiro")