'''1. Você tem um texto que contém vários endereços de e-mail. Utilize expressões
regulares para extrair todos os e-mails válidos (formato básico:
nome@dominio.com ou nome@dominio.org, etc.) e armazená-los em uma lista.
Texto de Exemplo:
artigo = "Entre em contato conosco em suporte@minhaempresa.com.br ou
vendas@minhaempresa.org. Você pode me encontrar em
meu.email@pessoal.com. Ou, se preferir, use um-email_invalido@.com ou
somente texto sem email."
Saída Esperada:
['suporte@minhaempresa.com.br', 'vendas@minhaempresa.org',
'meu.email@pessoal.com']'''

import re

artigo = ("""Entre em contato conosco em suporte@minhaempresa.com.br ou vendas@minhaempresa.org. 
          Você pode me encontrar em meu.email@pessoal.com. 
          Ou, se preferir, use um-email_invalido@.com ou somente texto sem email""")

padrao_email = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

encontrados = re.findall(padrao_email, artigo)
print(encontrados)
