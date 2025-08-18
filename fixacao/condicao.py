class condicao:
    salario = float(input("Qual seu salario? "))
    if(salario <= 300):
        salario += salario * 0.35
    else: salario += salario * 0.15

    print(f"Salario total R$ {salario}")


