'''7. Desenvolva um programa que calcule um aumento de salário. Para salários de até R$
1.250,00, o aumento é de 15%. Para salários superiores, o aumento é de 10%. Exiba o
novo salário com duas casas decimais.'''

salario = float(input("Digite o salário: R$ "))
if salario <= 1250.00:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
novo_salario = salario + aumento
print(f"Novo salário: R$ {novo_salario:.2f}")