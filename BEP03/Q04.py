'''4. Um e-commerce permite que um cliente aplique múltiplos cupons em uma
compra. O sistema deve calcular o valor final com base nos cupons válidos
inseridos e no valor do frete de R$ 15. Crie um programa que leia o valor total da
compra e dois cupons (como texto). O valor final deve ser atualizado
sequencialmente.

Cupons Válidos:
● ‘desconto10’: Aplica 10% de desconto sobre o valor.
● ‘fretegratis’: Subtrai R$ 15,00 do valor.'''
import re

class Q04:

    estoque = {"mel": 12.00,
               "leite": 10.00,
               "farinha": 5.00,
               "arroz": 8.00}

    cupons = {
        "desconto10": 10,
        "fretegratis": 15.00}

    carrinho = 0.00
    pedido = ""
    cupons_usados = set()

    print("O que voce deseja comprar?")
    for produto, preco in estoque.items():
        print(f"{produto}: R$ {preco:.2f}")

    while True:
        pedido = input("Digite o nome do produto. Ou 0 para sair: ")
        if pedido == "0":
            break

        if pedido in estoque:
            carrinho += estoque[pedido]
            print(f"Produto adicionado. Total: {carrinho:.2f}")

    while True:
        print("Deseja adicionar cupom? s ou n")
        if input().lower() == "s":
            aplicar_cupom = input("Digite o nome do cupom: ")
            try:
                    if aplicar_cupom in cupons_usados:
                        print("Cupom já está sendo utilizado")
                        continue
                    if aplicar_cupom in cupons:
                        if aplicar_cupom.startswith("desconto"):
                            porcentagem = int(re.search(r"\d+", aplicar_cupom).group())
                            carrinho -= carrinho * (porcentagem/100)
                            print(f"Desconto adicionado. Total: {carrinho:.2f}")

                        elif aplicar_cupom.startswith("frete"):
                            carrinho -= 15;
                            print(f"Desconto adicionado. Total: {carrinho:.2f}")
                        cupons_usados.add(aplicar_cupom)


                    else: print("Digite um cupom valido")
                    print()

            except Exception as e:
                print("Erro: " + e)

        else: break

    print(f"Valor final do carrinho: {carrinho:.2f}. Muito obrigado pela compra e volte sempre!")







