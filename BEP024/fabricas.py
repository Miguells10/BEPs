from abc import ABC, abstractmethod
from salas import Sala, SalaPequena, SalaMedia, Auditorio

# Simple Factory

def criar_sala_simple_factory(tipo: str) -> Sala:
    print(f"SimpleFactory: Tentando criar sala do tipo '{tipo}'...")
    if tipo == "pequena":
        return SalaPequena()
    elif tipo == "media":
        return SalaMedia()
    elif tipo == "auditorio":
        return Auditorio()
    else:
        raise ValueError(f"Tipo de sala desconhecido: {tipo}")

# Factory Method (O Padrão OCP)

class SalaFactory(ABC):
    @abstractmethod
    def criar_sala(self) -> Sala:
        pass

class SalaPequenaFactory(SalaFactory):
    def criar_sala(self) -> Sala:
        print("FactoryMethod: Usando a fábrica de Sala Pequena...")
        return SalaPequena()

class SalaMediaFactory(SalaFactory):
    """Fábrica Concreta 2"""
    def criar_sala(self) -> Sala:
        print("FactoryMethod: Usando a fábrica de Sala Média...")
        return SalaMedia()

class AuditorioFactory(SalaFactory):
    """Fábrica Concreta 3"""
    def criar_sala(self) -> Sala:
        print("FactoryMethod: Usando a fábrica de Auditório...")
        return Auditorio()