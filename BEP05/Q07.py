'''Desenvolva um programa em Python para registrar informações sobre
funcionários em uma empresa. Comece solicitando o número de funcionários. Para
cada funcionário, o programa deve requisitar o nome, salário e departamento
(“Vendas”, “RH” ou “Gerência”). Ao final, apresente as seguintes estatísticas:
● O nome do funcionário com o salário mais alto.
● A média dos salários dos funcionários.
● A quantidade de funcionários que trabalham no departamento de Vendas.'''

num_funcionarios = int(input("Digite o número de funcionários: "))
if num_funcionarios <= 0:
    print("Número de funcionários deve ser maior que zero.")
else:
    nome_maior_salario = ""
    maior_salario = 0
    soma_salarios = 0
    cont_vendas = 0

    for i in range(num_funcionarios):
        print(f"\nFuncionário {i + 1}:")
        nome = input("Nome: ")
        salario = float(input("Salário: "))
        departamento = input("Departamento (Vendas, RH ou Gerência): ").strip().lower()

        soma_salarios += salario

        if salario > maior_salario:
            maior_salario = salario
            nome_maior_salario = nome

        if departamento == "vendas":
            cont_vendas += 1

    media_salarios = soma_salarios / num_funcionarios

    print("\nEstatísticas:")
    print(f"Funcionário com o maior salário: {nome_maior_salario} (R$ {maior_salario:.2f})")
    print(f"Média dos salários: R$ {media_salarios:.2f}")
    print(f"Quantidade de funcionários no departamento de Vendas: {cont_vendas}")