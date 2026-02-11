from abc import abstractmethod

from Bep028.Observadores import Observadores


class DisplayDecorator(Observadores):
    def __init__(self, display_decorado: Observadores):
        self.display_decorado = display_decorado

    @abstractmethod
    def update(self, temperatura, umidade, pressao):
        pass