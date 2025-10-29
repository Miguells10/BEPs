class Aluno:
    def __init__(self, nome, idade, media):
        self.nome = nome
        self.idade = idade
        self.media = media

    def __str__(self):
        return f"{self.nome}: {self.idade}"

    def aprovar (self):
        if self.media > 6:
            print(f"Aprovado")
        else:
            print("Reprovado")


class Professor:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.modelo: {self.ano}}"

    



class Main:

    p1 = Aluno("Miguel", 10, 9)
    print(p1.idade)

    Aluno.aprovar(p1)

