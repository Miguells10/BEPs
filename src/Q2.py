#Faça um programa que leia as duas notas de um aluno em uma matéria e
#mostre na tela a sua média na disciplina com a mensagem: “A média entre
#[nota1] e [nota2] é igual a [média].

class Q2:
    print("Qual é a primeira nota do aluno?")
    nota1 = float(input())
    print("Qual é a segunda nota do aluno?")
    nota2 = float(input())
    media = (nota1 + nota2) / 2
    print(f"A média entre {nota1:.1f} e {nota2:.1f} é igual a {media:.1f}.")