'''8. Você tem uma lista de produtos, onde cada produto é um dicionário. Crie uma
função filtrar_produtos que recebe a lista de produtos e um preco_maximo. A
função deve retornar uma nova lista contendo apenas os produtos cujo preço é
menor ou igual ao preco_maximo.'''


lista = [
    {"nome": "videogame", "preco": 2000, "unidades": 5},
    {"nome": "carro", "preco": 20000, "unidades": 5},
    {"nome": "tv", "preco": 33000, "unidades": 5},
]

def filtrar_produtos(produtos, preco_maximo):
    nova_lista = [p for p in produtos if p["preco"] <= preco_maximo]


    for produto in nova_lista:
        print(f"{produto['nome']} - Preço: {produto['preco']} - Unidades: {produto['unidades']}")

    if not nova_lista:
        print("Não há produtos com esse valor.")

    return nova_lista

filtrar_produtos(lista, 400)





