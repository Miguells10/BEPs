'''3. Você está desenvolvendo um sistema de controle de estoque. O programa deve
ler a quantidade atual de um produto e emitir alertas específicos baseados no
nível do estoque. Se a quantidade em estoque for igual a 0, exiba a mensagem:
"ALERTA: Produto esgotado. Realizar pedido de compra urgente!". Se a
quantidade em estoque for menor que 10 (e maior que 0), exiba a mensagem:
"AVISO: Estoque baixo. Considerar fazer novo pedido." os dois alertas devem
ser realizados um independente do outro, ou seja, as duas verificações devem
ser realizadas.'''

estoque = {"mel": 12,
           "leite": 10,
           "farinha": 0,
           "arroz": 8}

#For para listar os produtos e quantidade
for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade}")

print("----------------------------")
#For para fazer a verificação de estoque
for produto, quantidade in estoque.items():
    if quantidade == 0:
        print(f"ALERTA: Produto {produto} esgotado. Realizar pedido de compra urgente!")
    elif quantidade < 10:
        print(f"AVISO: Estoque de {produto} baixo")

