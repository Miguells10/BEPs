'''2. Você precisa criar um sistema simples para armazenar informações sobre produtos de uma loja. Cada produto tem um código único (ID) e
um nome. Seu programa deve armazenar três produtos e, em seguida, permitir que o usuário digite um ID para buscar e imprimir o nome do
produto correspondente.
Dados de Entrada:
Produto 1: ID 101, Nome Camiseta
Produto 2: ID 102, Nome Calça Jeans
Produto 3: ID 103, Nome Tênis'''

produtos = {
    "produto1": {"id": 101, "nome": "camiseta"},
    "produto2": {"id": 102, "nome": "calça jeans"},
    "produto3": {"id": 103, "nome": "tenis"},
}

pedido = int(input("Digite o ID: "))

for p in produtos.values():
    if p["id"] == pedido:
        print(p["nome"])
        break

