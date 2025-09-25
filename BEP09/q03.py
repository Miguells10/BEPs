'''3. Dada uma string que representa um parágrafo, divida-a em uma lista de sentenças.
Considere que uma sentença termina com ponto (.), ponto de interrogação (?) ou ponto
de exclamação (!). Ignore espaços extras entre as sentenças.

Parágrafo de Exemplo:
paragrafo = "Olá! Como você está? Espero que esteja tudo bem. Este é
um exemplo de parágrafo. Fim."
Saída Esperada:
['Olá', 'Como você está', 'Espero que esteja tudo bem', 'Este é um
exemplo de parágrafo', 'Fim']'''
import re

paragrafo = "Olá! Como você está? Espero que esteja tudo bem. Este é um exemplo de parágrafo. Fim."

sentencas = re.split(r'[.!?]\s*', paragrafo)

sentencas = [s.strip() for s in sentencas if s.strip()]

print(sentencas)