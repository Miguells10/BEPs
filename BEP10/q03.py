'''3. (Adaptado de Rossi) Crie um novo script que solicite um número
inteiro e indique se ele é um número perfeito. Um número perfeito é
um número inteiro para o qual a soma de todos os seus divisores
positivos menores que ele é igual ao próprio número. Ex: 6 = 1+2+3.
O número informado deve ser maior que zero e deve ser menor ou igual
a 32767.
Se o dado informado não for um número ou se o número for maior que
32767, o programa deve informar a mensagem: “Erro: dado inválido”.
Se o número não for maior que zero, o programa deve imprimir a
mensagem: “Erro: o número deve ser maior que zero.”. Conjunto teste
na imagem abaixo.'''

try:
    numero = int(input("Numero:"))
    if numero > 32767:
        raise RuntimeError("Erro: dado inválido")
    if numero < 0:
        raise RuntimeError("Erro: o número deve ser maior que zero.")

    soma = 0
    i = 1

    while i < numero:
        if numero % i == 0:
            soma += i
        i += 1

    if soma == numero:
        print("perfeito")
    else:
        print("imperfeito")
except ValueError:
    print("Tipo errado")

