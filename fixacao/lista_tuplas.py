'''2. Você tem uma lista de tuplas, onde cada tupla contém o nome de um produto e
seu preço. Você precisa formatar esses dados em uma string para exibição,
garantindo que o preço tenha sempre duas casas decimais e o nome do produto
esteja alinhado para a esquerda em um campo de 20 caracteres.
Dados de Exemplo:
produtos = [("Notebook", 1200.5), ("Mouse", 25.99), ("Teclado Mecânico", 150.0)]'''

produtos = [("Notebook", 1200.5), ("Mouse", 25.99), ("Teclado Mecânico", 150.0)]

print("Produtos: ")
for nome, preco in produtos:
    print(f"Nome: {nome:<20} - Preço: {preco:.2f}")
