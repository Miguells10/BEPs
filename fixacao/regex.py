'''a) Contar quantas vezes a palavra "Python" (ignorando maiúsculas/minúsculas)
aparece na frase.'''

import re

texto = "Python é uma linguagem excelente para programar. Adoro programar em Python e aprender mais sobre Python."
texto_lowercase = texto.lower()
contador = 0
padrao = r"python"
encontrados = re.findall(padrao, texto_lowercase)
print("Contagem: ", len(encontrados))


'''b) Substituir todas as ocorrências de "programar" por "desenvolver"
'''

nova_frase = texto.replace("programar", "desenvolver")
print(nova_frase)