'''5. Você tem uma string com ruídos (caracteres especiais, múltiplos espaços, etc.) e
precisa limpá-la. A string final deve conter apenas letras, números e espaços simples,
sem múltiplos espaços consecutivos no meio.
String de Exemplo:
dados_sujos = " Olá, Mundo! #@$123 Isso é um teste. Com muitos
espaços!! "
Saída Esperada:
"Olá Mundo 123 Isso é um teste Com muitos espaços"'''
import re

dados_sujos = " Olá, Mundo! #@$123 Isso é um teste. Com muitos espaços!! "

limpo = re.sub(r'[^A-Za-zÀ-ÿ0-9 ]+', ' ', dados_sujos)

limpo = re.sub(r"\s+", ' ', limpo)

print(limpo.strip())
