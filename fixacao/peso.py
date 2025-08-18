altura = float(input("Qual sua altura? "))
sexo = input("Qual o seu sexo? h ou m: ")

if(sexo.lower() == "h"):
    peso_ideal = (altura * 72.7) -58
    print(f"O peso ideal é: {peso_ideal} ")
elif(sexo.lower() == "m"):
    peso_ideal = (altura * 62.1) -44.7
    print(f"O peso ideal é: {peso_ideal}")
else: print("Digite um caracter valido")
