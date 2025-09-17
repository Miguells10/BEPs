'''4. Em uma string que contém um tweet, extraia todas as hashtags (palavras que
começam com #). As hashtags podem conter letras, números e underscores.
Tweet de Exemplo:
tweet = "Adorei a aula de #Python hoje! #Programacao #DataScience com
#Regex_poderoso. Sem hashtag aqui."
Saída Esperada:
['#Python', '#Programacao', '#DataScience', '#Regex_poderoso']'''
import re

tweet = "Adorei a aula de #Python hoje! #Programacao #DataScience com #Regex_poderoso. Sem hashtag aqui."

padrao = re.findall(r'#\w+', tweet)

print(padrao)