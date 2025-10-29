from poo.herançamultipla.Pessoa import Pessoa


class Ingles(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)

    def saudacaoIngles(self):
        print("Hi " + self.nome)
