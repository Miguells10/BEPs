from abc import ABC, abstractmethod

class Sala(ABC):
    @abstractmethod
    def reservar(self):
        pass

class SalaPequena(Sala):
    def reservar(self):
        print("Sala Pequena reservada com sucesso.")

class SalaMedia(Sala):
    def reservar(self):
        print("Sala Média reservada com sucesso.")

class Auditorio(Sala):
    def reservar(self):
        print("Auditório reservado com sucesso.")