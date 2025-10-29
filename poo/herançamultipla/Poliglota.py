from poo.herançamultipla.Ingles import Ingles
from poo.herançamultipla.Portugues import Portugues


class Poliglota(Portugues, Ingles):
    def __init__(self, nome):
        Portugues.__init__(self, nome)
        Ingles.__init__(self, nome)
        self.nome = nome

p1 = Poliglota("Miguel")

p1.saudacao()
p1.saudacaoIngles()