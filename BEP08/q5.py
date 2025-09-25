'''5. Escreva uma função chamada somar_tudo que possa receber um número
variável de argumentos numéricos e retorne a soma de todos eles.'''


def somar_tudo(*args):
   return sum(args)

print(somar_tudo(1,4,5,23,2,5,2,54,23,2,45,2,4,2,4,2,))


