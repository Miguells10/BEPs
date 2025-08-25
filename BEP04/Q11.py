'''11. Crie uma calculadora de Índice de Massa Corporal (IMC) que, além de calcular o
valor (peso / altura2), classifique o resultado de acordo com as seguintes faixas:
● Abaixo de 18.5: Abaixo do peso
● 18.5 a 24.9: Peso ideal
● 25.0 a 29.9: Levemente acima do peso
● 30.0 a 34.9: Obesidade grau I
● 35.0 a 39.9: Obesidade grau II (severa)
● Acima de 40.0: Obesidade grau III (mórbida)'''

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso ideal")
elif 25.0 <= imc <= 29.9:
    print("Levemente acima do peso")
elif 30.0 <= imc <= 34.9:
    print("Obesidade grau I")
elif 35.0 <= imc <= 39.9:
    print("Obesidade grau II (severa)")
else:
    print("Obesidade grau III (mórbida)")

