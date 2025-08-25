'''10. Simule um caixa eletrônico. Peça ao usuário o valor do saque (inteiro). O programa
deve informar o número de notas de R$ 100, R$ 50, R$ 20, R$ 10 necessárias para
compor o valor. Suponha que o caixa sempre tem notas disponíveis e que o valor do saque é
múltiplo de 10.'''
saque = int(input("Digite o valor do saque (múltiplo de 10): "))
if saque % 10 != 0:
    print("O valor do saque deve ser múltiplo de 10.")
else:
    notas_100 = saque // 100
    saque %= 100
    notas_50 = saque // 50
    saque %= 50
    notas_20 = saque // 20
    saque %= 20
    notas_10 = saque // 10

    print(f"Notas de R$ 100: {notas_100}")
    print(f"Notas de R$ 50: {notas_50}")
    print(f"Notas de R$ 20: {notas_20}")
    print(f"Notas de R$ 10: {notas_10}")