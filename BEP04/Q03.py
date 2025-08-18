'''3. Elabore um programa que defina uma senha (por exemplo, "1234"). O programa deve
pedir ao usuário que digite a senha e, em seguida, informar se o "Acesso foi permitido"
ou "negado".'''

senha ="2020"

senha_usuario = input("Digite a senha: ")
if senha == senha_usuario:
    print("Acesso concedido")
else:
    print("Acesso negado")