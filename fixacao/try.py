def validaValor(numero):
    if (numero<3 or numero>92):
        raise Exception

try:
    numero_digitado = int(input("Digite a quantidade de números para a sequência FIBONACCI:"))
    validaValor(numero_digitado)

    primeiro_numero = 1
    segundo_numero = 1

    if numero_digitado == 1:
        print(primeiro_numero)

    else:
        print(primeiro_numero, segundo_numero, end=" ")

    for numero in range(2, numero_digitado):
        sequencia = primeiro_numero + segundo_numero
        print(sequencia, end=" ")

        primeiro_numero = segundo_numero
        segundo_numero = sequencia


except ValueError:
    print("Tipo errado pae")

except Exception:
    print("Erro valor fora da faixa. 3-92 digitos")
 