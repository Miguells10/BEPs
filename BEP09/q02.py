'''2. Crie uma função que valide se uma string corresponde ao formato de placa de
carro brasileira antiga (3 letras, 4 números) ou nova (3 letras, 1 número, 1 letra,
2 números). A função deve retornar True se a placa for válida e False caso
contrário.
Exemplos de Teste:
● "ABC1234" -> True (formato antigo)
● "XYZ9A87" -> True (formato novo)
● "ABC123" -> False
● "1234ABC" -> False
● "ABCD1234" -> False'''
import re

placa = input("Escreva sua placa: ")

padrao_placa_antiga = re.compile(r"[A-Z]{3}[0-9]{4}")
padrao_placa_nova = re.compile(r"[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}")

if padrao_placa_antiga.match(placa):
    print(True, ". formato antigo")
elif padrao_placa_nova.match(placa):
    print(True,  "formato novo")
else: False