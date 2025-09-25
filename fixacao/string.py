'''nome = "Miguel"
idade = 22
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))
print("Meu nome é {0} e eu tenho {1} anos.".format(nome, idade))

preco = 49.99
quantidade = 2

print(f"O preço total é R${preco * quantidade:.2f}")
print(f"{nome:>10}")  # Alinha à direita com largura 10

'''

import re

padrao_email = re.compile(r"{a-zA-Z0-9._%+-}+@{a-zA-Z0-9.-}+.{a-zA-Z}{2, }")

emails = ["teste@exemplo.com", "invalido.com", "usuario@dominio.com"]

for email in emails:
    if padrao_email.match(email):
        print(f"{email} é um email válido.")
    else:
        print(f"{email} não é um email válido.")
