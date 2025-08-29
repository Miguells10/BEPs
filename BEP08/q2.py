'''2. Crie uma função chamada calcular_imc que receba dois argumentos: peso (em
kg) e altura (em metros). A função deve calcular e retornar o valor do IMC. A
fórmula é: IMC = peso / (altura * altura). Crie uma segunda função para realizar a
classificação do IMC segundo a tabela:'''

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso ideal"
    elif 25.0 <= imc <= 29.9:
        return "Levemente acima do peso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade grau II (severa)"
    else:
        return "Obesidade grau III (mórbida)"

resultado = (calcular_imc(89, 1.79))
print(resultado)
print(classificar_imc(resultado))