'''5. Um sistema precisa validar os dados de um novo usuário (nome e e-mail). Crie
um programa que aponta inconsistências nos dados inseridos. O programa deve
ler um nome e um e-mail e exibir um alerta para cada regra que não for
cumprida.
Regras de Validação:
● O nome deve ter mais de 3 caracteres. Se o comprimento (número de
caracteres) do nome for menor ou igual a 3, exiba "Alerta: O nome deve ter mais
de 3 caracteres."
● O e-mail deve conter o caractere @.Se o caractere @ não estiver presente no
e-mail, exiba "Alerta: O formato do e-mail é inválido."'''


class Q05:
    while True:
        nome = input('Nome: ')
        if len(nome) < 3:
            print('O nome deve ter mais de 3 caracteres.')
            continue
        break

    while True:
        email = input('E-mail: ')
        if email.find("@") == -1 or not "@" in email:
            print("O email está no formato errado.")
            continue
        break

    print(f"Nome: {nome}. Email: {email}")
