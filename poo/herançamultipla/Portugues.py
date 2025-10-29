from poo.herançamultipla.Pessoa import Pessoa


class Portugues(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)
        self.nome = nome

    def saudacao(self):
        print("Oi, " + self.nome)