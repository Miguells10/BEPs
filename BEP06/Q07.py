'''Faça um programa que receba o nome de cinco produtos e seus respectivos
preços, armazene-os em listas, calcule e mostre:
a. a quantidade de produtos com preço inferior a R$ 50,00;
b. o nome dos produtos com preço entre R$ 50,00 e R$ 100,00;
c. a média dos preços dos produtos com preço superior a R$ 100;'''

produtos = []
precos = []
for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: R$ "))
    produtos.append(nome)
    precos.append(preco)

lista_inferior_50 = [produtos[i] for i in range(5) if precos[i] < 50]
lista_entre_50_e_100 = [produtos[i] for i in range(5) if 50 <= precos[i] <= 100]
lista_superior_100 = [precos[i] for i in range(5) if precos[i] > 100]

print("Quantidade de produtos com preço inferior a R$ 50,00:", len(lista_inferior_50))
print("Produtos com preço entre R$ 50,00 e R$ 100,00:", lista_entre_50_e_100)
if lista_superior_100:
    media_superior_100 = sum(lista_superior_100) / len(lista_superior_100)
    print(f"Média dos preços dos produtos com preço superior a R$ 100,00: R$ {media_superior_100:.2f}")
else:
    print("Não há produtos com preço superior a R$ 100,00.")
    
