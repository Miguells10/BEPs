from abc import ABC, abstractmethod


class Observadores(ABC):

    @abstractmethod
    def update(self,temperatuda, umidade, pressao):
        pass
