from abc import ABC

from Bep028.Observadores import Observadores

class Sujeito(ABC):
    def __init__(self):
        self._observadores = []

    def registrar_observadores(self, obs: Observadores):
        self._observadores.append(obs)

    def remover_observadores(self, obs: Observadores):
        self._observadores.remove(obs)

    def notificar_observadores(self, temp, umid, press):
        for i in self._observadores:
            i.update(temp, umid, press)