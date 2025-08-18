'''8. Desenvolva um programa que leia a idade e o tempo de serviço de um trabalhador e
escreva se ele pode ou não se aposentar. As condições para aposentadoria são: ter
pelo menos 65 anos, ou ter trabalhado pelo menos 30 anos, ou ter pelo menos 60 anos
e ter trabalhado pelo menos 25 anos.'''

idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite o tempo de serviço em anos: "))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("Você pode se aposentar.")
else:
    print("Você não pode se aposentar.")

    