'''2. (Adaptado de Rossi) Crie um programa que solicite o nome e o salário
do usuário e calcule o valor que a empresa deve depositar em sua conta
do FGTS.
Se o nome informado não for válido, o programa deve imprimir uma
mensagem de erro e solicitá-lo novamente. Conjunto teste na imagem
abaixo.
a) o nome deve conter de 5 a 50 caracteres.
b) o nome não pode conter números.
Se o salário informado não for válido, o aplicativo deve imprimir uma
mensagem de erro e solicitá-lo novamente.
a) o salário deve ser um número
b) o salário deve ser igual ou superior a R$ 1100,00.
Ao final o programa deve imprimir os dados que serão registrados no
recibo de pagamento do usuário: nome, salário e o valor do FGTS (8%
do salário).'''
import re

try:
    nome = input("Nome:")
    padrao = re.compile(r"^[a-zA-Z ]{5,50}$")

    if padrao.match(nome):
        print("Nome válido:", nome)

    salario = float(input("Salário"))
    if salario < 1100.0:
        raise RuntimeError ("Salario abaixo")

    print(f"""
    FGTS
    Nome: {nome}
    Salário: {salario}
    Valor fgts: {0.08 * salario}
    """)

except ValueError:
    print("tipo errado")