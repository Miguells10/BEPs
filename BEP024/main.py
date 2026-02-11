from config import Configuracoes

from fabricas import (
    criar_sala_simple_factory,
    SalaPequenaFactory,
    AuditorioFactory
)

def executar_demonstracao():
    print("--- 1. Teste do Singleton ---")

    config1 = Configuracoes()

    config1.empresa = "IFS"
    print(f"Config 1: {config1.get_config()}")

    config2 = Configuracoes()

    print(f"Config 2: {config2.get_config()}")
    print(f"config1 é a mesma instância que config2? {config1 is config2}\n")

    print("--- 2. Teste da Simple Factory (A 'Função') ---")

    s1 = criar_sala_simple_factory("media")
    s1.reservar()

    s2 = criar_sala_simple_factory("auditorio")
    s2.reservar()
    print("")

    # ---

    print("--- 3. Teste do Factory Method ---")

    fabrica_pequena = SalaPequenaFactory()
    sala_pequena = fabrica_pequena.criar_sala()
    sala_pequena.reservar()

    fabrica_auditorio = AuditorioFactory()
    sala_auditorio = fabrica_auditorio.criar_sala()
    sala_auditorio.reservar()
    print("")

if __name__ == "__main__":
    executar_demonstracao()