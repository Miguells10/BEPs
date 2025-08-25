'''9. Calcule as raízes da equação de 2° grau ( ax2 + bx + c = 0). Lembrando que: x = −b ±
√ ∆ 2a . Onde ∆ = B − 4ac . A variável a tem que ser diferente de zero. Caso seja igual,
imprima a mensagem “Não é equação de segundo grau”.'''

a = float(input("Digite o valor de a: "))
if a == 0:
    print("Não é equação de segundo grau")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A raiz única é: {x}")
    else:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        print(f"As raízes são: {x1} e {x2}")