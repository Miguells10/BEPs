'''Crie uma função processar_pedido que receba o nome de um cliente como
primeiro argumento, seguido por uma lista variável de itens do pedido (*args), e
por fim, detalhes adicionais como argumentos nomeados (**kwargs, ex:
pagamento="cartão", entrega="urgente"). A função deve imprimir um resumo do
pedido.'''

def processar_pedido(nome, *args, **kwargs):
    print("Nome do cliente: " + nome)
    print("Itens do pedido: ", args)

    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

processar_pedido("Miguel", ("queijo, biscoito, pao"), pagamento="cartão", entrega="urgente" )